import re

class MessageParseError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class MessageParser:
	def __init__(self):
		self.MAX_MENTION_LENGTH = '15'
		self.MAX_TOPIC_LENGTH = '15'
		self.MAX_URI_LENGTH = '23'

		self.mentions_regex = '(?<!\S)(@[A-Za-z0-9_]{1,'+self.MAX_MENTION_LENGTH+'})'
		self.topics_regex =  '(?<!\S)(#[A-Za-z0-9_]{1,'+self.MAX_TOPIC_LENGTH+'})'
		self.uri_regex = '(?<!\S)(https?:\/\/\S{1,'+self.MAX_URI_LENGTH+'})'

	def _get_mentions_from_msg(self, message):
		mentions_regex = re.compile(self.mentions_regex)
		mentions = re.findall(mentions_regex, message)
		return mentions

	def _get_topics_from_msg(self, message):
		topics_regex = re.compile(self.topics_regex)
		topics = re.findall(topics_regex, message)
		return topics

	def _get_uris_from_msg(self, message):
		uri_regex = re.compile(self.uri_regex)
		uris = re.findall(uri_regex, message)
		return uris

	def parse_message(self, message):
		if type(message) is str:
			parsed_message = {
				'msg_text': message,
				'mentions': self._get_mentions_from_msg(message),
				'topics': self._get_topics_from_msg(message),
				'uris': self._get_uris_from_msg(message)
			}
			return parsed_message
		else:
			raise MessageParseError('message must be of type str')

	def batch_parse_message(self, messages):
		parsed_messages = []
		if type(messages) is list:
			for msg in messages:
				parsed_msg = self.parse_message(msg)
				parsed_messages.append(parsed_msg)
			return parsed_messages
		else:
			raise MessageParseError('arg for batch_parse must be list')