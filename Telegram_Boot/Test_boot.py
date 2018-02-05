#!/usr/bin/python3

# Acceso a la API telegram con libreria Telepot
# Antes se debe instalar Telepot mediante pip3 en linux

# http://telepot.readthedocs.io/en/latest/

import os
import telepot
import socket
from pprint import pprint
from time import sleep


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

########################################################
##		Función añadir usuarios a lista conectados	  ##
########################################################
def usuario(id):
	global conectados


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print (str(msg['text']))
    if content_type == 'text':
        if msg['text'] == "/ip":
            missatge = "La meva ip local es : " + str(get_ip())
            bot.sendMessage(chat_id, missatge)
        if msg['text'] == "/apaga":
			

###############################################
##    EMPIEZA AQUÍ EL PROGRAMA PRINCIPAL     ##
###############################################
token_gabriel_bot = '368802964:AAFQzUTOsY3NSpw_2YVTBDXeWnAK7R-RGbw'
bot = telepot.Bot(token_gabriel_bot)
conectados = []

bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    sleep(5)
