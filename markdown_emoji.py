#!/usr/bin/env python3
# encoding: utf-8

import asyncio

from emoji_connoisseur.utils import emote as emote_utils
from emoji_connoisseur.utils import errors as emoji_connoisseur_errors
import markdown.extensions
import markdown.inlinepatterns
import markdown.util

from bot import *

loop = asyncio.get_event_loop()

class DatabaseEmotePattern(markdown.inlinepatterns.Pattern):
	def handleMatch(self, match):
		full_text = match.group(0)

		element = markdown.util.etree.Element()
		if emote_utils.RE_ESCAPED_EMOTE.match(full_text) or emote_utils.RE_CUSTOM_EMOTE.match(full_text):
			element.text = full_text
			return element

		try:
			result = str(loop.run_until_complete(db_cog.get_emote(match.group('name'))))
		except emoji_connoisseur_errors.EmoteNotFoundError:
			result = full_text

		element.text = markdown.util.AtomicString(result)
		return element

	def getCompiledRegex(self):
		return emote_utils.RE_EMOTE

class DatabaseEmoteExtension(markdown.extensions.Extension):
	def extendMarkdown(self, markdown, markdown_globals):
		# TODO investigate whether putting this ext at the end is the best place
		markdown.inlinePatterns.add('database_emote', DatabaseEmotePattern(markdown), '_end')
