from telethon import TelegramClient, events

from db.relational.dals import TG_DAL
from parsers.tg import classes_dct

import logging

class Our_tg_client:
    path = "app/db/relational/jsons"
    classes_dct = classes_dct

    def __init__(self):
        self.dal = TG_DAL(path_to_folder=self.path)
        self.log = logging.getLogger()

    def set(self):
        data = self.dal.get_api_keys()

        self.links_dct = self.dal.get_tg_channels()
        api_id, api_hash = data['api_id'], data['api_hash']
        
        self.client = TelegramClient('casino_listener', api_id, api_hash)

        for k in self.links_dct:
            channel_link = self.links_dct[k]

            if k not in self.classes_dct:
                self.log.warning(f'class to "{k}" not exist')
                continue

            our_class = self.classes_dct[k]
            
            @self.client.on(events.NewMessage(chats=channel_link))
            async def newMessageListener(event):
                new_message = event.message
                our_class().work(new_message)

    def run(self, debug:bool=False, message_number:int=None, channel_name:str=None):
        with self.client:

            if not debug:
                self.client.run_until_disconnected()
            else:
                for i, message in enumerate(self.client.iter_messages(self.links_dct[channel_name])):
                    if i+1 == message_number:
                        classes_dct[channel_name]().work(message=message)
                        break