from parsers.api_client import ApiClient
import clipboard

class Limon(ApiClient):
    def work(self, message): 
        print(message.message)

        for e in message.entities:
            print(e)