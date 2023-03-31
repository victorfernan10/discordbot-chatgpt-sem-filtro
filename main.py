import discord
from discord.ext import commands
import requests


key = ""


TOKEN = ''

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print(f'Online')

@client.command()
async def gpt(ctx, *,pergunta):
    url = "https://api.openai.com/v1/completions"
    
    pergunta1 = pergunta.replace('"',"")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    data = {
        "model": "text-davinci-003",
        "prompt": f"{pergunta1}",
        "max_tokens": 4000,
        "temperature": 1.0,
    }

    req = requests.post(url, headers=headers, json=data)
    resposta = req.json()

    if "choices" in resposta:
        autor = ctx.author.mention
        responder = (resposta["choices"][0]["text"].lstrip())  
        await ctx.send(f'> {autor}\n> Pergunta: {pergunta}\n\n{responder}')


client.run(TOKEN)