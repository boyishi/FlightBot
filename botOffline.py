# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 03:30:25 2020

@author: Tyler Pomberg
"""

import os
import random
import asyncio
from dotenv import load_dotenv
import discord
from discord.utils import get
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='#')
# client = discord.client()

def string1(arg):
    switcher = {
        0: "||       secret message      ||",
        1: "||        hey       ||",
        2: "||    Rot13.unfugntvzntr     ||"
        }
    return switcher.get(arg, "nothing")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='leader1', hidden=True)
async def leader1(ctx):
    await ctx.message.delete()
    print('Adding role Legendary to', ctx.message.author.name)
    member = ctx.message.author
    role = get(member.guild.roles, id=int(404103135615909888))
    print(role)
    message = 'Congrats, you completed the puzzle, but you werent the first so you dont get the prize, ' + member.name
    await ctx.author.send(message)
    # await member.add_roles(role)

@bot.command(name='join', help= 'Makes bot join the voice channel you are currently in')
async def join(ctx):
    await ctx.message.delete()
    channel = ctx.message.author.voice.channel
    # voice = get(bot.voice_clients, guild=ctx.guild)
    await channel.connect()
    print('1')
    await ctx.voice_client.disconnect()
    print('2')
    await channel.connect()
    print('3')
    print('bot joined channel')
    # voice.play(discord.FFmpegPCMAudio("Ethan.mp3"))
    # voice.source = discord.PCMVolumeTransformer(voice.source)
    # voice.source.volume = 0.07
    # print('playing audio file')

@bot.command(name='numb')
async def play(ctx):
    await ctx.message.delete()
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("numb.mp3"), after=lambda e: print('song finished'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.20
    print('playing audio file')

@bot.command(name='leave', help = 'Makes bot leave voice channel')
async def leave(ctx):
    await ctx.message.delete()
    await ctx.voice_client.disconnect()
    print('bot left the channel')

@bot.command(name='image', help = 'Testing response command', hidden=True)
async def image(ctx):
    await ctx.message.delete()
    print(ctx.message.author.name, ":")
    response = 'https://cdn.discordapp.com/attachments/634907622289571873/753377097413820486/Got_em.PNG'
    print('Image sent')
    await ctx.author.send(response)
    await ctx.author.send('message: dhsamhkqvedoz1')

@bot.command(name='roll_dice', help='Simulates rolling dice. Use #roll_dice(number of dice, number of sides)')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel', help='Creates new channel named after the input')
@commands.has_role('test')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print('Creating a new channel: ', channel_name)
        await guild.create_text_channel(channel_name)

@bot.command(name='secret', help='Testing private messaging. Try to find all the secrets')
async def secret(ctx):
    await ctx.message.delete()
    rand = random.randint(0, 2)
    num = 2
    secret1 = 'Secret Message: ' + string1(rand)
    print(ctx.message.author.name, ":")
    print(secret1)
    await ctx.author.send(secret1)
    
@bot.command(name='Rot13', help='Encrypts message using Rot13 cipher. Do not use spaces. Use only letters')
async def Rot13(ctx, message: str):
    await ctx.message.delete()
    print(ctx.message.author.name, ":")
    quote = message
    quote = quote.lower()
    quote = list(quote)
    count = 0
    for i in quote:
        quote[count] = ord(i)
        count = count + 1
    count = 0
    
    for i in quote:
        quote[count] = i + 13
        if quote[count] >= 123:
            quote[count] = quote[count] - 26
        #if quote[count] == 42 or quote[count] == 96 or quote[count] == 126 or quote[count] == 95:
        #    quote.insert(count, ord('\\'))
        count = count + 1
    count = 0
    
    for i in quote:
        quote[count] = chr(i)
        count = count + 1
    count = 0
    cipher = ''.join(quote)
    cipher = 'Encrypted Message: ' + cipher
    print(cipher)
    await ctx.author.send(cipher)
    
@bot.command(name='RKey', help='Encrypts message using running key cipher. Use only letters for both the key and the message')
async def RKey(ctx, key: str, message: str):
    await ctx.message.delete()
    print(ctx.message.author.name, ":")
    key = key.lower()
    message = message.lower()
    print(key, ':', message)
    key = list(key)
    message = list(message)
    count = 0
    for i in key:
        key[count] = ord(i) - 97
        count = count + 1
    count = 0
    for i in message:
        message[count] = ord(i)
        count = count + 1
    count = 0
    for i in message:
        if (message[count] >= 48 and message[count] <= 57):
            print(chr(i))
        else:
            message[count] = message[count] + key[count]
        if message[count] >= 123:
            message[count] = message[count] - 26
        count = count + 1
    count = 0
    for i in message:
        message[count] = chr(i)
        count = count + 1
    count = 0
    message = ''.join(message)
    message = 'Encrypted running key: ' + message
    print(message)
    await ctx.author.send(message)


@bot.command(name='Rot13Decipher', help= 'Deciphers code based upon Rot13 encryption. Use only letters')
async def decipher(ctx, message: str):
    await ctx.message.delete()
    print(ctx.message.author.name, ":")
    quote = message
    quote = quote.lower()
    quote = list(quote)
    count = 0
    for i in quote:
        quote[count] = ord(i)
        count = count + 1
    count = 0
    
    for i in quote:
        quote[count] = i - 13
        if quote[count] <= 96:
            quote[count] = quote[count] + 26
        count = count + 1
    count = 0
    
    for i in quote:
        quote[count] = chr(i)
        count = count + 1
    count = 0
    cipher = ''.join(quote)
    cipher = 'Decrypted Message: ' + cipher
    print(cipher)
    await ctx.author.send(cipher)

@bot.command(name='RKeyDecipher', help='Uses Running Key decryption in order to decipher the given key and message. Use spaces to seperate arguments, do not use spaces in arguments')
async def RKeyDecipher(ctx, key: str, message: str):
    await ctx.message.delete()
    print(ctx.message.author.name, ":")
    key = key.lower()
    message = message.lower()
    print(key, ':', message)
    key = list(key)
    message = list(message)
    count = 0
    for i in key:
        key[count] = ord(i) - 97
        count = count + 1
    count = 0
    for i in message:
        message[count] = ord(i)
        count = count + 1
    count = 0
    for i in message:
        if (message[count] >= 48 and message[count] <= 57):
            print(chr(i))
        else:
            message[count] = message[count] - key[count]
        if (message[count] <= 96 and message[count] >= 65):
            message[count] = message[count] + 26
        count = count + 1
    count = 0
    for i in message:
        message[count] = chr(i)
        count = count + 1
    count = 0
    message = ''.join(message)
    message = "Decrypted running key message: " + message
    print(message)
    await ctx.author.send(message)

@bot.event
async def on_voice_state_update(member, prev, cur):
    if member.id == 407011088438263819:
        # server = member.guild.voice_client
        # voice = get(bot.voice_clients, guild=404098740639498250)
        # print(voice)
        # if voice != None:
        #    await voice.disconnect()
        voice = await member.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('numb.mp3'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.25
        print('audio playing')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)