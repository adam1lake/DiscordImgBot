# DiscordImgBot
Bot to retrieve images from Google Images using discord commands.

### Quick setup:
Discord Bot set -up:
Follow this tutorial up until writing code in order to set up an application and a bot in your server.
https://realpython.com/how-to-make-a-discord-bot-python/.  
Once complete, ensure that your bot has the correct permissions in your server/channel.


In the .env file:
1. Enter the Channel ID you want to use the bot in. You can get this by right-clicking on the channel in Discord and clicking "Copy ID".
2. Enter the token for the bot. This can be obtained from the Bot page on the Discord API Console (https://discord.com/developers/).
3. Choose your command prefix. The default is "$".

To run the bot:
1. Install the correct version of ChromeDriver for your Chrome browser (https://chromedriver.chromium.org/downloads). Place this in the root of this repository.
2. Ensure Python 3 is installed (https://wiki.python.org/moin/BeginnersGuide/Download)
3. Verify the installation using the command "python --version", ensuring it returns the correct Python version.
4. Install the requirements using the command "python -m pip install -r requirements.txt".
5. Run main.py using the command "python src/main.py".

The commands (using the prefix you specify in .env instead of "$"):
- $image querystring
   - Returns the first result from Google Images
- $random querystring
   - Returns a random result from the first 50 results from Google Images
  
