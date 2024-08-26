from twilio.rest import Client
import os

# Load environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
YOUR_PHONE_NUMBER = os.environ.get('YOUR_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(message):
  try:
      # Split the message into chunks if it exceeds 1600 characters
      max_length = 1600
      message_chunks = [message[i:i + max_length] for i in range(0, len(message), max_length)]
      
      for chunk in message_chunks:
          sent_message = client.messages.create(
              body=chunk,
              from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
              to=f'whatsapp:{YOUR_PHONE_NUMBER}'
          )
          print(f"Message sent: {sent_message.sid}")
  except Exception as e:
      print(f"Error sending WhatsApp message: {str(e)}")