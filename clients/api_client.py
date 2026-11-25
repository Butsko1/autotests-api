import httpx

class APIClient:
    def __init__(self, client: httpx.Client):
        self.client = client

    def get(self, url, params=None):
        return self.client.get(url=url, params=params)

    def post(self, url, json = None, data=None, files = None):
        return self.client.post(url=url, json=json, data=data, files=files)

    def patch(self, url, json=None, params = None):
        return self.client.patch(url=url, json=json, params=params)

    def delete(self, url, params=None):
        return self.client.delete(url=url, params=params)