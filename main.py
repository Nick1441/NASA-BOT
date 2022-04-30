import os
import discord
#Import Custom Classes
import commands
import config

token = config.DISCORD_TOKEN
client = discord.Client()

def checkMessage(message):
    return False



#On Start Commands!2
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_message(message):
    if message.author == client.user:       #Checks to See if itself sent the message
        return

    if  message.content[0] != '!':          #Checks to see if its a command

        
        return

    await commands.main(message, client)





@client.event
async def on_voice_state_update(member, before, after):
    VCID = discord.utils.get(client.get_all_channels(), name="CREATE ROOM")
    vc = client.get_channel(id=VCID.id)

    if vc.members:
        channel = client.get_channel(969736299974127668)
        await channel.send("THIS WORKS?")
        return



client.run(token)