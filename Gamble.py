import discord, os, sqlite3, random, operator, time, Estrapy, requests, json, string
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import find
from bs4 import BeautifulSoup
#os.system('cls')
os.system('clear')

bot = commands.Bot(command_prefix='%', case_sensitive=False,intents = discord.Intents.all())
bot.remove_command('help')
hot = 'https://cdn.discordapp.com/attachments/914279612568178689/1027654027644784691/unknown.png'
random_things = ['moon knight', 'moon knight fanart',  'bob ross', 'hot lopunny', 'hot markiplier', 'random pokemon', 'pokemon', 'hot pokemon', 'goofy snapchat memes', 'pp', 'me irl', 'ivy x layten', 'hot femboy hooters', 'hot anime women in thigh highs', 'dank memes', 'isab x sauda', 'hot roblox', 'oh my hot roblox', '老干妈', 'funny twitter posts', 'sus minecraft', 'amongus minecraft', 'hot minecraft pics', 'hot belle delphine', 'belle delphine', 'hooters gone wrong', 'femboy hooters','heisenberg', 'heisenburger', 'isab', 'ludwig', 'cute cat', 'crazy rich asians', 'cute dog', 'hot anime girls', 'hot anime guys', 'hot genshin pics', 'amongus', 'fortnite', 'breaking bad', 'walter white', 'jesse pinkman', 'valorant', 'hot valorant pics', 'gay men kissing', 'hot valorant mommy', 'hot valorant men', 'hot valorant mommy', 'hot valorant daddy', 'handsome jschlatt', 'handsome jerma', 'smallant1', 'celeste fanart', 'hot bloons td6', 'hot league of legends', 'league of legends', 'terraria fanart', 'slime rancher fanart', 'amongus', 'fortnite', 'hot amongus', 'plants vs zombies fanart', 'my singing monsters fanart', 'hot fortnite', 'tf2 fanart', 'hot tf2', 'stumble guys', 'hot stumble guys', 'cuphead fanart', 'stardew valley fanart', 'hot stardew valley', 'tenz and kyedae', 'hot minecraft', 'minecraft fanart', 'hot spongebob', 'spongebob fanart', 'jschlatt gun', 'hot sans', 'femboy jimmyhere', 'hot jimmyhere', 'jimmyhere', 'moai', 'giga chad', 'penguinz0', 'hot penguinz0', 'xqc', 'hot xqc', 'waluigi', 'hot waluigi', 'big dumpy', 'hot viper mommy', 'hot sage mommy', 'hot brimstone daddy', 'frankie dumpy', 'clown', 'nerd emoji', 'TryingToBeHooman', 'csgo', 'amongus balls', 'stray', 'stray fanart', 'gta5', 'hot gta5', 'caramilk', 'hot dog', 'glizzy', 'hot glizzy', 'michael reeves', 'michael reeves x lilypichu', 'amouranth', 'pokimane', 'legend of zelda fanart', 'hot legend of zelda', 'mario', 'hot mario', 'splatoon', 'hot splatoon', 'splatoon fanart', 'cyberpunk 2077', 'hot cyberpunk 2077', 'hot ludwig', 'hot femboys', 'femboys', 'wawa cat']
walter = ''
jesse = ''
deck = []
roles = []
quotes = []
quotees = []
submitters = []
#https://discord.com/api/oauth2/authorize?client_id=1030540712665686087&permissions=8&scope=bot

thingies = [':eggplant:', ':peach:', ':sweat_drops:', ':nerd:', ':clown:', ':moyai:']
cool_money_get = 0

def count_pp(thing, list):
    return int(list.count(thing))

def get_roll():
    global rolls

    if random.randint(0,100) < 10:
        rolls.append(thingies[0])
    elif random.randint(0,100) < 1:
        rolls.append(thingies[5])
    elif random.randint(0,100) < 5:
        rolls.append(thingies[4])
    elif random.randint(0,100) < 20:
        rolls.append(thingies[1])
    elif random.randint(0,100) < 20:
        rolls.append(thingies[2])
    elif random.randint(0,100) < 1:
        rolls.append(thingies[3])
    else:
        pass

