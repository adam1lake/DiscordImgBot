import discord
from imagegetter import ImageGetter
from discord.ext import commands
from sys import exit
import os
from dotenv import load_dotenv


class IpDiscordBot:
    # Initialises the Discord API and the imagegetter
    def __init__(self, token, prefix):
        self.token = token
        self.client = discord.Client()
        # Command prefix can be changed here
        self.client = commands.Bot(command_prefix=prefix)
        self.ig = ImageGetter()

    def start(self):
        # Handles invalid commands
        @self.client.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                await ctx.send("Invalid command.")

        # Executes when the bot starts and is online on Discord
        @self.client.event
        async def on_ready():
            channel = self.client.get_channel(int(os.getenv("DISCORD_CHANNEL_ID")))
            await channel.send("ImageBot is running!")
            print("ImageBot is activated.")

        # Gets the first image, sends the image or an error message
        @self.client.command()
        async def image(ctx, *args):
            query = " ".join(args[:])
            if query == "":
                await ctx.send("Error: No parameters given.")
            print(f"Searching for first image with query: {query}...")
            result = self.ig.get_image(query)
            if result:
                await ctx.send(file=discord.File("current_image.png"))
            elif result == "NoResults":
                await ctx.send("Error: Unexpected result.")
            elif result == "Error":
                await ctx.send("Internal Error.")

        # Gets a random image, sends the image or an error message
        @self.client.command()
        async def random(ctx, *args):
            query = " ".join(args[:])
            if query == "":
                await ctx.send("Error: No parameters given.")
            print(f"Searching for random image with query: {query}...")
            result = self.ig.get_image(query, True)

            if result == "NoResults":
                await ctx.send("Error: No results found.")
            elif result == "Error":
                await ctx.send("Error: Complain at chub because this shouldn't happen.")
            else:
                await ctx.send(file=discord.File("current_image.png"))

        # Handles errors with the image command
        @image.error
        async def info_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Error: Invalid arguments.")

        # Handles errors with the random command
        @random.error
        async def info_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Error: Invalid arguments.")

        # Starts the bot
        self.client.run(self.token)


if __name__ == "__main__":
    try:
        # Gets values from .env
        load_dotenv()
        TOKEN = os.getenv("DISCORD_BOT_TOKEN")
        PREFIX = os.getenv("DISCORD_COMMAND_PREFIX")

        bot = IpDiscordBot(TOKEN, PREFIX)
        bot.start()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
