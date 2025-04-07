from utils.BaseAPI import API

class Filter(API):
    def __init__(self, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/filter', token, sign)
    
    def filter(self, query, page):
        '''{"country":null,"season":null,"sort":0,"studio":null,"age_ratings":[],"category_id":null,"end_year":null,"episode_duration_from":null,"episode_duration_to":null,"episodes_from":null,"episodes_to":null,"genres":[],"profile_list_exclusions":[],"start_year":null,"status_id":null,"types":[143],"is_genres_exclude_mode_enabled":false}'''
        return self._post(f'/{page}', json=query)
    