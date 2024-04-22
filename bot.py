import discord
from dotenv import load_dotenv
from os import environ

load_dotenv()


class EchoBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.bot:
            return
        print(f"Got message from {message.author}: {message.content}")
        await message.reply(message.content)


intents = discord.Intents.default()
intents.message_content = True

client = EchoBot(intents=intents)
client.run(environ["DISCORD_TOKEN"])
