import re

class MessageParseError(Exception):
	"""
	Exception to be thrown by MessageParser. 
	This Exception is thrown when a message being parsed is not a sting and when a list of messages to be parsed is not of type list.
	"""
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class MessageParser:
	"""
	.. autoclass:: MessageParser

	Message Parser for twitter/slack like messages. Prior to reaching this module the messages will have been validated.
	"""
	def __init__(self):
		"""
		Set up regexs for parsing the message based on twitter criteria.
		"""
		self.MAX_MENTION_LENGTH = '15'
		self.MAX_URI_LENGTH = '23'

		self.mentions_regex = '(?<!\S)(@[A-Za-z0-9_]{1,'+self.MAX_MENTION_LENGTH+'})'
		self.topics_regex =  '(?<!\S)(#[A-Za-z0-9_]+)'
		self.uri_regex = '(?<!\S)(https?:\/\/\S{1,'+self.MAX_URI_LENGTH+'})'

	def _get_mentions_from_msg(self, message):
		"""
		Function to return a list of mentions found in a message. This is for internal use by the MessageParser class.

		:param message: String message to be parsed
		:return: List of found mentions or an empty list
		"""
		mentions_regex = re.compile(self.mentions_regex)
		mentions = re.findall(mentions_regex, message)
		return mentions

	def _get_topics_from_msg(self, message):
		"""
		Function to return a list of topics found in a message. This is for internal use by the MessageParser class.

		:param message: String message to be parsed
		:return: List of found topics or an empty list
		"""
		topics_regex = re.compile(self.topics_regex)
		topics = re.findall(topics_regex, message)
		return topics

	def _get_uris_from_msg(self, message):
		"""
		Function to return a list of URIs found in a message. This is for internal use by the MessageParser class.

		:param message: String message to be parsed
		:return: List of found URIs or an empty list
		"""
		uri_regex = re.compile(self.uri_regex)
		uris = re.findall(uri_regex, message)
		return uris

	def parse_message(self, message):
		"""
		Function to parse a given message. The message should be validated and all URIs shortend prior to calling this method.

		:param message: Sting message to be parsed
		:return: Returns a python objects containing stinrg-msg_text, list-mentions, list-topics, and list-uris.
		"""
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
		"""
		Function to parse a multiple messages. The message should be validated and all URIs shortend prior to calling this method.

		:param messages: List of strings to be parsed.
		:return: Returns a list of messages. See parse_message for message return information.
		"""
		parsed_messages = []
		if type(messages) is list:
			for msg in messages:
				parsed_msg = self.parse_message(msg)
				parsed_messages.append(parsed_msg)
			return parsed_messages
		else:
			raise MessageParseError('arg for batch_parse must be list')