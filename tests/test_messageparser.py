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
		test_message = "This is a test @testing #testing https://testing"
		parsed_message = MP.parse_message(test_message)
		self.assertEqual(parsed_message['msg_text'], test_message, 'message not found')
		self.assertEqual(parsed_message['mentions'][0], '@testing', 'mention not found')
		self.assertEqual(parsed_message['topics'][0], '#testing', 'topic not found')
		self.assertEqual(parsed_message['uris'][0], 'https://testing', 'uri not found')

	def test_batch_parse_message(self):
		MP = self.MessageParser
		test_messages = [
		"This is a test @testing_basic09 #testing_basic09 https://testing",
		"This is also a test @stilltesting #testing #software #engineering http://testing"
		]
		parsed_messages = MP.batch_parse_message(test_messages)
		self.assertEqual(parsed_messages[0]['msg_text'], test_messages[0], 'message not found')
		self.assertEqual(parsed_messages[0]['mentions'][0], '@testing_basic09', 'mention not found')
		self.assertEqual(parsed_messages[0]['topics'][0], '#testing_basic09', 'topic not found')
		self.assertEqual(parsed_messages[0]['uris'][0], 'https://testing', 'uri not found')

	def test_parse_mentions(self):
		MP = self.MessageParser
		test_mentions = [
			"@testing_12345678@testing2_1234567",
			"@test*",
			"@test&",
			"@test$",
			"@test!",
			"@test@",
			"@test%",
			"@test^",
			"@test(",
			"@test)",
			"@test1 @test2"
			]
		parsed_ment_0 = MP._get_mentions_from_msg(test_mentions[0])
		self.assertEqual(parsed_ment_0, ['@testing_1234567'], 'Mention length not working')
		parsed_ment_1 = MP._get_mentions_from_msg(test_mentions[1])
		self.assertEqual(parsed_ment_1, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_2 = MP._get_mentions_from_msg(test_mentions[2])
		self.assertEqual(parsed_ment_2, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_3 = MP._get_mentions_from_msg(test_mentions[3])
		self.assertEqual(parsed_ment_3, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_4 = MP._get_mentions_from_msg(test_mentions[4])
		self.assertEqual(parsed_ment_4, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_5 = MP._get_mentions_from_msg(test_mentions[5])
		self.assertEqual(parsed_ment_5, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_6 = MP._get_mentions_from_msg(test_mentions[6])
		self.assertEqual(parsed_ment_6, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_7 = MP._get_mentions_from_msg(test_mentions[7])
		self.assertEqual(parsed_ment_7, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_8 = MP._get_mentions_from_msg(test_mentions[8])
		self.assertEqual(parsed_ment_8, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_9 = MP._get_mentions_from_msg(test_mentions[9])
		self.assertEqual(parsed_ment_9, ['@test'], 'Not catching special char in parse mentions')
		parsed_ment_10 = MP._get_mentions_from_msg(test_mentions[10])
		self.assertEqual(parsed_ment_10, ['@test1', '@test2'], 'Not handling space seperted mentions')


	@unittest.expectedFailure
	def test_parse_mentions_should_fail(self):
		MP = self.MessageParser
		test_mentions = [
			"@test1@test2",
			]
		parsed_ment_0 = MP._get_mentions_from_msg(test_mentions[0])
		self.assertEqual(parsed_ment_0, ['@test1', '@test2'], 'Improperly handling non space deliminated mentions')

	# def test_parse_topics(self):
	# 	MP = self.MessageParser
	# 	test_topics = [
	# 		"#testing_12345678#testing2_1234567",
	# 		"#test*",
	# 		"#test&",
	# 		"#test$",
	# 		"#test!",
	# 		"#test@",
	# 		"#test%",
	# 		"#test^",
	# 		"#test(",
	# 		"#test)",
	# 		"#test1@test2"
	# 		]
	# 	]

	# @unittest.expectedFailure
	# def test_parse_topics_should_fail(self):
	# 	MP = self.MessageParser
	# 	test_topics = []

	# def test_parse_uris(self):
	# 	MP = self.MessageParser
	# 	test_uris = []

	# @unittest.expectedFailure
	# def test_parse_uris_should_fail(self):
	# 	MP = self.MessageParser
	# 	test_uris = []