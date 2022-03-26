
# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import GetContactsRequest
  
# get your api_id, api_hash, token
# from telegram as described above
api_id = '19304238'
api_hash = '99a300d51caa08a3a9fa0dc179846f05'
token = '5218323126:AAFcF7-xZ0tYNiHi-kqugiioJGAIRZYNCCU'
message = "ALERT"
 
# your phone number
phone = '+91 9999906505'
  
# creating a telegram session and assigning
# it to a variable client





client = TelegramClient('session', api_id, api_hash)

contacts = client(GetContactsRequest(0))
print(contacts)
  
# connecting and building the session
client.connect()
 
# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():
  
    client.send_code_request(phone)
     
    # signing in the client
    client.sign_in(phone, input('Enter the code: '))

    try :
        for u in contacts.users :
            client.send_message(InputPeerUser(u.id , u.access_hash),"test")
    except Exception as e :
        print(e)  
  
'''try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    receiver = InputPeerUser('user_id', 'user_hash')
 
    # sending message using telegram client
    client.send_message(receiver, message, parse_mode='html')
except Exception as e:
     
    # there may be many error coming in while like peer
    # error, wrong access_hash, flood_error, etc
    print(e);'''
 
# disconnecting the telegram session
client.disconnect()

