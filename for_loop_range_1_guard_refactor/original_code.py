# original code:
# https://github.com/jwshields/noodlebot/blob/cddd6cb60bcb635a9b6539e61515abcac96e46ed/extensions/subclasses/customcontext.py#L98-L115
# the idea is to refactor this abuse of control flow into a proper guard

async def my_on_message(self, message):
    """This function replaces `bot.on_message`"""
    # Ignore bots without a heavy check on each command, this kills it right at the message receipt
    if message.author.bot:
        return
    # A check to see if the message should be ignored
    for _ in range(1):
        if str(message.author.id) in self.bot.c.trustedusers:
            break
        if message.guild is not None:
            if str(message.guild.id) in self.bot.c.trustedservers:
                break
            if str(message.guild.id) in self.bot.ignored.guilds:
                return
            if str(message.channel.id) in self.bot.ignored.channels:
                return
        if str(message.author.id) in self.bot.ignored.users:
			return
