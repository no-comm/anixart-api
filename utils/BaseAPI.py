from requests import Session

class API:
    def __init__(self, base_url, token=None, sign=None) -> None:
        self.params = {}
        if token:self.params['token']=token
        self.session = Session()
        self.session.params = self.params
        self.session.headers = {
            'Host': 'api-s4.anixart.tv',
            'user-agent': 'AnixartApp/8.2.3-24111318 (Android 13; SDK 33; arm64-v8a; Xiaomi 2109119DG; ru)',
            'sign': sign if sign else ''
        }
        self.base_url = base_url

    def _get(self, url, *args, **kwargs):
        res = self.session.get(self.base_url+url, *args, **kwargs)
        return res.json()

    def _post(self, url, *args, **kwargs):
        res = self.session.post(self.base_url+url, *args, **kwargs)
        return res.json()