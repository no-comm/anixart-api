from utils.BaseAPI import API

class Search(API):
    def __init__(self, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/search', token, sign)
    
    def releases(self, query, page):
        return self._post(f'/releases/{page}', json={"query":query,"searchBy":0})
    
    def profiles(self, query, page):
        return self._post(f'/profiles/{page}', json={"query":query,"searchBy":0})