from Ellie import Say, get_reply
import discord
from discord import *

TOKEN = 'NzA2NTE5NTg4Nzc0NjA4OTQ4.Xq744g.jxi3nEhTLvZiguJ22jUNudGs2J8'
client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('>'):
		Say(message.content.replace(">", "").lower())
		msg = get_reply()
		await message.channel.send(msg)
	
	if message.content.find("lol") != -1:
		await message.channel.send(":joy:")

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')	

client.run(TOKEN)

