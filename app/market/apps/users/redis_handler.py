from typing import Union, Optional

from django_redis import get_redis_connection
import json
from redis import Redis
from django.conf import settings


class RedisHandler():
    KEY_LOGIN_DOWNTIME = 'login_downtime'
    KEY_ADMIN_LOGIN_DOWNTIME = 'admin_login_downtime'

    def __init__(self):
        self.redis: Redis = get_redis_connection()
        # self.redis.delete('sum_withdraw_with_check_btc')

    def get(self, key: str) -> Optional[str]:
        if value := self.redis.get(key):
            return value.decode('utf-8')
        return None

    def set(self, key: str, value: Union[str, int, float]):
        return self.redis.set(key, value)

    def lpush(self, key: str, *values):
        return self.redis.lpush(key, *values)

    def lrange(self, key: str, start: int, end: int) -> Optional[dict]:
        if values := self.redis.lrange(key, start, end):
            for value in values:
                str_value = value.decode("utf-8").replace("'", '"')
                json_value = json.loads(str_value)
                return json_value
        return None

    def get_login_downtime(self) -> int:
        if login_downtime := self.get(self.KEY_LOGIN_DOWNTIME):
            return int(login_downtime)
        self.set(self.KEY_LOGIN_DOWNTIME, int(settings.LOGIN_DOWNTIME))
        return settings.LOGIN_DOWNTIME

    def get_admin_login_downtime(self) -> int:
        if admin_login_downtime := self.get(self.KEY_ADMIN_LOGIN_DOWNTIME):
            return int(admin_login_downtime)
        self.set(self.KEY_ADMIN_LOGIN_DOWNTIME, int(settings.ADMIN_LOGIN_DOWNTIME))
        return settings.ADMIN_LOGIN_DOWNTIME

