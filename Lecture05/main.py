# This example requires the 'message_content' intent.
import os
import discord
from dotenv import load_dotenv

load_dotenv()

discord_Token = os.getenv("API-KEY")
g_Token = os.getenv("G-KEY")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if client.user != message.author:
        if client.user in message.mentions:
            channel = message.channel

            from google import genai

            client_google = genai.Client(api_key=g_Token)

            response = client_google.models.generate_content(
                model="gemini-2.5-flash", contents=message.content
            )
            print(response.text)

            await channel.send(response.text)


client.run(discord_Token)
