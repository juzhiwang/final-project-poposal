

import discord     
from discord.ext import commands


TOKEN = "OTYxNDY2ODQ1NTc0MDkwNzU0.Yk5Zxw.QtYbthJ_yAnnnam7zsqXCvnVhIw"

client = discord.Client()
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print("hello We are {0.user}".format(client))
    

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    _ =  {"1":"dagger",'2':'Straight Sword','3':'Curved Sword','4':'knife','5':'Bayonet','6':'club','7':'Extra large weapons','8':'Special Weapons'}
    print(f'{username}:{user_message}({channel})')
    

    if message.author == client.user:
        return

    if message.channel.name == '恶魂':
        
        
        if user_message.lower() == 'start':
            await message.channel.send(f'what do you want to know {username}?')
            
            await message.channel.send(f'This is an elden ring weapon recommand bot, choose kind of items you want to know about{_}\n')
            return
        elif user_message.lower() == 'end':
            await message.channel.send(f"I hope you like your trip in Fromsoftware Game {username}.")
            return
        elif user_message.lower() == 'whoismalenia':
            await message.channel.send(f"Harlem's wife")
            return
        elif user_message.lower() == '!dagger':
            await message.channel.send(f'匕首:剑身短小而又笔直的短剑，致命一击的效果不错\n  慈悲短剑：过去战场医生所使用的短剑，锋利而又笔直，致命一级格外亮眼.医疗以慈悲为本')
            return
        elif user_message.lower() == '!straightsword':
            await message.channel.send(f'长剑：具有笔直剑身的双刃直剑')
            await message.channel.send(f'仪式直剑：参考古老仪式杖制成的细身直剑，黄金一族的后裔们，渴求着力量和缘分')
            await message.channel.send(f'夜与火之剑：传说中的武器之一，魔法师的前身----观星者之始，就在离天空最近的高山山顶，据说火焰巨人与之比邻')

            return
        elif user_message.lower() == '!curvedsword':
            await message.channel.send(f'短弯刀:刀身弯曲的单刃曲剑，对上坚硬铠甲的敌人效果不佳，但能以小而快的优势撕裂敌人')
            await message.channel.send(f'剥尸曲剑：具有锯齿状剑锋的曲剑，剑锋参差不齐也凹凸不平，还布满难请的血液----生命也有如此不详的一面吗')
            return
        elif user_message.lower() == '!knife' :
            await message.channel.send(f'打刀：刀身长而弯曲，锋利的单刃剑，芦苇之地武士们持有的出血武器')
            await message.channel.send(f'长牙：刀身非常长，令人畏惧的刀，血指猎人尤拉的武器')
            return
        elif user_message.lower() == '!club':
            await message.channel.send(f'棍棒：厚实的短木棒，不求灵巧的打击类武器')
            
            return
        elif user_message.lower() == '!extralargeweapon':
            await message.channel.send(f'基萨的刺轮：在轮子外围排满刀刃，用来撕裂皮肤的大刺轮，后来经过改良安装至少女人偶成为人偶的象征性武器')
            await message.channel.send(f'巨剑：巨大而又粗犷的铁块剑，超越人类挥舞极限的武器，也因此能用来斩杀非人之物')
            return
        elif user_message.lower() == '!bayonet':
            await message.channel.send(f'细剑：细长又尖锐的剑适用于突刺攻击，能在持盾状态下进行攻击')
            await message.channel.send(f'鲜血旋流：鲜血王朝的仪式剑，附有导血槽')
            return
        elif user_message.lower() == '!speaical weapon':
            await message.channel.send(f'维克的战矛：圆桌骑士维克的武器，与维克同样受到癫火折磨，由内而外收到燃烧')
            await message.channel.send(f'霍斯劳花瓣鞭：名门霍斯劳的传承物品，需要超高灵巧才能会晤，引发敌人大量出血，霍斯劳以血代言')
            return
        
        elif user_message.lower() in '1234567890':
            await message.channel.send(f'please used !weapenkind to check more information')
            return
        else:
            await message.channel.send(f'This bot is still develope 开发中，敬请见证')
        
        
        if user_message.lower() == 'way':
            await message.channel.send('请在服务器《恶魂》里发言')
            return
        
        
        



    

    





client.run(TOKEN)