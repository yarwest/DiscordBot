import discord
import asyncio

client = discord.Client()
variables = {}
commands = {}
vc = None

def initVars():
    with open("vars.conf", "r") as file:
        for line in file:
            line = line.strip()
            if line[0] != "#" and line[0] != "":
                varName,varValue = line.split("=")
                variables[varName] = varValue

def initCommands():
    with open("commands.conf", "r") as file:
        for line in file:
            if line[0] != "#" and line[0] != "":
                commandName,commandResponse= line.split("=")
                commands[commandName] = commandResponse

def initLocal():
    initVars()
    initCommands()

async def moveToChannel(channel):
    if vc != None:
        if vc.is_connected():
            await vc.move_to(channel)
            return vc
    return await client.join_voice_channel(channel)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.send_message(client.get_channel(variables["generalChannelID"]), "hi guys, bot up and running")

@client.event
async def on_message(message):
    global vc
    content = message.content.strip()
    if any([content.startswith(command) for command in commands]):
        for command in commands:
            if content.startswith(command):
                await client.send_message(message.channel, commands[command])
    elif content.startswith("!resetLocal"):
        initLocal()
        await client.send_message(message.channel, "Environment reset")
    elif content.startswith("!sb"):
        content = content.strip("!sb ")
        author = message.author
        channel = author.voice_channel
        vc = await moveToChannel(channel)
        player = vc.create_ffmpeg_player("audio/flokkie_Twee men.ogg")
        player.start()

    elif content.startswith("!yt"):
        content = content.strip("!yt").strip()
        if content == "":
            await client.send_message(message.channel, "Include a link to play audio from YouTube")
        else:
            youtubePrefix = "https://www.youtube.com/watch?v="
            if content == "developers" or content == "devs":
                link = youtubePrefix + "KMU0tzLwhbE"
                await client.send_message(message.channel, link)
            elif content.startswith("https://www.youtube.com/watch?v="):
                link = content
            else:
                link = youtubePrefix + "MtN1YnoL46Q"
                await client.send_message(message.channel, link)
            author = message.author
            channel = author.voice_channel

            vc = await moveToChannel(channel)
            player = await vc.create_ytdl_player(link)
            player.start()

initLocal()

client.run(variables["botToken"])

client.close()
