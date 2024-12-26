from telethon import TelegramClient, events

from db.relational.dals import TG_DAL
from parsers.tg import classes_dct

import logging

class Our_tg_client:
    path = "app/db/relational/jsons"

    def __init__(self):
        self.dal = TG_DAL(path_to_folder=self.path)
        self.log = logging.getLogger()

    def set(self):
        data = self.dal.get_api_keys()

        links_dct = self._get_data()
        api_id, api_hash = data['api_id'], data['api_hash']
        
        self.client = TelegramClient('casino_listener', api_id, api_hash)

        for k in links_dct:
            channel_link = links_dct[k]

            if k not in classes_dct:
                self.log.warning(f'class to "{k}" not exist')
                continue

            our_class = classes_dct[k]
            
            @self.client.on(events.NewMessage(chats=channel_link))
            async def newMessageListener(event):
                new_message = event.message.message
                our_class().work(new_message)

    def run(self):
        with self.client:
            self.client.run_until_disconnected()
    
    def _get_data(self):
        data = self.dal.get_tg_channels()
        return data
