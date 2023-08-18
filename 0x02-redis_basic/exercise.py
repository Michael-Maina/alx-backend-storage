#!/usr/bin/env python3
"""
Cache class module
"""
import redis
from typing import Callable, Optional, Union
from uuid import uuid4


class Cache():
    """
    Caching class implementation with Redis
    """
    def __init__(self):
        """
        Initializes the a Redis instance and flushes all keys
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores input data in Redis using the random key
        and returns the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> (
            Union[str, bytes, int, float]
    ):
        """
        Overrides Redis.get() method
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Parameterizes the Cache.get() fn to convert value to a string
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """
        Parameterizes the Cache.get() fn to convert value to an integer
        """
        return self.get(key, fn=int)
