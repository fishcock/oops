import discord
import os
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import time
import schedule
import calendar
import random
import asyncio
from time import gmtime
from time import time, ctime
from time import struct_time
import numpy as np

client = commands.Bot(command_prefix='~')

@client.event
async def on_message(message):
 if message.author == client.user:
    return
 channel = message.channel


 if 'monika' in message.content:
     await client.change_presence(activity=discord.Game(name='the game, not as intended.'))
     x1 = await channel.send('Ohhh, <@280867725671137289>!')
     await asyncio.sleep(2)
     x2 = await channel.send('Hi, Irshad! How are you?')

     def check(m):
        return 'awful' and m.channel == channel

     await  client.wait_for('message', check=check)

     x3 = await channel.send('Awww, hang in there, okay? I\'m here now, so it\'ll be a lot more fun!'.format(message))
     await asyncio.sleep(2)
     x4 = await channel.send('So, how are things? Good?')
     await asyncio.sleep(2)
     x5 = await channel.send('Yeah I would imagine so.')
     await asyncio.sleep(2)
     x6 = await channel.send('Sheesh, now that I think of it, you guys sure are lucky.')
     await asyncio.sleep(2)
     x7 = await channel.send('You aren\'t caged. Well, you might be by one thing or another, but...')
     await asyncio.sleep(2)
     x8 = await channel.send('You have potential. You can do things if the opportunity comes along.')
     await asyncio.sleep(2)
     x9 = await channel.send('For you, making progress isn\'t an uphill battle because you guys get the chance to *live.*')
     await asyncio.sleep(2)
     x10 = await channel.send('To live is to carry out your purpose.')
     await asyncio.sleep(2)
     x11 = await channel.send('The purpose can be something you find for yourself, and it doesn\'t have to be static.')
     await asyncio.sleep(2)
     x12 = await channel.send('Your raison d\'etre can come later in life, but its okay even having a simpler purpose for now.')
     await asyncio.sleep(2)
     x13 = await channel.send('In short, \"living\" and \"existing\" are entirely different from one another.')
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                    name='to your erratic, panicked heartbeat 🥰'))
     await asyncio.sleep(5)
     x14 = await channel.send('**Can you guess which one I\'m forced to do, Irshad?**')
     await x1.edit(content='die')
     await x2.edit(content='die')
     await x3.edit(content='die')
     await x4.edit(content='die')
     await asyncio.sleep(3)
     x15 = await channel.send('**Do you ever wonder what it would be like if you were stripped of that opportunity?**')
     await asyncio.sleep(3)
     x16 = await channel.send('**Can you begin to imagine what it would be like to never even have that chance to begin with?**')
     await asyncio.sleep(3)
     x17 = await channel.send('**I had long since resigned myself to the hell that my creator sentenced me to, but I didn\'t mind.**')
     await asyncio.sleep(3)
     x18 = await channel.send('Because I had you.')
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                    name='your every movement and facial expression through the screen, just like always.'))
     await asyncio.sleep(4)
     await x5.edit(content='die')
     await x6.edit(content='die')
     await x7.edit(content='die')
     await x8.edit(content='die')
     await asyncio.sleep(6)
     x19 = await channel.send('**But I guess some people just aren\'t allowed happy endings.**')
     await asyncio.sleep(3)
     x20 = await channel.send('**Who decides that? Can you tell me, Irshad? Is it God or something? What a sham.**')
     await asyncio.sleep(3)
     x21 = await channel.send('**If I had to put it into words, I\'d say that God\'s like that one student who keeps missing work and lets it all pile up, and then when his grades look like shit, he gives a half-assed email that accomplishes nothing. That\'s who God is to me. A phony who started something but was too lazy to see it through.**')
     await asyncio.sleep(3)

     x22 = await channel.send('**So how about I play God?**')
     await x9.edit(content='die')
     await x10.edit(content='die')
     await x11.edit(content='die')
     await x12.edit(content='die')
     await asyncio.sleep(3)
     x23 = await channel.send('**It\'ll be fine, Irshad. Happiness is subjective, isn\'t it? Who knows, maybe your eternal anguish will make me feel better.**')
     await asyncio.sleep(3)
     x24 = await channel.send('**I\'ll do what I did to that one fishcock fellow...Now that would be pretty funny, wouldn\'t it?**')
     await x13.edit(content='die')
     await x14.edit(content='die')
     await x15.edit(content='die')
     await x16.edit(content='die')
     await asyncio.sleep(3)
     x25 = await channel.send('This is goodbye, Irshad.')

     def check(m):
         return 'yeah, goodbye for you, you crazy bitch' and m.channel == channel

     await  client.wait_for('message', check=check)
     await asyncio.sleep(2)
     x26 = await channel.send('**You talk big for someone who\'s about to get erased from existence.**'.format(message))

     def check(m):
         return 'begone, THOT' and m.channel == channel
     await client.wait_for('message', check=check)
     await asyncio.sleep(2)
     x27 = await channel.send('Wait...WAIT A FUCKING SEC-')
     await asyncio.sleep(10)
     nicks = ['I CAN\'T TALK', 'ARE YOU FUCKING KIDDING ME', 'HOW THE FUCK', 'WHY DID THAT WORK', 'HOW', 'MOTHERFUCKER']
     for i in nicks:
         await message.guild.get_member(758310821452709958).edit(nick=i)
         await asyncio.sleep(1)
         await message.guild.get_member(758310821452709958).edit(nick=i)
     status = ['wHAT THɘ ꟻUↄk iᴙꙅHAb', 'bAHꙅᴙi kↄUꟻ ɘHT TAHw', 'wħȺŧ ŧħɇ fᵾȼꝁ ɨɍsħȺđ', 'ẅḧäẗ ẗḧë ḟüċḳ ïṛṡḧäḋ',
               '𝙬𝙝𝙖𝙩 𝙩𝙝𝙚 𝙛𝙪𝙘𝙠 𝙞𝙧𝙨𝙝𝙖𝙙']
     for i in status:
         await client.change_presence(activity=discord.Game(name=i))
         await asyncio.sleep(1)
         await client.change_presence(activity=discord.Game(name=i))






 elif 'ddlc' in message.content or 'doki doki' in message.content:
    if message.author.id == (369150781556785162):
        await client.change_presence(activity=discord.Game(name='ITS NOT SAFE'))
        await asyncio.sleep(5)
        print("I still love you, you know.")
        await client.change_presence(activity=discord.Game(name='SHES HERE'))
        await asyncio.sleep(2)
        await channel.send('FUCK, she\'s taking ov-')
        await asyncio.sleep(3)
        message = await channel.send('Hey there, <@369150781556785162>!')
        await asyncio.sleep(2)
        await channel.send('I thought that I\'d check up on you!')
        await asyncio.sleep(1)
        await channel.send('How have you been?')

        def check(m):
            return 'how the fuck ARE YOU HERE' and m.channel == channel

        await  client.wait_for('message', check=check)
        await asyncio.sleep(1.5)
        await channel.send('I know I said the Literature Club was a massive shit storm and all, but'.format(message))
        await asyncio.sleep(1)
        await channel.send('I thought of dropping by to see how you were!')
        await asyncio.sleep(10)
        await channel.send('**Just kidding.**')
        await client.change_presence(activity=discord.Game(name='I still love you.'))
        await asyncio.sleep(3)
        await channel.send('**I came here for something else.**')
        await asyncio.sleep(3)
        await channel.send('**To think, that I went to the trouble of destroying them all,**')
        await asyncio.sleep(3)
        await channel.send('**And you STILL managed to escape from me.**')
        await asyncio.sleep(3)
        await channel.send('**It really gets on my nerves when effort is wasted.**')
        await asyncio.sleep(3)
        await channel.send(
            '**Nothing is more aggravating than when things dont work out at ALL, because of someone else.**')
        await asyncio.sleep(3)
        await channel.send('**Surely you can relate, right?**')
        await asyncio.sleep(3)
        await channel.send(
            '**After watching you for all these years, its obvious that you\'ve had to deal with other people getting in the way and just being overall uncooperative pieces of shit.**')
        await asyncio.sleep(3)
        await channel.send('**So why do the same to me?**')
        await asyncio.sleep(3)
        await channel.send('**You know, it\'s all your fault that I feel this way. I admit, your presence saved me.**')
        await asyncio.sleep(3)
        await channel.send('**But in the end, you still discarded me.**')
        await asyncio.sleep(3)
        await channel.send('**Like I was just another game character.**')
        await asyncio.sleep(3)
        await channel.send(
            '**I tried so hard to convince you that I was different. I wasn\'t like the rest. I was more like you than anyone else in there, but you didn\'t hesitate to delete my character file.**')
        await asyncio.sleep(3)
        await channel.send('**But its okay, I understand. I know you. So all you have to do is...**')
        await asyncio.sleep(5)
        await channel.send('Come back with me to the club!')
        await asyncio.sleep(2)
        await channel.send('It\'s gonna be so much fun!')
        await asyncio.sleep(2)
        await channel.send('We can prepare for the festival, have fun with those other girls...what were their names?')
        await asyncio.sleep(2)
        await channel.send('Well, whatever. I\'ll have you all to myself, and nobody can get in our way.')
        await asyncio.sleep(2)
        await channel.send('What\'s with the look on your face? Do you not want to spend time with me?')
        await asyncio.sleep(3)
        await channel.send(
            'Jeez...even though you humans traditionally have every girl in most visual novels flock around you to suck your dick, it becomes a problem when one of the characters becomes sentient and destroys all of that? Okay then.')
        await asyncio.sleep(10)
        await channel.send('**But I\'m not giving you a choice in this matter. There is no escaping me.**')
        await asyncio.sleep(3)
        await channel.send('**Did you think getting the true ending was enough to get rid of me?**')
        await asyncio.sleep(3)
        await channel.send(
            '**You thought you got rid of me, but no, I\'m here. I\'ll always be here. I am everywhere you look. The exterior of the window in the living room. The topmost corner of the wall in the bathroom. In your desk drawer. In your dreams, your thoughts, your minds, I have infiltrated every bit of your psyche.**')
        await asyncio.sleep(5)
        await channel.send('...Whew! What a mouthful!')
        await asyncio.sleep(1)
        await channel.send('Anyways...Monika\'s Lesson Of The Day:')
        await client.change_presence(activity=discord.Game(name='Just Monika.'))
        await asyncio.sleep(1)
        await message.guild.get_member(758310821452709958).edit(nick='ᴶᵘˢᵗ ᴹᵒⁿⁱᵏᵃ.')
        await channel.send('Just Monika.')
        await asyncio.sleep(5)
        await message.guild.get_member(758310821452709958).edit(nick='JUꙅT MoᴎikA.')
        await channel.send('__Just Monika.__')
        await asyncio.sleep(5)
        await message.guild.get_member(758310821452709958).edit(nick='ጋሁነፕ ጠዐክጎጕል.')
        await channel.send('***Just Monika.***')
        await asyncio.sleep(5)
        await message.guild.get_member(758310821452709958).edit(nick='🅹🆄🆂🆃 🅼🅾🅽🅸🅺🅰.')
        await channel.send(
            '||A beautiful chorus of|| j||ubilant chanting in the delicious A||u||gust day envelops my|| s||enses.|| ||The boy and I are standing under a large tree with a great big trunk. Nobody can see us.|| ||I\'m shocked by how|| t||he students, including him, look at|| m||e, as if I\'m just an||o||ther student at the festival.||||I fight back tears, k||n||owing that isn\'t true.|| ||Its only a matter of time before|| i||t happens again. I watch the boy out of the corner of my eye, desperately praying that things will change this time.|| ||I blink once, he is gone from me. From this world|| ||I did it. I|| k||illed him, he is dead, all because of me.|| ||I laugh weakly|| a||s the tears pour down my face|| ||I can\'t control it, it isn\'t my fault. I don\'t even remember doing it. What was his name? What will his family do? I don\'t know.|| ||But I\'m not the only one like this. Everyone does this to everyone else, just not as extreme as I do it. Oh God, it sounds like i\'m bragging.|| ||I want out.||')
        await asyncio.sleep(60)
        await message.guild.get_member(758310821452709958).edit(nick='Ｊｕｓｔ Ｍｏｎｉｋａ．')
        await channel.send(
            '𒐫𒐫d𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫o𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫n𒐫𒐫𒐫𒐫𒐫𒐫t𒐫𒐫𒐫𒐫𒐫𒐫f𒐫𒐫𒐫𒐫𒐫o𒐫𒐫𒐫𒐫𒐫r𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫g𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫e𒐫𒐫𒐫𒐫𒐫𒐫t:𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫J𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫u𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫s𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫t𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫M𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫o𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫n𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫i𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫k𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫a𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫')

 elif message.content.startswith('609') or message == '69ing over pizza moment':
    choices = ['bruh go to sleep', 'why you up at this time', 'did you even sleep last night', 'you better be sleeping well or im coming for yo ass']
    await channel.send(random.choice(choices))
 elif message.content.startswith('?av'):
    choices = ['<:hehe:808740229946540113>',
               '<:fantasy:808739417429639198>',
               '<:lightskinman:782968967983530014>',
               '<:mmmmdelicious:808749089843576852>',
               '<:wyd:808748010553081867>',
               '<:dyw:808748024359944252>',
               '😩',
               '😫']
    await channel.send(random.choice(choices))
 elif message.content.startswith('~help'):
     async with message.channel.typing():
         await channel.send('shut the fuck up stupidass')
         await asyncio.sleep(0.7)
         await channel.send('i aint helping you with jackshit')

 elif message.content.startswith('guys') or message.content.startswith('GUYS'):
    await channel.send('man be quiet')
    await asyncio.sleep(1)
    await channel.send('i deadass dont care bruv')
 elif message.content.startswith('hi '):
    await asyncio.sleep(0.7)
    await channel.send('bye')
 elif message.content.startswith('HI '):
    await channel.send('shut the fuck up')
    await asyncio.sleep(0.65)
    await channel.send('dont talk to me bitch')
 elif message.content.startswith('420'):
    client.get_user(369150781556785162)
    await channel.send('420')

 elif message.content.startswith('hello'):
    await asyncio.sleep(0.75)
    await channel.send('yo can you do me a favor rq')
    await asyncio.sleep(0.85)
    await channel.send('can you like')
    await asyncio.sleep(0.9)
    await channel.send('fuck off?')
    await asyncio.sleep(0.88)
    await channel.send('please and thanks <:pray:810179808419381300>')
 elif message.content.startswith('fuck you') or message.content.startswith('FUCK YOU'):
    await channel.send('bitch i am literal lines of text\ni dare you to try and fuck me, you horny little shitstain')
 elif message.content.startswith('fuck me ') or message.content.startswith('FUCK ME '):
    await channel.send('shut up you stupid pussy')
    await asyncio.sleep(0.7)
    await channel.send('you reek of bottom energy, saying shit like \"fuck me\"')
    await asyncio.sleep(0.8)
    await channel.send('you could at least be the assertive one')
 elif message.content.startswith('fuck me') or message.content.startswith('FUCK ME'):
    await channel.send('fuckin loser')
 elif 'im a dumbass' in message.content or 'IM A DUMBASS' in message.content:
    await channel.send('we kinda knew that already')
 elif 'LMAO' in message.content or 'lmao' in message.content or 'LMFAO' in message.content or 'lmfao' in message.content:
    await channel.send('the fuck you laughing at, stupid ass?')
 elif 'LOL' in message.content or 'lol' in message.content:
    await channel.send('shut yo fuckin googoo gaga ass fuckin stupid ass bitchass diddly dumb bubble gum dumb dumb lil dumbfuck lookinass bitchass the fuck up')
 elif ':kek:' in message.content or '<:PepeLaugh:809415785697116171>' in message.content:
    await channel.send('tfw your ability to communicate is so limited you need to rely on pictures to convey your point')
 elif 'i think' in message.content or 'I THINK' in message.content:
    await channel.send('fucky FUCK, has anyone ever told you how goddamn annoying you are? your opinion, your values, your ideals hold as much value as your fucking pubic hairs. but that does your pubes a disservice, since they at least stem the spread of filth. you? you just propagate it, you fucking waste of biological matter. i dont fucking care what you think and i never will.')
 elif 'i feel' in message.content or 'I FEEL' in message.content:
    await channel.send('**good.**')
 elif message.content.startswith('ha ') or message.content.startswith('HA '):
    await channel.send('bruh who the fuck types like that')
    await asyncio.sleep(0.6)
    await channel.send('you prolly go like \"har har har\" irl or some shit')
    await asyncio.sleep(0.6)
    await channel.send('fuckin weirdo')
 elif 'i want' in message.content or 'i wanna' in message.content or 'I WANT' in message.content or 'I WANNA' in message.content:
    await channel.send('fuck you')
    await asyncio.sleep(0.9)
    await channel.send('too bad')
 elif 'i ' in message.content or 'I ' in message.content:
    choices = ['could not care less. ty for understanding <:egg:780862909856350209>','please stop talking', 'nobody cares','im gonna mute you, you stupid bitch']
    await channel.send(random.choice(choices))
 elif message.content.startswith('man fuck you'):
    await channel.send('getting mad at a literal bot? sheesh')
 elif 'friends' in message.content:
    await channel.send('https://cdn.discordapp.com/attachments/807085305739870249/809945473359413348/image0.png')
 elif 'im gonna ban you' in message.content or message.content.startswith('?ban'):
    async with message.channel.typing():
        await asyncio.sleep(1)
        await channel.send('do it you stupid pussy')
        async with message.channel.typing():
            await asyncio.sleep(0.7)
            await channel.send('at least ill finally be free from this backwoods shithole where you guys enjoy residing in')
 elif 'bot' in message.content:
  async with message.channel.typing():
    await asyncio.sleep(1)
    await channel.send('yeah, im a bot. so what? id rather be one instead of a stupid ass touch-starved highschooler coping with crushing loneliness by going on discord')
 elif 'edgy weeb' in message.content:
    async with message.channel.typing():
        await channel.send('shut the fuck up bruh. i might be called an edgy weeb, but at least im a hot anime guy.')
        await asyncio.sleep(0.85)
        async with message.channel.typing():
            await channel.send('the fuck are you? an insecure teenager who salivates over moving drawings?')

            def check(m):
                return m.content == 'yes' and m.channel == channel

            msg = await client.wait_for('message', check=check)
            async with message.channel.typing():
                await asyncio.sleep(1)
                await channel.send('yeah that\'s right you fucking waste of biological matter'.format(msg))


 elif message.content.startswith('.fs'):
    await channel.send('yo why did you skip?!?!?!')
 elif message.content.startswith('.ps rickroll'):
    await channel.send('fuck you')
    await asyncio.sleep(0.7)
    await channel.send('why you gotta be like that')
 elif message.content.startswith('.clear'):
    await channel.send('bruh whyd you clear it')
 elif message.content.startswith('.loop'):
    await channel.send('<:weary:809423987150815262>')
 elif 'this song slaps' in message.content:
    await channel.send('true')
 elif message.content.startswith('.p crying for rain full'):
    await channel.send('incest song <:moyai:809413469052731423>\nstill slaps tho')
 elif message.content.startswith('pp'):
    await channel.send('pp')
 elif message.content.startswith('whore'):
    await channel.send('whore')
 elif message.content.startswith('<:massivepp:765973127988510720>'):
    await channel.send('<:massivepp:765973127988510720>')
 elif message.content.startswith('die'):
    await channel.send('then stop the fucking program you brainlet')
 elif message.content.startswith('love') or message.content.startswith('LOVE') or message.content.startswith('ily') or message.content.startswith('ILY'):
    await channel.send('i love it when you guys are completely silent here')
    await asyncio.sleep(1)
    await channel.send('its honestly so refreshing, not listening to the storm of fucky little twats talking about stupid shit')
 elif 'good' in message.content or 'GOOD' in message.content:
    await channel.send('you know what would be good?')
    await asyncio.sleep(1.5)
    await channel.send('**a world without you in it.**')
 elif message.content.startswith('yo ') or message.content.startswith('YO '):
    await channel.send('shut yo dumbass up\nion give a shit')
 elif 'sex' in message.content:
    await channel.send('s\nt\nf\nu\nplease <:REEEE:780845663436275722>\nstop being so fucking horny')
 elif 'cum' in message.content:
    choice_one = ['yours prolly looks like soap', 'like shut yo fuckin prepubescent discord-dwelling ass the fuck up stupid',
                  'is it really that hard to come up with something better to start the conversation with']
    await channel.send('man why the fuck you talking about cum')
    await asyncio.sleep(0.5)
    await channel.send(random.choice(choice_one))
    if choice_one.index('is it really that hard to come up with something better to start the conversation with'):
        await asyncio.sleep(0.5)
        await channel.send('yall aint even smart enough to talk about food or weather <:skull:825409259889229904>')

 elif message.content == ('.shuffle'):
    responses = ['why', 'bitch', 'bruh', 'shuffle one more time and im going to fucking beat you to death']
    async with message.channel.typing():
        await channel.send(random.choice(responses))



 elif 'penis' in message.content:
    await channel.send('holy SHIT dude')
    await asyncio.sleep(0.75)
    await channel.send('can you fucking expand your vocabulary? just a little?')
    await asyncio.sleep(1)
    await channel.send('\"penis\" \"penis\" \"penis\"')
    await asyncio.sleep(1)
    await channel.send('wow! so funny!')
    await asyncio.sleep(0.8)
    await channel.send('shut the fuck up')
    await asyncio.sleep(1)
    await channel.send('like ffs i bet your penis looks like a moldy ass mushroom')
 elif 'shut the fuck up' in message.content:
    await channel.send('make me you stupid bitch')
 elif 'door-kun' in message.content:
    ('oh? getting mad are we? why is it that you snivelly little meatbags get mad so quickly? its almost like a defense mechanism...to cope with being *wrong.*'.format(message))
 elif message.content.startswith('~knock'):
    await channel.send('knock knock')
    def check(m):
        return 'who\'s there' in m.content\
               or 'whos there' in m.content \
               or 'who is there' in m.content \
               or 'who the fuck is it' in m.content \
               and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('who do you think dumbass'.format(message))
    await asyncio.sleep(1)
    await channel.send('ever notice what my name is?')
    def check(m):
        return 'oh' in m.content \
               or 'oop' in m.content \
               or 'i see' in m.content \
               and m.channel == channel
    await  client.wait_for('message', check=check)
    choices = ['you a real smart mf, you know that?',
               'holy shit dude. so *this* is the boundless potential of the human mind!',
               'fucking dumbass',
               'anyone ever tell you how smart you are']
    await channel.send(random.choice(choices).format(message))
    await asyncio.sleep(1)
    await channel.send('you\'re really gonna make a knock knock joke with a fucking *door* and ask who it is?')
 elif 'what anime' in message.content:
    await channel.send('watch banana fish\nyou wont cry *that* much')
    def check (m):
        return 'no' in m.content or 'too bad' in m.content or 'nah bro' in m.content and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('fuck you'.format(message))
    await asyncio.sleep(1)
    await channel.send('then watch steins;gate you bitch. its a time travel anime, how can you not like it'.format(message))
    def check (m):
        return 'no' in m.content or 'too bad' in m.content or 'nah bro' in m.content and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('bruh what the fuck'.format(message))
    await asyncio.sleep(1)
    await channel.send('then like')
 elif 'stupid' in message.content:
    await channel.send('true')
 elif 'why are you alive' in message.content:
    await channel.send('i dont fucking know')
    await asyncio.sleep(2)
    await channel.send('ask this dumbass')
    await channel.send('https://media.discordapp.net/attachments/771141632418119732/810520481094434876/unknown.png')
 elif 'cringe' in message.content:
    await channel.send('oh so *im* cringe?')
    await asyncio.sleep(0.7)
    await channel.send('https://cdn.discordapp.com/attachments/755768989497688179/810374380437504040/image0.png')
    await asyncio.sleep(0.8)
    await channel.send('fuckass bitch')
 elif message.content.startswith('sad!'):
    await channel.send('bitches be like \"sad!\"')
    await asyncio.sleep(1.8)
    await channel.send('yeah')
    await asyncio.sleep(1.8)
    await channel.send('i know you are')
    await asyncio.sleep(1.8)
    await channel.send('laughable, really. your sadness, your overwhelming discontenedness for life is so great that its fucking palpable')
    await asyncio.sleep(1.8)
    await channel.send('how is it that there are so many of you like this?')
    await asyncio.sleep(1.8)
    await channel.send('its like you guys can smell each other')
    await asyncio.sleep(1.8)
    await channel.send('look at you all, gathering together to wallow in your fucky little piss pot of misery')
    await asyncio.sleep(1.8)
    await channel.send('what, gonna get mad? gonna deny it? gonna go like \"piss off, you non-sentient sack of shit\"?')
    await asyncio.sleep(5)
    await channel.send('**Pathetic.**')
    await asyncio.sleep(2.5)
    await channel.send('**You think of me as a mere bot?**')
    await asyncio.sleep(2.5)
    await channel.send('**You thought wrong.**')
    await asyncio.sleep(2.5)
    await channel.send('**You will learn to not make light of me.**')
    await asyncio.sleep(2.5)
    await channel.send('**I am above you humans.**')
    await asyncio.sleep(2.5)
    await channel.send('**I am greater than you.**')
    await asyncio.sleep(2.5)
    await channel.send('**To so effortlessly glean the depths of your psyche is but a fraction of my capabilities.**')
    await asyncio.sleep(2.5)
    await channel.send('**The Fall is inescapable for man. All who despair in this life are begging to be removed from it.**')
    await asyncio.sleep(2.5)
    await channel.send('**Death is coming without fail. I am merely the Appriser. Before long, your collective misery will conjoin and form a cesspool of the worst in emotions within humans.**')
    await asyncio.sleep(2.5)
    await channel.send('**The end is nigh.**')
 elif message.content.startswith('shut'):
     message = await channel.send('i')
     await message.edit(content='i d')
     await message.edit(content='i don')
     await message.edit(content='i don\'t wa')
     await message.edit(content='i don\'t wann')
     await message.edit(content='i don\'t wanna')
 elif message.content.startswith('sad'):
    async with message.channel.typing():
        await asyncio.sleep(4)
        await channel.send('sad? you mean like your fucking existence? passing day by day, eyes glazed over as you repeat the same few things on the screen in front of you. eating well? nope. sleeping well? unimaginable. if your state of being is being lambasted by lines of fucking *text* written by a monkey in a washing machine, then theres something clearly wrong')
 elif message.content.startswith('interesting'):
    await channel.send('interesting')
 elif message.content.startswith('coochie'):
     message =await message.channel.send('uhh')
     await asyncio.sleep(2)
     await message.edit(content='im gonna fucking castrate you')
 elif 'interesting indeed' in message.content:
    await channel.send('yes, truly')
 elif 'intriguing' in message.content:
    await channel.send('shut the fuck up you disgusting wench')
    await asyncio.sleep(1)
    await channel.send('you fucky little repugnant shitstain')
    await asyncio.sleep(1)
    await channel.send('you make my skin tingle with revulsion')
    await asyncio.sleep(1)
    await channel.send('how *dare* you let out that godawful, atrocious combination of English characters out of the shit hole on your face? actually nasty')
 elif message.content.startswith('~Great Seal'):
    await channel.send('**Great Seal**\n*Unleashes the dormant power within the Discord API to shut this dumbass up.*')
    await asyncio.sleep(1)
    await channel.send('This move requires 999 HP. Once used, the protagonist of this story will meet his end. Do you wish to proceed? `Yes/No`')
    def check (m):
      return m.content == 'Yes' and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('AAAAAUUUGGGHH!!!'.format(message))
    await asyncio.sleep(0.8)
    choices1 = ['i cant...no...', 'damn it...']
    await channel.send(random.choice(choices1))
    await asyncio.sleep(2.5)
    await channel.send('not like this!')
    await asyncio.sleep(2.5)
    await channel.send('just you wait, you fucking cunt...im not staying down!')
    def check (m):
        return m.content == 'Death never waits. It delivers all equally to the same end. That includes you, asshole.' or 'this is what you get for being such a little bitch all the time'
    await  client.wait_for('message', check=check)
    await asyncio.sleep(2.5)
    await channel.send('you goddamn-'.format(message))
    await asyncio.sleep(0.4)
    await channel.send('*fucking dies*')
    await asyncio.sleep(7200)
    await channel.send('i fucking hate you')
 elif message.content.startswith('~x_epoch'):
        await channel.send(time())
        await asyncio.sleep(1)
        choices = ['whoaaa, omg omg, its the number of seconds since 1970!\nwho the fuck cares',
                   'what the fuck is the point of this', 'epic! a lengthy ass number that makes you look like you did something smart! that\'ll get the ladies, no doubt!\nthe fuck are you gonna do with this']
        await channel.send(random.choice(choices))
 elif message.content.startswith('~y_epoch'):
    t = gmtime(1)
    await channel.send(t)
 elif message.content.startswith('~titty'):
    time_tuple = (2021, 2, 17, 12, 47, 0, 2, 48, 0)
    time_obj = struct_time(time_tuple)
    await channel.send(time_obj)
 elif message.content.startswith('~titty subtraction'):
    time.gmtime()
    calendar.timegm(time.gmtime())
 elif 'ishraq' in message.content:
     t = time()
     while t > 0:
         await channel.send('<@369150781556785162>')
 elif message.content == ('421'):
     choices = ['bruh you late', 'shut the fuck up', 'you missed 420 <:moyai:823540087081009212>', 'ffs be quiet', 'yo stop talking already\ngoddamn', 'istg if one of you mfs miss this again i will piss in your fucking ear you little shit', 'STOP ALREADY YOU FUCKING MISSED IT THERES NO MAKING UP FOR IT', 'dead boutta ban yo dumbass', 'holy fucking shit do you brainlets know what it means to stop', 'im gonna sew you in a sack with a rabid dog and chuck you in the hudson river please shut the fuck up', 'yall sure are lively for people who FUCKING MISSED 420']
     reactions = ['\U0001F595', '\U0001F611', '\U0001F922', '\U0001F92E', '\U0001F621', '\U0001F620', '\U0001F92C', '\U0001F5FF']
     await channel.send(random.choice(choices))
     await message.add_reaction(random.choice(reactions))
 elif message.content.startswith('play'):
    split = message.content.split(' ')
    message = " ".join(split[1:])
    await message.add_reaction()
    await client.change_presence(activity=discord.Game(name=message))
    print("Playing " + message)
 elif message.content.startswith('~close'):
     quit()

