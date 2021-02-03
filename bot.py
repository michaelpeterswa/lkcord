# michaelpeterwswa
# bot.py

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import toml
from discord import Embed, Game, Status
from discord.ext import commands

secrets = toml.load("./secrets.toml")
bot = commands.Bot(command_prefix=".", description="letterkenny")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.change_presence(
        activity=Game(name="fuck you shoresy | .lk"), status=Status.dnd
    )

@bot.command(pass_context=True)
async def beep(ctx):
  await ctx.message.channel.send("boop ✅")

@bot.command(pass_context=True)
async def lk(ctx):
  resp = get_quote()
  await ctx.message.channel.send(resp["quote"])

def get_quote():
  url = 'https://cascades.dev/api'

  try:
    response = requests.get(url)
    data = json.loads(response.text)
    return data
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
    return -1

if __name__ == '__main__':
  bot.run(secrets["disc"])
  
  