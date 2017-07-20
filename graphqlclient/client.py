import json
import requests


class GraphQLClient:
    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def _send(self, query, variables):
        data = {
            'query': query,
            'variables': variables
        }

        headers = {
            'Content-Type': 'application/json',
            'X-Application-Key': self.key,
        }

        req = requests.post(self.endpoint, data=json.dumps(data), headers=headers)

        return req