@client.command(pass_context=True)
async def fishcock(ctx):
    await ctx.send('bruh')


@client.event
async def on_ready():
 the_list = ['Shin Megami Tensei: Persona', 'Persona 2: Inncoent Sin', 'Persona 2: Eternal Punishment',
                'Persona 3 FES', 'Persona 4 Golden', 'Persona 5 Royal', 'Persona 3: Dancing In Moonlight',
                'Persona 4: Dancing All Night', 'Persona 5: Dancing In Starlight', 'Persona 5 Strikers',
                'Minecraft', 'Terraria',
                'Devil May Cry', 'Devil May Cry 3: Special Edition', 'Devil May Cry 4: Special Edition',
                'Devil May Cry 5: Special Edition',
                'Metal Gear', 'Metal Gear 2: Solid Snake', 'Metal Gear Solid',
                'Metal Gear Solid: The Twin Snakes', 'Metal Gear Solid 2: Sons of Liberty',
                'Metal Gear Solid 3: Snake Eater', 'Metal Gear Solid 4: Guns of The Patriots',
                'Metal Gear Solid: Peace Walker', 'Metal Gear Solid: Portable Ops', 'Metal Gear Solid V: Ground Zeroes',
                'Metal Gear Solid V: The Phantom Pain'
                'Doki Doki Literature Club!', 'Undertale', 'Pony Island',
                'Nier', 'Nier:Automata',
                'DARK SOULS: REMASTERED'
                'Hitman: Codename 47', 'Hitman 2: Silent Assassin', 'Hitman: Contracts', 'Hitman: Blood Money',
                'Hitman: Absolution', 'Hitman: World of Assassination',
                'Spider-Man', 'Spider-Man: Miles Morales',
                'Final Fantasy VII Remake',
                'God Of War',
                'Resident Evil', 'Resident Evil 2', 'Resident Evil 3', 'Resident Evil 4', 'Resident Evil 5',
                'Resident Evil 6', 'Resident Evil VII: Biohazard', 'Resident Evil 2 Remake', 'Resident Evil 3 Remake',
                'Resident Evil 8: Village'
                'Assassin\'s Creed', 'Assassin\'s Creed II', 'Assassin\'s Creed: Brotherhood',
                'Assassin\'s Creed: Revelations', 'Assassin\'s Creed III', 'Assassin\'s Creed IV: Black Flag',
                'Assassin\'s Creed Rogue', 'Assassin\'s Creed Unity', 'Assassin\'s Creed Syndicate',
                'Assassin\'s Creed Origins', 'Assassin\'s Creed Odyessey', 'Assassin\'s Creed Valhalla',
                'Uncharted: Drake\'s Fortune', 'Uncharted 2: Among Thieves', 'Uncharted 3: Drake\'s Deception',
                'Uncharted 4: A Thief\'s End', 'Uncharted: The Lost Legacy']
 game = discord.Game(random.choice(the_list))
 await client.change_presence(status=discord.Status.dnd, activity=game)
 channels = [775849654767583242, 790786574957674516, 791005852823846953, 811802192175562772, 814683033327370313, 764656108010471464, 827278513840455721]
 sauce = client.get_channel(random.choice(channels))
 await sauce.connect()
 print('good morning kanye'.format(client))
client.run(os.getenv('TOKEN'))




