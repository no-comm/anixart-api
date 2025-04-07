from utils.BaseAPI import API

class Collection(API):
    def __init__(self, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/collection/all', token, sign)
    
    def collection_all(self, page=0, previous_page=-1, where=1, sort=2):
        return self._get(f'/{page}?previous_page={previous_page}&where={where}&sort={sort}')
    
    def release(self, release_id, page=0, sort=1):
        return self._get(f'/release/{release_id}/{page}?sort={sort}')
    
    def profile(self, profile_id, page=0):
        return self._get(f'/profile/{profile_id}/{page}')
    