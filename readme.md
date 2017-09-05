This is a simple Discord chat bot that me and my friends use on our Discord server.

## Set up

You will need to create a Discord application and a bot account at https://discordapp.com/developers/applications/me

Adding a bot to a server (of which you are an admin) can be done here https://discordapp.com/oauth2/authorize?client_id=BOTID&scope=bot&permissions=0

Where BOTID is the ID of the newly created bot.

This project requires you to install Python and libffi which can be done with apt-get ```sudo apt-get install python3-dev libffi-dev```

Additionally you will need to install the Discord API Python wrapper, youtube_dl and PyNaCl. This can be done via pip using the following command ```python3 -m pip install -U discord.py[voice] PyNaCl youtube_dl```

### Configuration

There isn't much that needs to be done to get this bot up and running. The most important part is the variable file. There is an example file in the repository called ```example.conf``` copy this file and rename it to ```vars.conf``` and replace the placeholders by your variables.

After all the above steps have been completed run ```python3 bot.py``` and the bot should be working.

## The goal

There isn't much of a goal apart from having a practical, working, discord bot. I'd like to implement the audio from my [soundboard app](https://github.com/yarwest/SoundBoard). I might think up more (complex) functionality that would be a nice stretch goal. Feel free to leave suggestions as issues.

## Licensing

The project is licensed under the MIT license which can be found in the LICENSE file.

## Contribution

Feel free to contribute by forking the repository and making a pull request.

Any issues or suggestions can be added as an issue and I will take a look at it :)

### Disclaimer

You will need to host the bot yourself, this repository only provides the code (which is subject to change and faults). For more information I can be reached at yarnoboelens@gmail.com