def gen_screenshot():
    link = 'https://prnt.sc/'
    for i in range(2):
        link += random.choice(string.ascii_lowercase)
    for i in range(4):
        link += random.choice(string.digits)
    return link

def random_image():
    global walter, jesse, random_things

    base_link = 'https://www.google.com/search?q={}&sxsrf=ALiCzsYzF5WB09ckxP22Bo7gG-cFfJ2R_Q:1665095701648&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj75sDu1Mz6AhXUIH0KHQUPAMAQ_AUoAnoECAIQBA&biw=1879&bih=931&dpr=1'
    pp = random.choice(random_things)
    amongus = base_link.format(pp)
    amongus_sus = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r = requests.get(amongus, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    joe = True
    i = 0

    while joe == True:
        try:
            images = soup.findAll('img')[i]
            src = images['src']
            i += 1

            if 'https://' in src:
                amongus_sus.append(src)
            else:
                pass
        except IndexError:
            joe=False
            break

    walter = random.choice(amongus_sus)
    jesse = pp

def random_image_custom(phrase):
    global walter, jesse, random_things

    base_link = 'https://www.google.com/search?q={}&sxsrf=ALiCzsYzF5WB09ckxP22Bo7gG-cFfJ2R_Q:1665095701648&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj75sDu1Mz6AhXUIH0KHQUPAMAQ_AUoAnoECAIQBA&biw=1879&bih=931&dpr=1'
    pp = phrase
    amongus = base_link.format(pp)
    amongus_sus = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r = requests.get(amongus, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    joe = True
    i = 0

    while joe == True:
        try:
            images = soup.findAll('img')[i]
            src = images['src']
            i += 1

            if 'https://' in src:
                amongus_sus.append(src)
            else:
                pass
        except IndexError:
            joe=False
            break

    walter = random.choice(amongus_sus)
    jesse = pp

def joe(user, monies, name):
    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    pp = f"INSERT INTO JOE(USER, MONIES, NAME) VALUES({user},{monies}, '{name}')"

    cur.execute(pp)
    conn.commit()

def joe_quote(quote, quotee, submitter):
    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    pp = f'INSERT INTO QUOTES(QUOTE, QUOTEE, SUBMITTER) VALUES("{quote}","{quotee}", "{submitter}")'

    cur.execute(pp)
    conn.commit()

def get_quote():
    global quotes, quotees, submitters, joeee, joeeee, joeeeee

    quotes = []
    quotees = []
    submitters = []

    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM QUOTES')
    rows = cur.fetchall()

    for row in rows:
        quote = row[0]
        quotee = row[1]
        submitter = row[2]
        quotes.append(quote)
        quotees.append(quotee)
        submitters.append(submitter)
    
    pp = random.randint(0, len(quotes))

    joeee = quotes[pp]
    joeeee = quotees[pp]
    joeeeee = submitters[pp]

def mama(user, name):
    name = name.split('#')[0]
    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM JOE')
    rows = cur.fetchall()
    pp = [x[0] for x in rows]

    if user in pp:
        return True
    else:
        joe(user, 500, name)

    conn.close()

def get_monies(user):
    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM JOE')
    rows = cur.fetchall()

    for row in rows:
        user_id = row[0]
        user_balance = row[1]
        name = row[2]
        
        try:
            if str(user_id) == str(user):
                return user_balance
        except:
            pass
        
    return 'Cant Find Value'

def get_leaderboard():
    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM JOE')
    rows = cur.fetchall()
    joe_mama = {}
    pp = [x[1] for x in rows]
    pp2 = [x[2] for x in rows]

    if len(pp2) >= 5:
        for i in range(0, 5):
            joe_mama.update({pp2[i]: pp[i]})
    else:
        for i in range(len(pp2)):
            joe_mama.update({pp2[i]: pp[i]})

    joe_mama = sorted(joe_mama.items(), key=operator.itemgetter(1), reverse=True)
    joe_mama = dict(joe_mama)
    return joe_mama

def monies_operation(user, amount, operator):
    conn = sqlite3.connect('Joe.db')
    cur = conn.cursor()

    if operator == '-':
        update = f'''UPDATE JOE SET MONIES = {get_monies(user) - int(amount)} WHERE USER = {user}'''
    elif operator == '+':
        update = f'''UPDATE JOE SET MONIES = {get_monies(user) + int(amount)} WHERE USER = {user}'''
    else:
        print('Something Went Wrong Monies Operation')

    cur.execute(update)
    conn.commit()

    conn.close()

@bot.event
async def on_ready():
    #os.system('cls') windows clear function
    os.system('clear') #linux clear function just comment it out if you dont wanna use it
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'Gamble Is On {len(bot.guilds)} Servers!'))

