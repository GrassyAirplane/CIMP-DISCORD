import discord
from discord import guild

TOKEN = ""
client = discord.Client()

MESSAGE_ID = 800299541576155146

@client.event
async def on_ready():
    print("Logged In")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id ==guild_id, client.guilds)

        if payload.emoji.name == "FUNCTIONS":
            role = discord.utils.get(guild.roles, name = "FUNCTIONS")
        elif payload.emoji.name == "COMPUTER":
            role = discord.utils.get(guild.roles, name = "COMPUTERSCIENCE")
        elif payload.emoji.name == "CALCULUS":
            role = discord.utils.get(guild.roles, name = "CALCULUS")  
        elif payload.emoji.name == "PHYSICS":
            role = discord.utils.get(guild.roles, name = "PHYSICS")
        elif payload.emoji.name == "DATA":
            role = discord.utils.get(guild.roles, name = "DATAMANAGEMENT")
        elif payload.emoji.name == "ENGLISH":
            role = discord.utils.get(guild.roles, name = "ENGLISH")
        elif payload.emoji.name == "STOCK":
            role = discord.utils.get(guild.roles, name = "STOCK")
        elif payload.emoji.name == "CHEMISTRY":
            role = discord.utils.get(guild.roles, name = "CHEMISTRY")
        elif payload.emoji.name == "BIOLOGY":
            role = discord.utils.get(guild.roles, name = "BIOLOGY")
        elif payload.emoji.name == "CIMP":
            role = discord.utils.get(guild.roles, name = "CIMP STUDENT")
        elif payload.emoji.name == "KINESIOLOGY":
            role = discord.utils.get(guild.roles, name = "KINESIOLOGY")
        elif payload.emoji.name == "GAMINGANIMEETC":
            role = discord.utils.get(guild.roles, name = "GAMING")    
        elif payload.emoji.name == "FAMILIES":
            role = discord.utils.get(guild.roles, name = "FAMILIES")    
        else:
            role = discord.utils.get(guild.roles, name =payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Done")
            else:
                print("Member not found.")
        else:
            print("Role not found, or already")        



client.run(TOKEN)


