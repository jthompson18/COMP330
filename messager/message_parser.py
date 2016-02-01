import re

class MessageParser:
	def __init__(self):
		self.MAX_MENTION_LENGTH = '15'

		self.mentions_regex = '(?<!\S)(@[A-Za-z0-9_]{1,'+self.MAX_MENTION_LENGTH+'})'
		self.topics_regex =  '(?<!\S)(#\S+)'
		self.uri_regex = '(?<!\S)(https?:\/\/\S+)'

	def _get_mentions_from_msg(self, message):
		mentions_regex = re.compile(self.mentions_regex)
		mentions = re.findall(mentions_regex, message)
		print mentions
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
		parsedMessage = {
			'msg_text': message,
			'mentions': self._get_mentions_from_msg(message),
			'topics': self._get_topics_from_msg(message),
			'uris': self._get_uris_from_msg(message)
		}
		return parsedMessage

	def batch_parse_message(self, messages):
		parsedMessages = []
		for msg in messages:
			parsed_msg = {
				'msg_text': u'msg',
				'mentions': self._get_mentions_from_msg(msg),
				'topics': self._get_topics_from_msg(msg),
				'uris': self._get_uris_from_msg(msg),
			}
			parsedMessages.append(parsed_msg)
		return parsedMessages