from datetime import datetime
from turtle import title
import discord
import requests
import typer
from config import NASA_API

async def main(message, client):

    messageCont = message.content
    messageCont = messageCont[1:]
    messageCont = messageCont.lower()

    NASAchecker = messageCont.split()

    #Check what Command Was..
    if messageCont == "hello":
        await message.channel.send(f"Hello to you @{message.author}!")
    if messageCont == "ping":
        await message.channel.send(f"Hello to you @{message.author}!")
    if messageCont == "help":
        await displayHelp(message, client)


    #NASA
    NASAlen = len(NASAchecker)
    if  NASAlen >= 2:
        #APOD
        if NASAchecker[0] == "nasa" and NASAchecker[1].lower() == "apod":
            if NASAlen == 3:
                await nasaImage("https://api.nasa.gov/planetary/apod", "Astronomy Picture of the Day", str(NASAchecker[2]), message, "Error sending request, please check date or try again later")
            elif NASAlen == 2:
                await nasaImage("https://api.nasa.gov/planetary/apod", "Astronomy Picture of the Day", await currentDate(), message, "Error sending request, please check date or try again later")
            else:
                await message.channel.send(f"Oh No! Invalid input <@{message.author.id}>! Try Again Maybe?")
        
        #NEXT THING


        # r = requests.get("?api_key=zodmkbogyvfaBQoeC0UHSw3bffJXuz61JqiUyCrw&date=2022-04-29")
        # r.raise_for_status()
        # data = r.json()
        # URL = data['url']
        # title = data['title']

        # embed = discord.Embed(title=title, description="Desc", color=0x00ff00) #creates embed
        # embed.set_image(url=URL)

        # await message.channel.send(embed=embed)


#NASA FUNCTIONS
async def nasaImage(url, title, date, message, error):
    try:
        nasaURL = f"{url}?api_key={NASA_API}&date={date}"
        response = requests.get(url=nasaURL)

        data = response.json()

        imgURL = data['url']

        try:
            imgURL = data['hdurl']
        except:
            print()

        imgTitle = data['title']

        imgEmbed = discord.Embed(title=f"{title}\n{imgTitle}", description=f"Image Taken on {date}.\n<@{message.author.id}>", color=0x0abccc)
        imgEmbed.set_image(url=imgURL)

        await message.channel.send(embed=imgEmbed)
    except:
        await message.channel.send(f"{error}")

async def currentDate():
    date = datetime.today().strftime('%Y-%m-%d')

    return str(date)


#HELP FUNCTIONS
async def displayHelp(message, client):
    self = client.get_user(client.user.id)


    helpEmbed = discord.Embed(title="Help - List of Commands", description=f"<@{message.author.id}>", color=0x0abccc)
    helpEmbed.set_author(name=f"NickBot Help", icon_url=self.avatar_url)

    helpEmbed.add_field(name = "**NASA**", value="""
    -> _APOD_ - Astronomy Picture of the Day for current or given date.
    --> e.g. `!NASA APOD` or `!NASA APOD 1998-12-14`\n
    """, inline = False)

    await message.channel.send(embed=helpEmbed)


#msg: "Date must be between Jun 16, 1995 and Apr 30, 2022.",
    #OLD AND POTENTIALY USEFUL STUFF!
    # imageres = requests.get(url)
    # image = Image.open(BytesIO(imageres.content))

    # DIR = Path() / 'images'
    # image_name = f"{title}.{image.format}"
    
    # if not DIR.exists():
    #     os.mkdir(DIR)
    # image.save(DIR / image_name, image.format)

    #await message.channel.send(file=discord.File(DIR / image_name))


    # await message.channel.send(f"Hello to you {message.author}!")
    # await message.author.send("I Can Smell You...")


    #zodmkbogyvfaBQoeC0UHSw3bffJXuz61JqiUyCrw

    #https://api.nasa.gov/planetary/apod?api_key=zodmkbogyvfaBQoeC0UHSw3bffJXuz61JqiUyCrw