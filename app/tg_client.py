from telethon import TelegramClient, events

from db.relational.dals import TG_DAL


class Our_tg_client:
    path = "app/db/relational/jsons"

    def __init__(self):
        self.dal = TG_DAL(path_to_folder=self.path)

    def set(self):
        data = self.dal.get_api_keys()

        links_dct, classes_dct = self._get_data()
        api_id, api_hash = data['api_id'], data['api_hash']
        
        self.client = TelegramClient('anon', api_id, api_hash)

        for k in links_dct:
            channel_link, our_class = links_dct[k], classes_dct[k]
            
            @self.client.on(events.NewMessage(chats=channel_link))
            async def newMessageListener(event):
                newMessage = event.message.message
                print(newMessage)

    def run(self):
        with self.client:
            self.client.run_until_disconnected()
    
    def _get_data(self):
        return [{"dima": "https://t.me/+gImjQuW52AZiMzZi"}, {"dima": None}]
