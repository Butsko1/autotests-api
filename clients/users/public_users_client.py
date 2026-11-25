from clients.api_client import APIClient

class PublicUserClient(APIClient):
    def create_user_api(self, json):
        return self.post('/api/v1/users', json = json)
