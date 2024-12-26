from db.relational.dals import TG_DAL

import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)



from array import array

import os
import io

import PIL.Image as Image

path = "app/db/relational"
data = TG_DAL()._get_api_keys(path_to_file=path)
api_id, api_hash = data['api_id'], data['api_hash']
client = TelegramClient('anon', api_id, api_hash)


input_channel = "https://t.me/+gImjQuW52AZiMzZi"
@client.on(events.NewMessage(chats=input_channel))
async def newMessageListener(event):
    # Get message text
    newMessage = event.message.message
    print(newMessage)
    # # Apply 1st round of Regex for Subject for current messageContent - return list of keywords found (case-insensitive)
    # subjectFiltered = re.findall(r"(?=("+'|'-join(subjectFilter)+r"))", newMessage, re. IGNORECASE)
    # if len(subjectFiltered) != 0:
    #     # Apply 2nd round of Regex for Level
    #     levelFiltered = re.findall(r"(?=("+'|'-join(levelFilter)+r"))", newMessage, re. IGNORECASE)
    # if len(levelFiltered) != 0:
    #     await client.forward_messages(entity='me', messages=event.message)




from telethon import functions, types

chat = 'https://t.me/atompromo'
with client:
    # client.run_until_disconnected()

    for message in client.iter_messages(chat):
        for e in message.entities:
            
            print(e)

        break


    # result = client(functions.messages.GetCustomEmojiDocumentsRequest(
    #     document_id=[5332587336939084375]
    # ))
    
    # for x in result:
    #     print(x.thumbs[0])
        
    #     # stream = io.BytesIO(x.thumbs[0].bytes)
    #     # byte_data = b'\xFF\xD8\xFF\xE0...\xFF\xD9'  # JPEG byte header and footer
    #     # with open('output.jpg', 'wb') as file:
    #     #     file.write(x.thumbs[0].bytes)

    #     import cv2
    #     import numpy as np

    #     # assume 'image_bytes' is a bytes object containing image data
    #     image_bytes = x.thumbs[0].bytes

    #     nparr = np.frombuffer(image_bytes, np.uint8)
    #     image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #     cv2.imwrite('output_image.jpg', image)

    #     # y = x.attributes[1].stickerset
    #     # result = client(functions.messages.GetStickerSetRequest(
    #     # stickerset=types.InputStickerSetID(
    #     #     id=y.id,
    #     #     access_hash=y.access_hash
    #     # ),
    #     # hash=0
    #     # ))
    #     # print(result)

    #     break

