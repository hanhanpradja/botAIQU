import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url 
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')

            nama, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')

            # Inferensi
            if nama == 'Merpati\n' and skor >= 0.65:
                await ctx.send('Ini adalah burung merpati')
                await ctx.send('makanan dari burung ini adalah kecambah')
                await ctx.send('habitatnya sangat mudah ditemukan')
            elif nama == 'Pipit\n' and skor >= 0.65:
                await ctx.send('Ini adalah burung pipit')
                await ctx.send('makanan dari burung ini adalah kecambah')
                await ctx.send('habitatnya sangat mudah ditemukan')
            else:
                await ctx.send("GAMBAR YANG DIKIRIM TIDAK DIKENALI")
    else:
        await ctx.send("TIDAK ADA FILE YANG DIKIRIMKAN")

bot.run('FILL WITH YOUR OWN TOKEN')
