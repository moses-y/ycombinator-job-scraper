from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
YOUR_PHONE_NUMBER = '+254729625258'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(message):
  try:
      message = client.messages.create(
          body=message,
          from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
          to=f'whatsapp:{YOUR_PHONE_NUMBER}'
      )
      print(f"Message sent: {message.sid}")
  except Exception as e:
      print(f"Error sending WhatsApp message: {str(e)}")