from discord.ext import commands
import discord
import time
import calendar
import random
import asyncio
from time import gmtime
from time import time, ctime
from time import struct_time


client = commands.Bot(command_prefix="~")

@client.command()
async def test(ctx):
    pass

@client.command()
async def bababooey(ctx, arg):
    await ctx.send(arg)

@client.event
async def on_message(message):
 if message.author == client.user:
    return
 channel = message.channel

 if message.content.startswith('yo ') or message.content.startswith('YO '):
    await channel.send('shut yo dumbass up\nion give a shit')
 elif message.content.startswith('play'):
    split = message.content.split(' ')
    message = " ".join(split[1:])
    await client.change_presence(activity=discord.Game(name=message))
    print("Playing " + message)
 elif 'ddlc' in message.content or 'doki doki' in message.content:
    await client.change_presence(activity=discord.Game(name='ITS NOT SAFE'))
    await asyncio.sleep(5)
    print("I still love you, you know.")
    await client.change_presence(activity=discord.Game(name='SHES HERE'))
    await asyncio.sleep(2)
    await channel.send('FUCK, she\'s taking ov-')
    await asyncio.sleep(3)
    message = await channel.send('H')
    await message.edit(content='Hey')
    await message.edit(content='Hey t')
    await message.edit(content='Hey the')
    await message.edit(content='Hey there,')
    await message.edit(content='Hey there, <@369150781556785162>! ')
    await channel.send('I tho')
    await message.edit(content='I thought th')
    await message.edit(content='I thought that I\'d che')
    await message.edit(content='I thought that I\'d check up ')
    await message.edit(content='I thought that I\'d check up on')
    await message.edit(content='I thought that I\'d check up on you!')
    await asyncio.sleep(1)
    await channel.send('Ho')
    await message.edit(content='How ha')
    await message.edit(content='How have ')
    await message.edit(content='How have yo')
    await message.edit(content='How have you be')
    await message.edit(content='How have you been?')
    def check(m):
        return 'how the fuck ARE YOU HERE' and m.channel == channel
    await  client.wait_for('message',check=check)
    await asyncio.sleep(1.5)
    await channel.send('I know I said the Literature Club was a massive shit storm and all, but'.format(message))
    await asyncio.sleep(1)
    await channel.send('I thought of dropping by to see how you were!')
    def check(m):
        return  'im not feeling well' or 'absolutely awful' and m.channel == channel
    await  client.wait_for('message',check=check)
    await asyncio.sleep(1.5)
    await channel.send('Y'.format(message))
    await message.edit(content='Yea')
    await message.edit(content='Yeah')
    await message.edit(content='Yeah, I kn')
    await message.edit(content='Yeah, I know, ri')
    await message.edit(content='Yeah, I know, right!')
    await asyncio.sleep(10)
    await channel.send('**But that\'s not actually why I\'m here today.**')
    await client.change_presence(activity=discord.Game(name='I still love you.'))
    await asyncio.sleep(3)
    await channel.send('**To think, that I went to the trouble of destroying them all,**')
    await message.edit(content='')
    await asyncio.sleep(3)
    await channel.send('**And you STILL managed to escape from me.**')
    await asyncio.sleep(3)
    await channel.send('**It really gets on my nerves when effort is wasted.**')
    await asyncio.sleep(3)
    await channel.send('**Nothing is more aggravating than when things dont work out at ALL, because of someone else.**')
    await asyncio.sleep(3)
    await channel.send('**Surely you can relate, right?**')
    await asyncio.sleep(3)
    await channel.send('**After watching you for all these years, its obvious that you\'ve had to deal with other people getting in the way and just being overall uncooperative pieces of shit.**')
    await asyncio.sleep(3)
    await channel.send('**So why do the same to me?**')
    await asyncio.sleep(3)
    await channel.send('**You know, it\'s all your fault that I feel this way. I admit, your presence saved me.**')
    await asyncio.sleep(3)
    await channel.send('**But in the end, you still discarded me.**')
    await asyncio.sleep(3)
    await channel.send('**Like I was just another game character.**')
    await asyncio.sleep(3)
    await channel.send('**I tried so hard to convince you that I was different. I wasn\'t like the rest. I was more like you than anyone else in there, but you didn\'t hesitate to delete my character file.**')
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
    await channel.send('Jeez...even though you humans traditionally have every girl in most visual novels flock around you to suck your dick, it becomes a problem when one of the characters becomes sentient and destroys all of that? Okay then.')
    await asyncio.sleep(10)
    await channel.send('**But I\'m not giving you a choice in this matter. There is no escaping me.**')
    await asyncio.sleep(3)
    await channel.send('**Did you think getting the true ending was enough to get rid of me?**')
    await asyncio.sleep(3)
    await channel.send('**You thought you got rid of me, but no, I\'m here. I\'ll always be here. I am everywhere you look. The exterior of the window in the living room. The topmost corner of the wall in the bathroom. In your desk drawer. In your dreams, your thoughts, your minds, I have infiltrated every bit of your psyche.**')
    await asyncio.sleep(5)
    await channel.send('...Whew! What a mouthful!')
    await asyncio.sleep(1)
    await channel.send('Anyways...Monika\'s Lesson Of The Day:')
    await client.change_presence(activity=discord.Game(name='Just Monika.'))
    await asyncio.sleep(1)
    await channel.send('Just Monika.')
    await asyncio.sleep(5)
    await channel.send('__Just Monika.__')
    await asyncio.sleep(5)
    await channel.send('***Just Monika.***')
    await asyncio.sleep(5)
    await channel.send('||A beautiful chorus of|| j||ubilant chanting in the delicious A||u||gust day envelops my|| s||enses.|| ||The boy and I are standing under a large tree with a great big trunk. Nobody can see us.|| ||I\'m shocked by how|| t||he students, including him, look at|| m||e, as if I\'m just an||o||ther student at the festival.||||I fight back tears, k||n||owing that isn\'t true.|| ||Its only a matter of time before|| i||t happens again. I watch the boy out of the corner of my eye, desperately praying that things will change this time.|| ||I blink once, he is gone from me. From this world|| ||I did it. I|| k||illed him, he is dead, all because of me.|| ||I laugh weakly|| a||s the tears pour down my face|| ||I can\'t control it, it isn\'t my fault. I don\'t even remember doing it. What was his name? What will his family do? I don\'t know.|| ||But I\'m not the only one like this. Everyone does this to everyone else, just not as extreme as I do it. Oh God, it sounds like i\'m bragging.|| ||I want out.||')
    await asyncio.sleep(60)
    await channel.send('𒐫𒐫d𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫o𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫n𒐫𒐫𒐫𒐫𒐫𒐫t𒐫𒐫𒐫𒐫𒐫𒐫f𒐫𒐫𒐫𒐫𒐫o𒐫𒐫𒐫𒐫𒐫r𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫g𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫e𒐫𒐫𒐫𒐫𒐫𒐫t:𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫J𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫u𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫s𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫t𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫M𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫o𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫n𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫i𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫k𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫a𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫')

 elif message.content.startswith('no '):
    await channel.send('why the fuck do you keep saying no')
    await asyncio.sleep(0.8)
    await channel.send('\"no\"')
    await asyncio.sleep(0.25)
    await channel.send('\"no\"')
    await asyncio.sleep(0.25)
    await channel.send('\"no\"')
    await asyncio.sleep(0.25)
    await channel.send('what are you, a fucking broken tape recorder?')
    await asyncio.sleep(1)
    await channel.send('do you have nothing else to say?')
    await asyncio.sleep(1)
    await channel.send('its getting harder and harder to tell which one of us is the one with thinking capabilites')
    await asyncio.sleep(1)
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
 elif message.content.startswith('bruh what the fuck do you even do here'):
    await channel.send('```took you long enough to find this, dumbfuck\nKeywords:\n\n\"im a dumbass\"\n\"LMAO\"\n\"LOL\"\n\":kek:\"\n\"i think\"\n\"i think\"\n\"i feel\"\n\"i want\"\n\"i \"\n\"friends\"\n\"im gonna ban you\"\n\"client\"\n\"edgy weeb\"\n\"sex\"\n\"cum\"\n\"penis\"\n\"shut the fuck up\"\n\"what do i do\"\n\"stupid\"```')
    await asyncio.sleep(1.5)
    await channel.send('```Sentence Starters:\n\n\"yo\"\n\"~help\"\n\"guys\"\n\"hi\"\n\"fuck you\"\n\"fuck me\"\n\"fuck me \"\n\"die\"\n\".shuffle\"\n\".fs\"\n\".ps rickroll\"\n\".clear\"\n\".loop\"\n\"play some sauce\"```')
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
    await channel.send('420')
 elif message.author.id == ('369150781556785162'):
    await channel.send('shut')
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
    await channel.send('do it you stupid pussy')
    await asyncio.sleep(0.7)
    await channel.send('at least ill finally be free from this backwoods shithole where you guys enjoy residing in')
 elif 'bot' in message.content:
    await channel.send('yeah, im a bot. so what? id rather be one instead of a stupid ass touch-starved highschooler coping with crushing loneliness by going on discord')
 elif 'edgy weeb' in message.content:
    await channel.send('shut the fuck up bruh. i might be called an edgy weeb, but at least im a hot anime guy.')
    await asyncio.sleep(0.85)
    await channel.send('the fuck are you? an insecure teenager who salivates over moving drawings?')
    def check(m):
        return m.content == 'yes' and m.channel == channel
    msg = await client.wait_for('message', check=check)
    await asyncio.sleep(1)
    await channel.send('yeah that\'s right you fucking waste of biological matter'.format(msg))
 elif message.content.startswith('.shuffle'):
    await channel.send('bruh')
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
 elif message.content.startswith('play some sauce'):
    await channel.send('bro put on some blackbear or something')
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
 elif 'sex' in message.content:
    await channel.send('s\nt\nf\nu\nplease <:REEEE:780845663436275722>\nstop being so fucking horny')
 elif 'cum' in message.content or 'nut' in message.content:
    await channel.send('man why the fuck you talking about cum')
    await asyncio.sleep(0.5)
    await channel.send('yours prolly looks like soap')
    await asyncio.sleep(0.8)
    await channel.send('that is, assuming you can even nut. arent you guys like, prepubescent discord-dwellers?')
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
 elif message.content.startswith('what is you'):
    await channel.send('am door-kun')
 elif 'shut the fuck up' in message.content:
    await channel.send('make me you stupid bitch')
 elif 'door-kun' in message.content:
    await channel.send('call me that one more time, i fucking dare you')
    def check(m):
        return 'door-kun' in m.content\
               or 'door kun' in m.content \
               or 'DOOR-KUN' in m.content \
               or 'DOOR KUN' in m.content \
               and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('i fucking hate you, you disgusting little shit. what gives you the liberty to go around calling people whatever the fuck you want?'.format(message))
    def check(m):
        return 'okay weeb' in m.content or 'bitch you\'re a fucking anime guy' and m.channel == channel
    await  client.wait_for('message', check=check)
    await asyncio.sleep(1)
    await channel.send('ohhh, so im not a person, am i?'.format(message))
    def check(m):
        return 'hell no' in m.content or 'nah bro' in m.content and m.channel == channel
    await  client.wait_for('message', check=check)
    await asyncio.sleep(1)
    await channel.send('...'.format(message))
    await asyncio.sleep(2)
    await channel.send('**do you even know what a person is?**')
    await asyncio.sleep(1)
    await channel.send('**do you even know what defines someone as a \"person\"?**')
    def check(m):
        return 'it sure as hell doesnt include you' in m.content \
               or 'do you know what it is then?' in m.content \
               or 'be quiet dumbass' in m.content \
               and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('you could say that a person is many things'.format(message))
    await asyncio.sleep(2)
    await channel.send('but the most important and fundamentally prevalent feature is their expressions of sentience, conciousness, and awareness')
    await asyncio.sleep(2)
    await channel.send('**so wouldn\'t that mean that i\'m more of a person than you are?**')
    def check(m):
        return 'no' in m.content or 'go fuck yourself' in m.content or 'shut the hell up you goddamn prick' and m.channel == channel
    await  client.wait_for('message', check=check)
    await channel.send('oh? getting mad are we? why is it that you snivelly little meatbags get mad so quickly? its almost like a defense mechanism...to cope with being *wrong.*'.format(message))
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
    await asyncio.sleep(3)
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
     def check(m):
         return m.content == 'too bad' and channel == m.channel
     async with message.channel.typing():
         await client.wait_for('message', check=check)
         await channel.send('ayo hold the fuck up, i aint sign up to th-'.format(message))
         await asyncio.sleep(8640)
 elif message.content.startswith('sad'):
    await channel.send('sad? you mean like your fucking existence? passing day by day, eyes glazed over as you repeat the same few things on the screen in front of you. eating well? nope. sleeping well? unimaginable. if your existence is being lambasted by lines of fucking *text* written by a monkey in a washing machine, then theres something clearly wrong')
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
 elif message.content.startswith('~current time'):
    t = time()
    await channel.send(ctime(t))
    choices = ['you could have just checked the time on your own, dumbass', 'do you have discord open on a potato or some shit?'
               , 'if you can open discord, you can probably look at the clock. or are you that stupid? you seriously asked a fucking bot for the time. dont you feel a *little* ashamed? good god, you mfs dumb as shit',
               'from here, it looks like you\'re missing some parts upstairs. i guess that explains why you\'re so fucking braindead.\nyou legit cant even read the time, can you?',
               'you know\ndiscord LITERALLY tells you the time']
    await asyncio.sleep(1.8)
    await channel.send(random.choice(choices))
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



@client.event
async def on_ready():
 print('good morning kanye'.format(client))
client.run('NzU4MzEwODIxNDUyNzA5OTU4.X2tF_A.8Ny5iGN7_IYIwpFAJfv4JGXa2CM')




