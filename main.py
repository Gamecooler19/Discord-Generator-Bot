from webserver import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
import os
import discord, json
import random, string, os
import time, datetime
from discord.ext import commands
from discord import Embed, File


def gennitro(number):
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0'
    ]
    return "".join(random.choices(chars, k=16))

def NitroBox(number):
    code1 = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    return f'https://discord.com/billing/promotions/xbox-game-pass/redeem/{code1}'


bot = commands.Bot(command_prefix='.')
bot.remove_command('help')
link = "discord.gift/"

@bot.event
async def on_ready():
    print("Im alive :D")
    print(f"Prefix: .")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Rewards Generator Help",description="""**My prefix:** `.`
    
    📝 **Help Menu**
    `.help`
    
    **Unchecked Codes Generator**
     `.nitro (1 to 100)`      `.xbox (1 to 100)`

    **General Commands**
    `.stock`  `.gen (sfa , nfa , mfa or steam)`

    **Admin Commands**
    `.nfaadd` `.sfaadd` `.mfaadd`  `.steamadd`

   **Our Bot Developers**
    `.botinfo`

    [Get Support](https://discord.gg/x-slayer-op)

     [Invite the bot here](https://discord.com/oauth2/authorize?client_id=924936306126106634&scope=bot%20applications.commands&permissions=8589934591)
                          """, color=0x3498db)
    embed.set_footer(text=f"Requested by {ctx.author} | Rewards Generator | {datetime.datetime.now().hour}:{datetime.datetime.now().minute}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.channel.send(embed=embed)

@bot.command()
async def nitro(ctx, number: int):
    x=0
    while x < number:
        await ctx.author.send(link + gennitro(number))
        x=x+1
    else:
        print(f"Generated {number} codes of Nitro for the user {ctx.author} in time {datetime.datetime.now()}")
        await ctx.send(f"I generated {number} of Nitro Unchecked codes for {ctx.author.mention}")
        return

@bot.command()
async def xbox(ctx, number: int):
    x=0
    while x < number:
        await ctx.author.send(NitroBox(number))
        x=x+1
    else:
        print(f"Generated {number} codes of Nitro Xbox for the user {ctx.author} in time {datetime.datetime.now()}")
        await ctx.send(f"I generated {number} of Nitro Xbox Unchecked codes for {ctx.author.mention}")
        
keep_alive()
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Minecraft", url="http://www.twitch.tv/Gamecooler19"))
    print('Logged in Bot')


@bot.command()
async def stock(ctx):
    stockmenu = discord.Embed(title="Account Stock",description="",color=0x3498db) 
    for filename in os.listdir("Accounts"):
        with open("Accounts/"+filename) as f: 
            ammount = len(f.read().splitlines()) 
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") 
            stockmenu.description += f"**{name}** - {ammount}\n" 
    await ctx.send(embed=stockmenu) 



@bot.command() 
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Specify the account you want!") 
    else:
        name = name.lower()+".txt" 
        if name not in os.listdir("Accounts"): 
            await ctx.send(f"Account does not exist. `stock`")
        else:
            with open("Accounts/"+name) as file:
                lines = file.read().splitlines() 
            if len(lines) == 0: 
                await ctx.send("These accounts are out of stock") 
            else:
                with open("Accounts/"+name) as file:
                    account = random.choice(lines) 
                try: 
                    await ctx.author.send(f"`{str(account)}`\n\nThis message will delete in 3 minutes!", delete_after=180.0)
                except: 
                    await ctx.send("Failed to send! Turn on ur direct messages")
                else: 
                    await ctx.send("Sent the account to your inbox!")
                    with open("Accounts/"+name,"w") as file:
                        file.write("") 
                    with open("Accounts/"+name,"a") as file:
                        for line in lines: 
                            if line != account: 
                                file.write(line+"\n") 

@bot.command()
@commands.has_permissions(administrator=True)
async def sfaadd(ctx, account=None):
    if account is None:
        embed = discord.Embed(title=f"The command is: ```Add (Any) Accounts [Account]```", colour=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        with open("Accounts/sfa.txt", "a") as file:
            file.write(account + "\n")
            await ctx.send("Done")
            print(f"One accounts was puted in the Generator")

@sfaadd.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@bot.command()
@commands.has_permissions(administrator=True)
async def nfaadd(ctx, account=None):
    if account is None:
        embed = discord.Embed(title=f"The command is: ```Add (Any) Accounts [Account]```", colour=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        with open("Accounts/nfa.txt", "a") as file:
            file.write(account + "\n")
            await ctx.send("Done")
            print(f"One accounts was puted in the Generator")

@nfaadd.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@bot.command()
@commands.has_permissions(administrator=True)
async def mfaadd(ctx, account=None):
    if account is None:
        embed = discord.Embed(title=f"The command is: ```Add (Any) Accounts [Account]```", colour=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        with open("Accounts/mfa.txt", "a") as file:
            file.write(account + "\n")
            await ctx.send("Done")
            print(f"One accounts was puted in the Generator")

@mfaadd.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@bot.command()
@commands.has_permissions(administrator=True)
async def steamadd(ctx, account=None):
    if account is None:
        embed = discord.Embed(title=f"The command is: ```Add (Any) Accounts [Account]```", colour=0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        with open("Accounts/steam.txt", "a") as file:
            file.write(account + "\n")
            await ctx.send("Done")
            print(f"One accounts was puted in the Generator")

@steamadd.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@bot.command()
async def botinfo(ctx):
    members = 0
    for guild in bot.guilds:
      members += guild.member_count
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name="**Version**",value="1.0.0")
    embed.add_field(name="**Users**",value=members)
    embed.add_field(name="**Servers**",value=str(len(bot.guilds)))
    embed.add_field(name="**Discord.py Version**",value="1.7. 2")
    embed.add_field(name="**Developers**",value="""**Gamecooler19#3016**""",inline=False)
    embed.add_field(name="\u200b",value="[Join my support server](https://discord.gg/x-slayer-op) • [Invite me](https://discord.com/oauth2/authorize?client_id=924936306126106634&scope=bot%20applications.commands&permissions=8589934591)")
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"Bot | {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://cdn.discordapp.com/attachments/927073213794627623/927229934508834816/canopus_image.jpg")
    await ctx.channel.send(embed=embed)

bot.run("TOKEN")
