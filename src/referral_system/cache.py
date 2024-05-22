from typing import Optional

from django.core.cache import cache


def create(key: str, val: str) -> None:
    cache.set(key, val, timeout=1800)


def get(key: str) -> Optional[str]:
    return cache.get(key)


def delete(key: str) -> None:
    cache.delete(key)
