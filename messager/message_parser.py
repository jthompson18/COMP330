import re

class MessageParseError(Exception):
	"""
	Exception to be thrown by MessageParser. 
	This Exception is thrown when a message being parsed by parse_message is not a string.
	And when a list of messages to be parsed by batch_parse_message is not of type list.
	"""
	def __init__(self, value):
		"""

		:params value: String value for the Exception to display in stacktrace.
		"""
		self.value = value

	def __str__(self):
		return repr(self.value)

class MessageParser:
	"""
	Message Parser for twitter/slack like messages. Prior to reaching this module the messages will have been validated.

	**Considerations:**\n

	*\tA mention is defined as any alphanumerical character or underscore('_') preceded by an ' @' for up to 15 characters. \n
	*\tA topic is defined as any alphanumerical characters or special character preceded by an ' #' for any length of characters. \n
	*\tA URI is defined as a shortend URI that is shortend into a predefined format that begins with ' https://'. \n
	*\tAll validation will have been completed prior to the use of this module. \n
	*\tEmojis are not currently being handled explicityly. It is assumed they are in a string based encoding so they will be handled as such. \n

	**ReExs:**\n

	*\tMentions: (?<!\S)(@[A-Za-z0-9\_]{1,self.MAX_MENTION_LENGTH}) where MAX_MENTION_LENGTH is 15
	*\tTopics: (?<!\S)(#[A-Za-z0-9\_]+)
	*\tURIs: (?<!\S)(https?:\/\/\S{1,self.MAX_URI_LENGTH}) where MAX_URI_LENGTH is 23

	"""
	def __init__(self):
		self.MAX_MENTION_LENGTH = '15'
		self.MAX_URI_LENGTH = '23'

		#TODO add handling for real mentions, i.e., mentions that map to other users versus dead/inacitve mentions

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