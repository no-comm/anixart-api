from utils.BaseAPI import API

class Profile(API):
    def __init__(self, profile_id, token=None, sign=None) -> None:
        super().__init__('https://api-s4.anixart.tv/profile', token, sign)
        self.profile_id = profile_id
        
        # Основная информация
        self.id = None
        self.login = None
        self.avatar = None
        self.status = None
        self.badge = None
        
        # История просмотров и оценки
        self.history = []
        self.votes = []
        
        # Статистика активности
        self.last_activity_time = None
        self.register_date = None
        self.watching_count = None
        self.plan_count = None
        self.completed_count = None
        self.hold_on_count = None
        self.dropped_count = None
        self.favorite_count = None
        self.comment_count = None
        self.collection_count = None
        self.video_count = None
        self.friend_count = None
        self.subscription_count = None
        self.watched_episode_count = None
        self.watched_time = None
        
        # Социальные сети
        self.vk_page = None
        self.tg_page = None
        self.inst_page = None
        self.tt_page = None
        self.discord_page = None
        
        # Статусы и блокировки
        self.ban_expires = None
        self.ban_reason = None
        self.privilege_level = None
        self.is_private = None
        self.is_sponsor = None
        self.is_banned = None
        self.is_perm_banned = None
        self.is_vk_bound = None
        self.is_google_bound = None
        self.is_verified = None
        
        # Настройки уведомлений
        self.is_release_type_notifications_enabled = None
        self.is_episode_notifications_enabled = None
        self.is_first_episode_notification_enabled = None
        self.is_related_release_notifications_enabled = None
        
        # Динамика просмотров
        self.watch_dynamics = []
        
        # Дополнительные поля
        self.rating_score = None
        self.is_blocked = None
        self.is_stats_hidden = None
        self.is_counts_hidden = None
        self.is_social_hidden = None
        self.is_friend_requests_disallowed = None
        self.roles = []
    
    def load(self):
        """Загружает данные профиля из API и заполняет атрибуты класса"""
        response = self._get(f'/{self.profile_id}')
        if response:
            self._update_from_json(response['profile'])
    
    def _update_from_json(self, json_data: dict):
        """Обновляет атрибуты класса из JSON-данных"""
        for key, value in json_data.items():
            # Обработка вложенных объектов
            if key in ['friend_status']:
                if value is not None:
                    setattr(self, key, value)
                continue
                
            # Обработка списков
            if key in ['history', 'votes', 'watch_dynamics', 'roles']:
                if value is not None:
                    setattr(self, key, value or [])
                continue
                
            # Для всех остальных полей
            if hasattr(self, key):
                setattr(self, key, value)
    
    def refresh(self):
        """Обновляет данные профиля"""
        self.load()
    
    def friend_all(self, page=0):
        return self._get(f'/friend/all/{self.profile_id}/{page}')
    
    def vote_release_voted(self, page=0, sort=1):
        return self._get(f'/vote/release/voted/{self.profile_id}/{page}?sort={sort}')
    
    def login_history(self, page=0):
        return self._get(f'/login/history/all/{self.profile_id}/{page}')