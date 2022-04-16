import telebot
import os
import imageio
from makepng import makepng
import subprocess as sp

bot = telebot.TeleBot('2080386653:AAG13KOCzEIYQunjwQwyix_Xrl0idoCaJWo')
def makegif(list=[],duration=5):
    makepng(list)
    strout = []
    flist = []
    for i in list:
        i = f'Images\\{i}.png'
        flist.append(i)
    list = flist
    for i in range(len(list)):
        for _ in range(int(duration)):
            strout.append(list[i])
    images = []
    for filename in strout:
        images.append(imageio.imread(filename))
    imageio.mimsave('Images\\result.gif', images)
    os.chdir('Images\\')
    for img in os.listdir():
        if img.endswith('g') and img != "blank.png":
            sp.run(f'DEL "{img}"',shell=True)
    os.chdir('..')

@bot.message_handler(commands=['start'])
def startcom(message):
    bot.reply_to(message=message, text="""
Use:
/makegif
{word}
{time} #default is 20

/test
#returns a test image 
    """)

@bot.message_handler(commands=['makegif'])
def test(message):
    try:
        inpt = (str(message.text).split('\n')[1])
        makepng(list(inpt))
    except IndexError:
        bot.reply_to(message=message,text="""
Usage:
/makegif
{string}
{duration} #default duration is 5
        """)
    try:
        inpt2 = str(message.text).split('\n')[2]
        int(inpt2)
        if inpt != "♦":
            bot.reply_to(message=message, text="Making gif...")
        makegif(list(inpt), duration=inpt2)
        bot.send_animation(message.chat.id, open('Images\\result.gif', 'rb'))
    except IndexError:
        if inpt != "♦":
            bot.send_message(message.chat.id,text='You can specify duration at the 3rd line')
        inpt2 = 5
        if inpt != "♦":
            bot.reply_to(message=message, text="Making gif...")
        makegif(list(inpt), duration=inpt2)
        bot.send_animation(message.chat.id, open('Images/result.gif', 'rb'))
    except ValueError:
        bot.send_message(message.chat.id,text='Please use an integer(number) as duration.')
    

@bot.message_handler(commands=['test'])
def test(message):
    makegif('test')
    bot.send_animation(message.chat.id, open('Images\\result.gif', 'rb'))

print("Bot Started")
bot.polling(none_stop=True,timeout=None)