from utils.BaseAPI import API

class Discover(API):
    def __init__(self, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/discover', token, sign)
    
    def comments(self):
        return self._get('/comments')
    
    def watching(self, page):
        return self._get(f'/watching/{page}')
    
    def discussing(self):
        return self._get('/discussing')
    
    def interesting(self):
        return self._get('/interesting')
    