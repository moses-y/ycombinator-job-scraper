import unittest
from unittest.mock import patch
from src.messaging import send_whatsapp_message

class TestMessaging(unittest.TestCase):
  @patch('src.messaging.client.messages.create')
  def test_send_whatsapp_message(self, mock_create):
      message = "Test message"
      send_whatsapp_message(message)
      mock_create.assert_called_once()

if __name__ == '__main__':
  unittest.main()