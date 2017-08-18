This is a simple Discord chat bot that me and my friends use on our Discord server.

## Set up

You will need to create a Discord application and a bot account at https://discordapp.com/developers/applications/me

Adding a bot to a server (of which you are an admin) can be done here https://discordapp.com/oauth2/authorize?client_id=BOTID&scope=bot&permissions=0

Where BOTID is the ID of the newly created bot.

Additionally you will need to install the Discord API Python wrapper. This can be done via pip using the following command ```python3 -m pip install -U discord.py```

### Configuration

There isn't much that needs to be done to get this bot up and running. The most important part is the variable file. There is an example file in the repository called ```example.conf``` copy this file and rename it to ```vars.conf``` and replace the placeholders by your variables.

After all the above steps have been completed run ```python3 bot.py``` and the bot should be working.

## Contribution

Feel free to contribute by forking the repository and making a pull request.

Any issues or suggestions can be added as an issue and I will take a look at it :)
