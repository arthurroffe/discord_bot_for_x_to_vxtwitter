import discord as di
import re

intents = di.Intents.default()
intents.message_content = True
bot = di.Client(intents=intents)

@bot.event
async def on_ready():
    print('Now Role :', bot.user)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    new_message = str(message.content)
    if re.match("https://x.com",new_message):
        replace_message = new_message.replace("https://x.com","https://vxtwitter.com")
        await message.channel.send(replace_message)
        

token = "YOUR_BOT_TOKEN_HERE"

bot.run(token)