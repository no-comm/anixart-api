from utils.BaseAPI import API

class Release(API):
    def __init__(self, release_id, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/release', token, sign)
        self.release_id = release_id
        
        # Основные поля релиза
        self.id = None
        self.poster = None
        self.image = None
        self.year = None
        self.genres = None
        self.country = None
        self.director = None
        self.author = None
        self.translators = None
        self.studio = None
        self.description = None
        self.note = None
        self.title_original = None
        self.title_ru = None
        self.title_alt = None
        self.episodes_released = None
        self.episodes_total = None
        self.release_date = None
        self.duration = None
        self.season = None
        self.rating = None
        self.grade = None
        self.is_adult = None
        self.is_play_disabled = None
        self.age_rating = None
        
        # Статистика
        self.vote_1_count = None
        self.vote_2_count = None
        self.vote_3_count = None
        self.vote_4_count = None
        self.vote_5_count = None
        self.vote_count = None
        self.favorites_count = None
        self.watching_count = None
        self.plan_count = None
        self.completed_count = None
        self.hold_on_count = None
        self.dropped_count = None
        
        # Даты
        self.creation_date = None
        self.last_update_date = None
        self.aired_on_date = None
        
        # Связанные объекты
        self.related = None
        self.category = None
        self.status = None
        
        # Медиа
        self.screenshots = []
        self.screenshot_images = []
        self.video_banners = []
        self.comments = []
        
        # Пользовательские данные
        self.your_vote = None
        self.profile_list_status = None
        self.status_id = None
        self.last_view_timestamp = None
        self.last_view_episode = None
        self.is_viewed = None
        self.is_favorite = None
        
    def load(self):
        """Загружает данные релиза из API"""
        response = self._get(f'/{self.release_id}')
        if response and 'release' in response:
            self._update_from_json(response['release'])
    
    def _update_from_json(self, json_data: dict):
        """Обновляет атрибуты класса из JSON-данных"""
        for key, value in json_data.items():
            if key in ['related', 'category', 'status']:
                if value is not None:
                    setattr(self, key, value)
                continue
                
            if key in ['screenshots', 'screenshot_images', 'video_banners', 'comments']:
                if value is not None:
                    setattr(self, key, value or [])
                continue
                
            if hasattr(self, key):
                setattr(self, key, value)
    
    def refresh(self):
        """Обновляет данные релиза (синоним для load)"""
        self.load()
    
    def comment_all(self, page=0, sort=1):
        return self._get(f'/comment/all/{self.release_id}/{page}?sort={sort}')
    
    def comment(self, comment_id):
        return self._get(f'/comment/{comment_id}')
    
    def comment_replies(self, comment_id, page=0, sort=2):
        return self._get(f'/comment/replies/{comment_id}/{page}?sort={sort}')