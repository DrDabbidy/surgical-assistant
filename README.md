# Surgical Assistant
A bot for my Discord server, spitalul.

# Functions
- Command $trans(dest_lang, message): translates the given message to the destination language and outputs it to the same channel.
- Command $lang(language): returns the two-letter code of the given language for use with the $trans function.
- Command $troll_text(message): returns the message in meme text, similar to the spongebob memes. ex: hello --> h E l L o
- "Snarky Comments": responds to given keywords with a respective response (linked in a dictionary).
- $latex(message): renders LaTeX, given the code in the message. Also accepts options -d (deletes the original message) and -light (makes the background white and text colour black, as opposed to the standard discord colours)
- $embed(message): creates an embed to make nice messages for announcements, for example.

# Files
- .env: contains the bot token for more secure use.
- Surgical_Assistant_Commands: contains code for control of the bot via custom commands.
- Surgical_Assistant_Events: contains code for control of the bot via events like on_ready() and on_message().