@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        join_embed = discord.Embed(title='Thank You For Adding Gamble', description='The prefix is %\nUse %commands to list all the commands. If you need help with any command, just use %help {command name}\n\nPlease, [share](https://discord.com/api/oauth2/authorize?client_id=1030540712665686087&permissions=8&scope=bot) the bot with all your friends.\nIf you have any issues or bugs, report them on my [github](https://github.com/tryingtobehooman/gamble/issues) for a cool reward.\nIf you really like the bot, please consider supporting me on [patreon](https://www.patreon.com/tryingtobehooman/posts). You can suggest ideas and see whats going on behind the scenes.\nEnjoy!', color=discord.Color.from_rgb(1, 168, 221))
        await general.send(embed=join_embed)

@bot.group(invoke_without_command=True, aliases=['Help'])
async def help(ctx):
    random_image()

    help_embed = discord.Embed(title='Need Help?', description='Run %Commands To Get A List of Commands\nUse %Help {Command} To Get Help With That Command', color=discord.Color.from_rgb(1, 168, 221))
    help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=help_embed)

@help.command(aliases=['Commands'])
async def commands(ctx):
    random_image()

    commands_help_embed = discord.Embed(title='Commands Command Syntax', description='Syntax: %Commands', color=discord.Color.from_rgb(1, 168, 221))
    commands_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    commands_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=commands_help_embed)

@help.command(aliases=['Ping'])
async def ping(ctx):
    random_image()

    ping_help_embed = discord.Embed(title='Ping Command Syntax', description='Syntax: %Ping', color=discord.Color.from_rgb(1, 168, 221))
    ping_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    ping_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=ping_help_embed)

@help.command(aliases=['Test'])
async def test(ctx):
    random_image()

    test_help_embed = discord.Embed(title='Test Command Syntax', description='Syntax: %Test', color=discord.Color.from_rgb(1, 168, 221))
    test_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    test_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=test_help_embed)

@help.command(aliases=['Bal'])
async def bal(ctx):
    random_image()

    bal_help_embed = discord.Embed(title='Bal Command Syntax', description='Syntax: %Bal\nSyntax: %Bal Check {@Someone You Wanna Check}\nSyntax: %Bal Send {Amount} {@Someone You Wanna Give Money To}', color=discord.Color.from_rgb(1, 168, 221))
    bal_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    bal_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=bal_help_embed)

@help.command(aliases=['Coin'])
async def coin(ctx):
    random_image()

    coin_help_embed = discord.Embed(title='Coin Command Syntax', description='Syntax: %Coin {Amount You Wanna Bet}', color=discord.Color.from_rgb(1, 168, 221))
    coin_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    coin_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=coin_help_embed)

@help.command(aliases=['Truth'])
async def truth(ctx):
    random_image()

    truth_help_embed = discord.Embed(title='Truth Command Syntax', description='Syntax: %Truth', color=discord.Color.from_rgb(1, 168, 221))
    truth_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    truth_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=truth_help_embed)

@help.command(aliases=['Dare'])
async def dare(ctx):
    random_image()

    dare_help_embed = discord.Embed(title='Dare Command Syntax', description='Syntax: %Dare', color=discord.Color.from_rgb(1, 168, 221))
    dare_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    dare_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=dare_help_embed)

@help.command(aliases=['Leaderboard'])
async def leaderboard(ctx):
    random_image()

    leaderboard_help_embed = discord.Embed(title='Leaderboard Command Syntax', description='Syntax: %Leaderboard', color=discord.Color.from_rgb(1, 168, 221))
    leaderboard_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    leaderboard_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=leaderboard_help_embed)

