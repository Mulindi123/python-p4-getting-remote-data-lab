import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

    def load_json(self):
        items_list = []
        items = json.loads(self.get_response_body())
        for item in items:
            items_list.append(item)

        return items_list
    
request = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
parsed_data = request.load_json()
for info in (parsed_data):
    print(info)