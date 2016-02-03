import unittest
import messager

from messager.message_parser import MessageParser, MessageParseError

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

		with self.assertRaises(MessageParseError) as cm:
			MP.parse_message([])

		the_exception = cm.exception
		self.assertEquals(the_exception.value, 'message must be of type str')

		with self.assertRaises(MessageParseError) as cm:
			MP.parse_message({})

		another_exception = cm.exception
		self.assertEquals(another_exception.value, 'message must be of type str')

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

		self.assertEqual(parsed_messages[1]['msg_text'], test_messages[1], 'message not found')
		self.assertEqual(parsed_messages[1]['mentions'][0], '@stilltesting', 'mention not found')
		self.assertEqual(parsed_messages[1]['topics'], ['#testing', '#software', '#engineering'], 'topics not found')
		self.assertEqual(parsed_messages[1]['uris'][0], 'http://testing', 'uri not found')

		with self.assertRaises(MessageParseError) as cm:
			MP.batch_parse_message({})

		first_exception = cm.exception
		self.assertEquals(first_exception.value, 'arg for batch_parse must be list')

		with self.assertRaises(MessageParseError) as cm:
			MP.batch_parse_message('test')

		second_exception = cm.exception
		self.assertEquals(second_exception.value, 'arg for batch_parse must be list')

		with self.assertRaises(MessageParseError) as cm:
			MP.batch_parse_message(1)

		third_exception = cm.exception
		self.assertEquals(third_exception.value, 'arg for batch_parse must be list')

	def test_parse_mentions(self):
		MP = self.MessageParser
		test_mentions = [
			"@testing_12345678",
			"@test*",
			"@test&",
			"@test$",
			"@test!",
			"@test@",
			"@test%",
			"@test^",
			"@test(",
			"@test)",
			"@test1 @test2",
			"@test1@test2"
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
		self.assertEqual(parsed_ment_10, ['@test1', '@test2'], 'Not handling space separated mentions')

		parsed_ment_11 = MP._get_mentions_from_msg(test_mentions[11])
		self.assertNotEqual(parsed_ment_11, ['@test1', '@test2'], 'Improperly handling non space deliminated mentions')

	def test_parse_topics(self):
		MP = self.MessageParser
		test_topics = [
			"#testing_12345678",
			"#test*",
			"#test&",
			"#test$",
			"#test!",
			"#test@",
			"#test%",
			"#test^",
			"#test(",
			"#test)",
			"#test1 #test2",
			"#test1#test2"
			]

		parsed_topic_0 = MP._get_topics_from_msg(test_topics[0])
		self.assertEqual(parsed_topic_0, ['#testing_12345678'], 'Topic length not working')
		parsed_topic_1 = MP._get_topics_from_msg(test_topics[1])
		self.assertEqual(parsed_topic_1, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_2 = MP._get_topics_from_msg(test_topics[2])
		self.assertEqual(parsed_topic_2, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_3 = MP._get_topics_from_msg(test_topics[3])
		self.assertEqual(parsed_topic_3, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_4 = MP._get_topics_from_msg(test_topics[4])
		self.assertEqual(parsed_topic_4, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_5 = MP._get_topics_from_msg(test_topics[5])
		self.assertEqual(parsed_topic_5, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_6 = MP._get_topics_from_msg(test_topics[6])
		self.assertEqual(parsed_topic_6, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_7 = MP._get_topics_from_msg(test_topics[7])
		self.assertEqual(parsed_topic_7, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_8 = MP._get_topics_from_msg(test_topics[8])
		self.assertEqual(parsed_topic_8, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_9 = MP._get_topics_from_msg(test_topics[9])
		self.assertEqual(parsed_topic_9, ['#test'], 'Not catching special char in parse topics')
		parsed_topic_10 = MP._get_topics_from_msg(test_topics[10])
		self.assertEqual(parsed_topic_10, ['#test1', '#test2'], 'Not handling space separated Topics')

		parsed_topic_11 = MP._get_topics_from_msg(test_topics[11])
		self.assertNotEqual(parsed_topic_11, ['#test1', '#test2'], 'Improperly handling non space deliminated mentions')

	def test_parse_uris(self):
		MP = self.MessageParser
		test_uris = [
			"https://validURI&(*&#@)!",
			"https://validURI https://validURI",
			"https://validURIhttps://validURI",
			]

		parsed_uri_0 = MP._get_uris_from_msg(test_uris[0])
		self.assertEqual(parsed_uri_0, ['https://validURI&(*&#@)!'], 'Topic length not working')
		parsed_uri_1 = MP._get_uris_from_msg(test_uris[1])
		self.assertEqual(parsed_uri_1, ['https://validURI', 'https://validURI'], 'Not handling space separated URIs')
		parsed_uri_2 = MP._get_uris_from_msg(test_uris[2])
		self.assertNotEqual(parsed_uri_2, ['https://validURI', 'https://validURI'], 'Improperly handling non space deliminated mentions')
		