@help.command(aliases=['Nft'])
async def nft(ctx):
    random_image()

    nft_help_embed = discord.Embed(title='Nft Command Syntax', description='Syntax: %Nft', color=discord.Color.from_rgb(1, 168, 221))
    nft_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    nft_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=nft_help_embed)

@help.command(aliases=['Bored'])
async def bored(ctx):
    random_image()

    bored_help_embed = discord.Embed(title='Bored Command Syntax', description='Syntax: %Bored', color=discord.Color.from_rgb(1, 168, 221))
    bored_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    bored_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=bored_help_embed)

@help.command(aliases=['Image'])
async def image(ctx):
    random_image()

    image_help_embed = discord.Embed(title='Image Command Syntax', description='Syntax: %Image\nSyntax: %Image Get {Whatever You Want}', color=discord.Color.from_rgb(1, 168, 221))
    image_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    image_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=image_help_embed)

@help.command(aliases=['Slots'])
async def slots(ctx):
    random_image()

    slots_help_embed = discord.Embed(title='Slots Command Syntax', description='Syntax: %Slots', color=discord.Color.from_rgb(1, 168, 221))
    slots_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    slots_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=slots_help_embed)

@help.command(aliases=['Blackjack', 'blackjack', 'Bj'])
async def bj(ctx):
    random_image()

    bj_help_embed = discord.Embed(title='Bj Command Syntax', description='Syntax: %Bj', color=discord.Color.from_rgb(1, 168, 221))
    bj_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    bj_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=bj_help_embed)

@help.command(aliases=['Screenshot'])
async def screenshot(ctx):
    random_image()

    screenshot_help_embed = discord.Embed(title='Screenshot Command Syntax', description='Syntax: %Screenshot', color=discord.Color.from_rgb(1, 168, 221))
    screenshot_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    screenshot_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=screenshot_help_embed)

@help.command(aliases=['Batman'])
async def batman(ctx):
    random_image()

    batman_help_embed = discord.Embed(title='Batman Command Syntax', description='Syntax: %Batman', color=discord.Color.from_rgb(1, 168, 221))
    batman_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    batman_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=batman_help_embed)

@help.command(aliases=['Quote'])
async def quote(ctx):
    random_image()

    quote_help_embed = discord.Embed(title='Quote Command Syntax', description='Syntax: %Quote\nSyntax: Quote Add {Quote} {Person Who Said It}', color=discord.Color.from_rgb(1, 168, 221))
    quote_help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    quote_help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=quote_help_embed)

'''@help.command(aliases=[''])
async def (ctx):
    random_image()

    _help_embed = discord.Embed(title=' Command Syntax', description='Syntax: %', color=discord.Color.from_rgb(1, 168, 221))
    _help_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    _help_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=_help_embed)'''

@bot.command(aliases=['Commands'])
async def commands(ctx):
    def check(reaction, user):
        return user == ctx.author

    page1 = discord.Embed (
        title = 'List Of Commands Page 1/4',
        description = '%Help (Gives Help On A Command)\n%Commands (lists The Commands)\n%Ping (Pong)\n%Test (Test)\n%Bal (Check Your Balance)',
        colour = discord.Color.from_rgb(1, 168, 221)
    )
    page2 = discord.Embed (
        title = 'List Of Commands Page 2/4',
        description = '%Bal Check (Check Balance Of Another Person)\n%Bal Send (Sends Money To Person)\n%Coin (Bet On A Coin Flip)\n%Truth (No Need To Explain)\n%Dare (Also No Need To Explain)',
        colour = discord.Color.from_rgb(1, 168, 221)
    )
    page3 = discord.Embed (
        title = 'List Of Commands Page 3/4',
        description = '%Leaderboard (See Whos The Best)\n%Nft (Gives Random Bored Ape Nft)\n%Bored (Gives Random Activity To Do)\n%Image (Gives Random Image Based On A Phrase)\n%Slots (Slots Babee)',
        colour = discord.Color.from_rgb(1, 168, 221)
    )
    page4 = discord.Embed (
        title = 'List Of Commands Page 4/4',
        description='%Screenshot (Gives Random Screenshot)\n%Bj (Succy Succy)\n%Batman (???)\n%Quote (Gives Random Quote)\n%Quote Add (Add A Quote)',
        colour = discord.Color.from_rgb(1, 168, 221)
    )

    pages = [page1, page2, page3, page4]
    
    message = await ctx.send(embed=page1)
    await message.add_reaction('◀')
    await message.add_reaction('▶')

    i = 0
    reaction = None
    while True:
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 3:
                i += 1
                await message.edit(embed=pages[i])
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()

