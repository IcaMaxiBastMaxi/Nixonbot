# This is a sample Python script.
# Nixonclient v 1.2
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# client.py
import random
import os
from dotenv import load_dotenv
import youtube_dl
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(D6nr)

Adject = ['Liberal ', 'Secular', 'Criminal', 'Stupid',  'Centrist', 'Radical ', 'Dictatorial ', 'Whimsical', 'Based',
          'Dengist', 'Nationalist ', 'Classical ', 'Individualist ', 'Libertarian ', 'Futurist ', 'Social ', 'Green ',
          'Authoritarian ', 'Auth ', 'Orthodox ']
Adject2 = ['Eco-', 'Turkish', 'Christian',
           'https://tenor.com/view/ray-william-johnson-turkish-turkey-angry-man-gif-17112765', 'Islamic', 'Jewish',
           'Sámi', 'Saltsea', 'Revolutionary', 'Right-wing', 'Left-wing', 'Pacifist', 'Mosaic ', 'Ultra-', 'Agrarian ',
           'Pirate', 'Matriachical', 'Patriarchical', 'Jingoist ', 'Republican', 'Totalitarian ', 'Ethno-', 'Queer ',
           'Neo-', 'Paleo-', 'Elective ', 'Danish', 'Constitutional ', 'Traditionalist ', 'Anti-', 'Market ', 'Anarcho-',
           'Conservative ']
Main = ['Xi-ism ', 'Oilbaronism', 'Sabaism', 'Fuccboi-ism', 'Alcoholism', 'Leisureism', 'Hedonism', 'Nomadism',
        'Redwine-socialdemocrat', 'Charter-companyism', 'Dean-Browningism', 'Ho-Chi-Minh Thought', 'Direct-democracy',
        'Third way', 'Procrastinism', 'Big-Tent', 'Pol-Potism', 'Communalism', 'Hive-Mind Collectivism', 'Salafism',
        'Platoism', 'Mormonism', 'Nazism', 'Environmentalism', 'Imperialism', 'Centrism', 'Feminism', 'Putinism',
        'Baathism', 'Zionism', 'Ultranationalism', 'Nationalism', 'Populism', 'Reformist', 'National Bolsevism',
        'Maoism ', 'Agrarianism ', 'Trotskyism ', 'Stalinism ', 'Juche ', 'Marxism ', 'State Capitalism ', 'Fascism ',
        'Theocraticism ', 'Corporateism ', 'Aristrocratism ', 'Technocraticism ', 'Pinochetism ', 'Monarchism ',
        'Totalitarianism', 'Feudalism ', 'Conservatism ', 'Communism ', 'Dengism ', 'Primitivism ', 'Liberalism ',
        'Social-Democracy ', 'Confederalism ', 'Syndicalism ', 'Socialism ', 'Pacifism ', 'Capitalism ',
        'Kleptocracism ', 'Transhumanism ', 'Maxist-Leninist']
crook_quotes = ["Don't lick the dick!", "Lick the dick!", "Eat the chicken",
                "I did not wiretap the democrats, it's not true! It's bullshit! I did not wiretap them! I did not! Oh hi, Ford.",
                "Kick ‘em in the ass. Ok?",
                "They’re against it because they consider it a dictatorship. I don’t give a damn what it is; I’m for ‘em",
                "One can only be angry with those he respects", "Not illegal!",
                "Let’s find somebody in this world we can kick.",
                "https://tenor.com/view/richard-nixon-republican-president-corrupt-crook-gif-19639396",
                "I've earned everything I've got", "I am not a crook",
                "The Cold War isn't thawing; it is burning with a deadly heat. Communism isn't sleeping; it is, as always, plotting, scheming, working, fighting.",
                "If you take no risks, you will suffer no defeats. But if you take no risks, you win no victories.",
                "If an individual wants to be a leader and isn't controversial, that means he never stood for anything.",
                "The presidency has many problems, but boredom is the least of them.", "Sock it to me?"]
