import json
import requests


class GraphQLClient:
    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def _send(self, query, variables):

        # Encode the variables if needed
        try:
            variables.decode()
        except AttributeError:
            variables = json.dumps(variables)

        data = {
            'query': query,
            'variables': variables
        }

        headers = {
            'Content-Type': 'application/json',
            'X-Application-Key': self.key,
        }

        res = requests.post(self.endpoint, json=data, headers=headers)

        return res.json()
