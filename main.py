import discord

#Custom PY Files
import functions
import config

from discord.ext import commands

client = commands.Bot(command_prefix="!", case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name = "Thinking of Space"))


@client.event
async def on_message(message):
    if message.author == client.user:       #Checks to See if itself sent the message
        return

    if  message.content[0] != '!':          #Checks to see if its a command
        return

    await functions.main(message, client)
    await client.process_commands(message)


@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def APOD(ctx, *arg):
    url = "https://api.nasa.gov/planetary/apod"
    title = "Astronomy Picture of the Day"
    error = "Error, make sure date is correct format. Date must be between Jun 16, 1995 and Apr 30, 2022"

    if len(arg) == 0:
        await functions.nasaImage(url, title, await functions.currentDate(), ctx, error)
    elif len(arg) == 1:
        try:
            split = arg[0].split(".")
            reorder = f"{split[2]}-{split[1]}-{split[0]}"
            await functions.nasaImage(url, title, reorder, ctx, error)
        except:
            await ctx.send("Invalid Input. You sure you entered this correct?")
    else:
        await ctx.send("Invalid Input. You sure you entered this correct?")



client.run(config.DISCORD_TOKEN)