@bot.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.reply(f'Ping: {round(bot.latency*1000)}ms')

@bot.command(aliases=['Test'])
async def test(ctx):
    random_image()
    test_button = Button(label='Test', style=discord.ButtonStyle.green, emoji=':eggplant:')
    test_view = View()
    test_view.add_item(test_button)

    test_embed = discord.Embed(title='Test', description=f'Test :eggplant::eggplant::eggplant:', color=discord.Color.from_rgb(1, 168, 221))
    test_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    test_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=test_embed, view=test_view)

@bot.group(name='bal', invoke_without_command=True, aliases=['Bal', 'Balance', 'balance'])
async def bal(ctx):
    random_image()
    user = ctx.author.id
    name = ctx.author
    mama(user, str(name))

    bal = get_monies(user)

    bal_embed = discord.Embed(title='Your Balance', description=f'Your Balance Is ${bal}', color=discord.Color.from_rgb(1, 168, 221))
    bal_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    bal_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=bal_embed)

@bal.command(aliases=['Check'])
async def check(ctx):
    random_image()
    user = ctx.author.id
    name = ctx.author
    mama(user, str(name))

    user = ctx.message.content.split(' ')[2]
    user = user.replace('<', '')
    user = user.replace('>', '')
    user = user.replace('@', '')
    bal = get_monies(user)

    bal_embed = discord.Embed(title='Their Balance', description=f'Their Balance Is ${bal}', color=discord.Color.from_rgb(1, 168, 221))
    bal_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    bal_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=bal_embed)

@bal.command(aliases=['Send'])
async def send(ctx):
    random_image()
    joe = ctx.author.id
    name = ctx.author
    mama(joe, str(name))

    pp = ctx.message.content.split(' ')

    user = pp[3]
    user = user.replace('<', '')
    user = user.replace('>', '')
    user = user.replace('@', '')
    send_amount = pp[2]

    monies_operation(user, send_amount, '+')
    monies_operation(joe, send_amount, '-')

    your_bal = get_monies(joe)
    their_bal = get_monies(user)

    bal_embed = discord.Embed(title=f'You Sent {send_amount}', description=f'Their Balance Is Now ${their_bal}\nYour Balance Is Now ${your_bal}', color=discord.Color.from_rgb(1, 168, 221))
    bal_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    bal_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=bal_embed)

@bot.command(aliases=['Coin'])
async def coin(ctx):
    random_image()
    user = ctx.author.id
    name = ctx.author
    mama(user, str(name))
    heads = str(ctx.message.content.split(' ')[1])
    amount = int(ctx.message.content.split(' ')[2])

    try:
        if get_monies(user) >= amount:
            if heads.lower() == random.choice(['heads', 'tails']) or user == 405461437520019456:
                monies_operation(user, amount, '+')
                win_embed = discord.Embed(title='Congragulations!', description=f'You Won ${amount}\nYour New Balance Is Now ${get_monies(user)}', color=discord.Color.from_rgb(1, 168, 221))
                win_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
                win_embed.set_thumbnail(url=walter)
                await ctx.reply(embed=win_embed)
            else:
                monies_operation(user, amount, '-')
                lose_embed = discord.Embed(title='Congragulations!', description=f'You Lost ${amount}\nYour New Balance Is Now ${get_monies(user)}', color=discord.Color.from_rgb(1, 168, 221))
                lose_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
                lose_embed.set_thumbnail(url=walter)
                await ctx.reply(embed=lose_embed)
        else:
            await ctx.reply('Use An Amount That Is Under Or Equal Your Balance')
    except:
        await ctx.reply('Proper Syntax: %coin {heads or tails} {Amount}')

@bot.command(aliases=['Truth'])
async def truth(ctx):
    random_image()
    truth = await Estrapy.AniGames.truth()
    truth_embed = discord.Embed(title='Truth', description=f'{truth}', color=discord.Color.from_rgb(1, 168, 221))
    truth_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    truth_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=truth_embed)

