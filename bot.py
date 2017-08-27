import discord
import asyncio

client = discord.Client()
variables = {}

def initVars():
    with open("vars.conf", "r") as file:
        for line in file:
            if line[0] != "#" and line[0] != "":
                varName,varValue = line.split("=")
                varValue = varValue[:len(varValue)-1]
                variables[varName] = varValue

async def moveToChannel(channel):
    if True:
        vc = await client.join_voice_channel(channel)
    else:
        vc = await client.move_to(channel)
    return vc

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.send_message(client.get_channel(variables["generalChannelID"]), "hi guys, bot up and running")

@client.event
async def on_message(message):
    content = message.content
    if content.startswith("!test"):
        await client.send_message(message.channel, "what the hell are you testing for")
    elif content.startswith("!flokkie"):
        await client.send_message(message.channel, "checkout it'sFlokkie at https://twitch.tv/itsFlokkie")
    elif content.startswith("!help"):
        await client.send_message(message.channel, "WIP")
    elif content.startswith("!github"):
        await client.send_message(message.channel, "Fork me on GitHub! https://github.com/yarwest/DiscordBot")
    elif content.startswith("!vars"):
        initVars()
        await client.send_message(message.channel, "Vars updated")
    elif content.startswith("!sb"):
        content = content.strip("!sb ")
        author = message.author
        channel = author.voice_channel
        vc = await moveToChannel(channel)

    elif content.startswith("!yt"):
        content = content.strip("!yt ")
        if content == "":
            await client.send_message(message.channel, "Include a link to play audio from YouTube")
        else:
            if content == "developers" or content == "devs":
                link = "https://www.youtube.com/watch?v=KMU0tzLwhbE"
            else:
                link = content
            author = message.author
            channel = author.voice_channel

            vc = await moveToChannel(channel)
            player = await vc.create_ytdl_player(link)
            await client.send_message(message.channel, link)
            player.start()

initVars()

client.run(variables["botToken"])

client.close()
