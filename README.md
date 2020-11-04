# DiscordImgBot
Bot to retrieve images from Google Images using discord commands.

### Quick setup:
Discord Bot set-up:
Follow this tutorial up until writing code in order to set up an application and a bot in your server.
https://realpython.com/how-to-make-a-discord-bot-python/


In the .env file:
1. Enter the Channel ID you want to use the bot in. You can get this by right-clicking on the channel in Discord and clicking "Copy ID".
2. Enter the token for the bot. This can be obtained from the Bot page on the Discord API Console (https://discord.com/developers/).
3. Choose your command prefix. The default is "$".
Ensure that your bot has the correct permissions in your server/channel, and run main.py

Using the bot:
The commands:
- $image <query>
  Returns the first result from Google Images
- $random <query>
  Returns a random result from the first 50 results from Google Images
  

