import requests


class BaseApi:
    def __init__(self):
        self.session = requests.Session()
        self.corpid = 'ww9227048f2cac6416'
        self.corpsecret = 'IK1y4HGwTHpxDmn9-4tBcnPn7bvrzhX7eREJdefO6cM'
        self.token_url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}'
        self.token = self.get_token()
        self.session.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)

    def get_token(self):
        # print(f'token_url: {self.token_url}')
        r = requests.get(self.token_url)
        # print(f'token response: {r}')
        token = r.json()['access_token']
        return token
