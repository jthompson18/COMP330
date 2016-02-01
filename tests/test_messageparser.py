import unittest
import messager

from messager.message_parser import MessageParser

class TestMessageParser(unittest.TestCase):
	def setUp(self):
		self.MessageParser = MessageParser()

	def tearDown(self):
		self.MessageParser = None

	def test_parse_message(self):
		MP = self.MessageParser
		test_messages = [
		"This is a test @testing #testing https://testing",
		]
		parsed_message = MP.parse_message(test_messages[0])
		print parsed_message['mentions'][0]
		self.assertEqual(parsed_message['msg_text'], test_messages[0], 'message not found')
		self.assertEqual(parsed_message['mentions'][0], '@testing', 'mention not found')
		self.assertEqual(parsed_message['topics'][0], '#testing', 'topic not found')
		self.assertEqual(parsed_message['uris'][0], 'https://testing', 'uri not found')