import os
import subprocess as sp
f = open('api','w+')
api_key = input('API:')
f.write(api_key)
os.system("pip install imageio telebot PyTelegramBotAPI pillow")