@bot.command(aliases=['Dare'])
async def dare(ctx):
    random_image()
    dare = await Estrapy.AniGames.dare()
    dare_embed = discord.Embed(title='Dare', description=f'{dare}', color=discord.Color.from_rgb(1, 168, 221))
    dare_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    dare_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=dare_embed)

@bot.command(aliases=['Leaderboard', 'top', 'Top'])
async def leaderboard(ctx):
    random_image()
    user = ctx.author.id
    name = ctx.author
    mama(user, str(name))

    leaderboard_embed = discord.Embed(title='Pp', description=f'Top 5 $:', color=discord.Color.from_rgb(1, 168, 221))
    leaderboard_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    leaderboard_embed.set_thumbnail(url=walter)

    top = get_leaderboard()
    iiiii = 1
    for k, v in top.items():
        leaderboard_embed.add_field(name=f'{iiiii}.{k}', value=f'${v}')
        iiiii += 1
    await ctx.reply(embed=leaderboard_embed)

@bot.command(aliases=['Nft'])
async def nft(ctx):
    nft_list = ['https://opensea.io/assets/ethereum/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/']
    url = random.choice(nft_list)
    pp = str(random.randint(0, 9999))
    url += pp
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    images = soup.findAll('img')[1]
    src = images['src']

    nft_embed = discord.Embed(title=f'Bored Ape #{pp}', color=discord.Color.from_rgb(1, 168, 221))
    nft_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    nft_embed.set_image(url=src)
    await ctx.reply(embed=nft_embed)

@bot.group(invoke_without_command=True, aliases=['Image', 'im', 'Im'])
async def image(ctx):
    random_image()

    image_embed = discord.Embed(title=f"You Got '{jesse.title()}'", color=discord.Color.from_rgb(1, 168, 221))
    image_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    image_embed.set_image(url=walter)
    await ctx.reply(embed=image_embed)

@image.command(aliases=['Get'])
async def get(ctx):
    phrase = ctx.message.content
    base = ctx.message.content.split(' ')
    phrase = phrase.replace(base[0], '')
    phrase = phrase.replace(base[1], '')
    phrase = phrase.strip()
    random_image_custom(phrase)

    image_embed = discord.Embed(title=f"You Looked Up Images For '{jesse.title()}'", color=discord.Color.from_rgb(1, 168, 221))
    image_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    image_embed.set_image(url=walter)
    await ctx.reply(embed=image_embed)

@bot.command(aliases=['Bored'])
async def bored(ctx):
    random_image()
    r = requests.get('https://www.boredapi.com/api/activity')
    json_data = r.json()
    activity = json_data['activity']
    activity_type = json_data['type']

    image_embed = discord.Embed(title=f'Your Activity', description=f'Your Activity: {activity}\nActivity Type: {(activity_type).title()}', color=discord.Color.from_rgb(1, 168, 221))
    image_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    image_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=image_embed)

def card_deck():
    global deck
    card_value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_type = ['Hearts','Spades','Clubs','Diamonds']
    for i in range(2):
        for i in card_type:
            for j in card_value:
                deck.append(j + ' Of ' + i)
    return deck

def gen_card():
    o = random.choice(deck)
    deck.remove(o)
    return o

def determine_value(card):
    card = card.split(' ')[0]

    if card in ['Jack', 'Queen', 'King']:
        return 10
    elif card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(card)
    elif card == 'Ace':
        pass

@bot.command(aliases=['Blackjack', 'blackjack', 'Bj'])
async def bj(ctx):
    random_image()
    user = ctx.author.id
    name = ctx.author
    mama(user, str(name))
    amount = ctx.message.content.split(' ')[1]

    async def hit_callback(interaction):
        pass
    async def stand_callback(interaction):
        pass

    if int(amount) >= 100:
        card1 = gen_card()
        card2 = gen_card()
        dealer_card1 = gen_card()
        dealer_card2 = gen_card()

    else:
        await ctx.reply('You Have To Have At Least $100')

