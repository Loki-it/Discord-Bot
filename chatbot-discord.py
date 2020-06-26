import discord
import random

TOKEN = '' # Inserire il tuo Token
client = discord.Client() # Definizione del bot

# Avvio
@client.event
async def on_ready():
    print('Il bot è online :D')
    print(client.user.name)
    print(client.user.id)
    print('__________________')
    # Imposta uno stato custom
    game = discord.Game("Chattare con te")
    await client.change_presence(status=discord.Status.online, activity=game)

# Chatbot
@client.event
async def on_message(message):
    # Evita che il bot parla da solo
    if message.author == client.user:
        return
    # Messaggio standard
    if message.content.find("ciao") != -1:
        await message.channel.send("Ciao!")
    # Messaggio con risposte multiple casuali
    if message.content.find("salve") != -1:
        await message.channel.send(random.choice(("Ciao!","Salve!","Eila!","Hey")))
    # Stoppa il bot in caso di emergenza
    if message.content == 'stop': await client.logout() # STOPPA IL BOT

# Start del bot
client.run(TOKEN)

# ------------------------------------



