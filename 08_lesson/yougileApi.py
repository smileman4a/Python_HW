import requests
from config import config


class yougileAPI:

    def __init__(self, url=config.BASE_URL):
        self.url = url

    def get_company_id(self, user=config.USER, pwd=config.PWD):
        body = {
            "login": user,
            "password": pwd
        }
        resp = requests.post(self.url + "api-v2//auth/companies", json=body)
        return resp.json()["content"][0]["id"]

    def get_token(self, user=config.USER, pwd=config.PWD):
        id = self.get_company_id(user, pwd)
        body = {
            "login": user,
            "password": pwd,
            "companyId": id
        }
        resp = requests.post(self.url + "api-v2/auth/keys",
                             json=body)
        config.TOKEN = resp.json()["key"]
        return config.TOKEN

    def get_token_list(self, user=config.USER, pwd=config.PWD):
        id = self.get_company_id(user, pwd)
        body = {
            "login": user,
            "password": pwd,
            "companyId": id
        }
        resp = requests.post(self.url + "api-v2/auth/keys/get",
                             json=body)
        return resp.json()

    def delete_token(self, token):
        resp = requests.delete(f"{self.url}/api-v2/auth/keys/{token}")
        return resp.json()

    def create_project(self, title, token=config.TOKEN):
        headers = {
            "Authorization": "Bearer " + str(token)
        }
        body = {
            "title": title
        }
        resp = requests.post(
            self.url + '/api-v2/projects', json=body, headers=headers
        )
        return resp

    def get_project_by_id(self, id, token=config.TOKEN):
        headers = {
            "Authorization": "Bearer " + str(token)
        }
        resp = requests.get(f"{self.url}/api-v2/projects/{id}",
                            headers=headers)
        return resp.json()

    def update_project(self, id, title, token=config.TOKEN, deleted=False):
        headers = {
            "Authorization": "Bearer " + str(token)
        }
        body = {
            "deleted": deleted,
            "title": title
        }
        resp = requests.put(f"{self.url}/api-v2/projects/{id}",
                            json=body, headers=headers)
        return resp
