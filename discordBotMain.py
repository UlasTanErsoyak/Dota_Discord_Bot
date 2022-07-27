import discord
from discord.ext import commands
import WebScraping

bot_token ="MTAwMTExNTY4ODU2NTQ4MTYxMg.GmaKBh._yUnorz0a5S1RQd2QYpJufGZB-0DHzy6CukZ0g"

bot_command = commands.Bot(command_prefix=".")

@bot_command.event
async def on_ready():
    print("Bot is ready to use.")

@bot_command.command(name="commands")
async def _command(context):
    await context.send("use **.price** to get information about a specific item(sadly i cant give information about item sets:<)\nuse **.clear <amount of lines(default 100)>** to clear chat\nuse **.eferin** to thank me for all my efforts\nuse **.benim_adam** to congratulate me ")

@bot_command.command(name="eferin")
async def _command(context):
    await context.send("**tsk cnm**")

@bot_command.command(name="benim_adam")
async def _command(context):
    await context.send("**damlamayi surdur benim g**")

@bot_command.command(name="occ")
async def _command(context):
    await context.send("*n€ di$€n mQQQQQ* :drooling_face:")

@bot_command.command(name="kafi")
async def _command(context):
    await context.send("**bb**:lying_face:")
    await bot_command.logout()

@bot_command.command()
async def clear(context,amount=100):
    await context.channel.purge(limit=amount)
    

@bot_command.command(name="price")
async def _command(context):
    await context.send("provide an item name")
    def isAnswerValid(answer):
        return(answer.author==context.author and answer.channel==context.channel)
    
    message = await bot_command.wait_for("message",check=isAnswerValid)
    try:
        all_data=[]
        all_data=WebScraping.itemInfo(message.content)
        all_data.append(WebScraping.steamxCutCalculator(all_data[6],all_data[5]))
        await context.send(f"""hero's name:{all_data[0]}\nitem's name: {all_data[8]}\nitem's slot: {all_data[1]}\nitem's rarity: {all_data[2]}\nitem's market price(with steam tax): {all_data[6]}\nitem's market price(without steam tax): {all_data[5]}\nsteam's tax cut: {all_data[9]}\nquantity in steam market: {all_data[4]}\nsteam market link: {all_data[7]}""")
        print(all_data)
    except:
        await context.send("something went wrong.oops.")

bot_command.run(bot_token)