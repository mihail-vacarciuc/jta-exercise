import asyncio

cache = {
    "users": [],
    "products": [],
    "last_updated": None
}

cache_lock = asyncio.Lock()