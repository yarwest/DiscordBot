import discord
import asyncio

client = discord.Client()
variables = {}

with open("vars.conf", "r") as file:
    for line in file:
        if line[0] != "#" and line[0] != "":
            varName,varValue = line.split("=")
            varValue = varValue[:len(varValue)-1]
            variables[varName] = varValue

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.send_message(client.get_channel(variables["generalChannelID"]), "hi guys, bot up and running")

@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "what the hell are you testing for")
    elif message.content.startswith("!flokkie"):
        await client.send_message(message.channel, "checkout it'sFlokkie at https://twitch.tv/itsFlokkie")
    elif message.content.startswith("!help"):
        await client.send_message(message.channel, "WIP")

client.run(variables["botToken"])

client.close()