@bot.command(aliases=['Slots'])
async def slots(ctx):
    global rolls

    random_image()
    user = ctx.author.id
    name = ctx.author
    mama(user, str(name))

    thingies = [':eggplant:', ':peach:', ':sweat_drops:', ':nerd:', ':clown:', ':moyai:']
    rolls = []

    cool_money_get = 0

    if int(get_monies(user)) >= 100:
        monies_operation(user, 100, '-')

        rolls = []
        while int(len(rolls)) != 3:
            get_roll()

        if count_pp(':moyai:', rolls) == 3 or count_pp(':nerd:', rolls) == 3:
            cool_money_get = 6969
        elif count_pp(':clown:', rolls) == 3:
            cool_money_get = 699
        elif rolls == [':eggplant:', ':peach:', ':sweat_drops:'] or count_pp(':peach:', rolls) == 3 or count_pp(':eggplant:', rolls) == 3 or count_pp(':clown:', rolls) == 3:
            cool_money_get = 6969
        else:
            cool_money_get = 0

        amongnus = ''
        for i in range(len(rolls)):
            amongnus += rolls[i]

        monies_operation(user, cool_money_get, '+')

        slots_embed = discord.Embed(title=f'Slots Big Pp', description=f'You Rolled: {amongnus}\nYou Got ${cool_money_get}\nYour Balance Is Now {get_monies(user)}', color=discord.Color.from_rgb(1, 168, 221))
        slots_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
        slots_embed.set_thumbnail(url=walter)
        await ctx.reply(embed=slots_embed)
    else:
        slots_embed = discord.Embed(title=f'Too Poor :rofl:', description=f'Get Some Money', color=discord.Color.from_rgb(1, 168, 221))
        slots_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
        slots_embed.set_thumbnail(url=walter)
        await ctx.reply(embed=slots_embed)

@bot.command(aliases=['Screenshot'])
async def screenshot(ctx):
    random_image()
    link = gen_screenshot()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r = requests.get(link, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    images = soup.findAll('img', src=True)
    images = [x['src'] for x in images]

    for screenshot in images:
        if 'https://' in screenshot and 'prnt.sc' not in screenshot:
            screenshot_embed = discord.Embed(title=f'Your Random Screenshot', description=f'Image Link (Working On Embed Image Shit): {screenshot}', color=discord.Color.from_rgb(1, 168, 221))
            screenshot_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
            screenshot_embed.set_thumbnail(url=walter)
            await ctx.reply(embed=screenshot_embed)
        else:
            pass

@bot.command(aliases=['lego', 'Lego'])
async def batman(ctx):
    random_image()
    batman_embed = discord.Embed(title=f'Lego Batman (W)', description=f"Enjoy Your Movie (Totally Not Illegal But It's Funny)\nhttps://img.guildedcdn.com/ContentMediaGenericFiles/ec3d1f56be6b1b59c4446bbd9e789c23-Full.mp4?w=854&h=354", color=discord.Color.from_rgb(1, 168, 221))
    batman_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    batman_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=batman_embed)

@bot.group(invoke_without_command=True, aliases=['Quote'])
async def quote(ctx):
    get_quote()
    random_image()

    quote_embed = discord.Embed(title=f'Random Quote', description=f"Quote: {joeee}\nSaid By: {joeeee}\nSubmitted By: {joeeeee}", color=discord.Color.from_rgb(1, 168, 221))
    quote_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    quote_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=quote_embed)

@quote.command(aliases=['Add'])
async def add(ctx):
    random_image()

    quote = ctx.message.content
    submitter = ctx.author
    j = quote.split(' ')[0]
    o = quote.split(' ')[1]
    quote = quote.replace(j, '')
    quote = quote.replace(o, '')
    quotee = quote.split(' ')[-1]
    quote = quote.replace(quotee, '')
    quote = quote.strip()

    joe_quote(quote, quotee, submitter)

    quote_embed = discord.Embed(title=f'Submitted Quote', description=f"Quote: {quote}\nSaid By: {quotee}\nSubmitted By: {submitter}", color=discord.Color.from_rgb(1, 168, 221))
    quote_embed.set_author(name='Executed By '+ ctx.author.display_name, url=hot, icon_url=hot)
    quote_embed.set_thumbnail(url=walter)
    await ctx.reply(embed=quote_embed)

bot.run('')
