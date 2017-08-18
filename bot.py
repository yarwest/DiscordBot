import discord
import asyncio

client = discord.Client()
ownerID = "" # ID of your user account
generalChannelID = "" # ID of the channel in which you want the bot to be most active
botToken = "" # Insert the token of your bot account here

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.send_message(client.get_channel(generalChannelID), "hi guys, bot up and running")

@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "what the hell are you testing for")
    elif message.content.startswith("!flokkie"):
        await client.send_message(message.channel, "checkout it'sFlokkie at https://twitch.tv/itsFlokkie")
    elif message.content.startswith("!help"):
        await client.send_message(message.channel, "WIP")

client.run(botToken)

client.close()