food_quote = ["I am not a cook"]
arrayOfUsersIds = ['905919187766083595']
ashook_quote = ["I'm not ashook", "I have decided we’re going to give Allende the hook"]
book_quote = ["I am not a book"]
krok_quote = ["I am not a krok"]
chicken_quote = ["I am not a cock"]
youtube_quote = ["Youtube is the crook!"]
fyeah = ["Fuck yeah"]
youtube = ["youtube", "Youtube", "youtube?"]
chicken = ["Chicken", "chicken", "kyckling", "Kyckling"]
america = ["America?", "america?"]
election = ["1972"]
join = ["Join the channel"]
should = ["Should I", "should I", "should i", "Should i"]
shouldans = ["Yes", "No", "Maybe", "¯\_(ツ)_/¯", "Definitely", "My sources say no"]
coinflip = ["Coinflip"]
flipcoin = ["Heads", "Tails"]
D6 = ["D6"]
D6nr = list(range(1,7))
leave = ["Leave the channel"]
ideology = ["Based", "based", 'Baserad', 'baserad',
            'Jag känner mig så osolidarisk idag, ge mig någonting att engagera mig i', "basado",
            "Basado", "vuođđoduvvon", '踏实', "perusteltu", "Perusteltu", "vuođđuduvvon", "Vuođđuduvvon",
            "Vuođđoduvvon", "Baserat", "baserat"]
krok = ["krok", "Krok", "Kroken", "kroken", "Krokar", "krokar"]
commandhelp = ["Help me Nixon"]
crookwords = ['crook', 'CROOK', 'Nixon', 'nixon', 'Richard Nixon', 'Crook', 'crookoids', "Nicke", "nicke"]
foodwords = ['kött', 'mat', 'fläskkotlet']
ashookwords = ["Förvånad", "förvånad", "Chile", "chile", "chileansk", "Chileansk"]
book = ["bok", "litteratur"]
kennedy = ["Kennedy", "kennedy", "JFK"]
music = ["Are you a crook?"]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id == arrayOfUsersIds:
        return message.reply('You are on the crooklist!')

    for i in ideology:
        if i in message.content:
            await message.channel.send("Here is your new based ideology: ")
            if random.randint(0, 100) <= 70:
                await message.channel.send(random.choice(Adject))
            if random.randint(0, 100) <= 70:
                await message.channel.send(random.choice(Adject2))
            await message.channel.send(random.choice(Main))
            return

    for i in D6:
        if i in message.content:
            await message.channel.send("I am rolling the die")
            await message.channel.send(random.sample(D6nr, 1))
            return

    for i in should:
        if i in message.content:
            await message.channel.send(random.choice(shouldans))
            return

    for i in coinflip:
        if i in message.content:
            await message.channel.send(random.choice(flipcoin))
            return

    for i in commandhelp:
        if i in message.content:
            await message.channel.send("fuck no")
            return

    for i in join:
        if i in message.content:
            channel = message.author.voice.channel
            await channel.connect()

    for i in leave:
        if i in message.content:
            voice_client = message.guild.voice_client
            if voice_client.is_connected():
                await voice_client.disconnect()
                await message.channel.send("I've left the voice channel for important presidential work")

    for i in crookwords:
        if i in message.content:
            response = random.choice(crook_quotes)
            await message.channel.send(response)
            return

    for i in youtube:
        if i in message.content:
            response = random.choice(youtube_quote)
            await message.channel.send(response)
            return

    for i in chicken:
        if i in message.content:
            response = random.choice(chicken_quote)
            await message.channel.send(response)
            return

    for i in foodwords:
        if i in message.content:
            response = random.choice(food_quote)
            await message.channel.send(response)
            return

    for i in ashookwords:
        if i in message.content:
            response = random.choice(ashook_quote)
            await message.channel.send(response)
            return

    for i in krok:
        if i in message.content:
            response = random.choice(krok_quote)
            await message.channel.send(response)
            return

    for i in book:
        if i in message.content:
            response = random.choice(book_quote)
            await message.channel.send(response)
            return

    for i in america:
        if i in message.content:
            response = random.choice(fyeah)
            await message.channel.send(response)
            return

    if random.randint(0, 100) <= 0.01:
        await message.channel.send(
            f"{message.author.mention}, Me and Stefan Löfven have a lot in common. We both got elected into office, got into scandals and had to resign. The difference between us is that I'm not a crook.")
        return

    if random.randint(0, 100) <= 0.01:
        await message.channel.send(f"{message.author.mention}, I am not a crook")
        return

    for i in kennedy:
        if i in message.content:
            await message.channel.send("https://tenor.com/view/sweating-nervous-paranoid-gif-4974019")
            return

    for i in election:
        if i in message.content:
            await message.channel.send("https://tenor.com/view/richard-nixon-nixon-president-smile-happy-gif-17083965")
            return

    if random.randint(0, 100) <= 0.01:
        await message.channel.send("I've heard there is a great poet called Saba, I'd like to meet this man")
        return

    if random.randint(0, 100) <= 0.01:
        await message.channel.send("https://youtu.be/MacmN1EtIPQ")
        return


bot.run('ODU4MzU3NTM1MTUyOTMwODM3.YNc9vw.ht0StCuGOmV--UbEx0LYOaGyGvk')
