from utils.BaseAPI import API

class Schedule(API):
    def __init__(self, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/schedule', token, sign)
    
    def schedule(self):
        return self._get('')