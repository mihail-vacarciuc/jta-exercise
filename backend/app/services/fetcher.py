import httpx
import os
from datetime import datetime, timedelta
from pydantic import ValidationError
from dotenv import load_dotenv
from app.cache import cache, cache_lock
from app.schemas.user import UsersResponseSchema
from app.schemas.product import ProductsResponseSchema

load_dotenv()

USERS_URL = os.getenv("USERS_URL")
PRODUCTS_URL = os.getenv("PRODUCTS_URL")
CACHE_REFRESH_TIME_MIN = 5

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    
    
#chek if cache exist or if it is old (> CACHE_REFRESH_TIME_MIN)
def is_cache_old() -> bool:
    last_updated = cache["last_updated"]
    if  last_updated is None:
        return True
    
    return datetime.now() - last_updated > timedelta(minutes=CACHE_REFRESH_TIME_MIN)


# get cash data if requested
async def get_cache_data (refresh: bool = False):
    # check if cache shall be updated
    if refresh or is_cache_old():
        # ensure that only one request to update/ refresh the cache is running
        async with cache_lock:
            # refresh the cache
            users = await fetch_data(USERS_URL)
            products = await fetch_data(PRODUCTS_URL) 

            valid_users = UsersResponseSchema.model_validate(users)
            valid_products = ProductsResponseSchema.model_validate(products)

            cache["users"] = [u.model_dump(mode= "json") for u in valid_users.users]
            cache["products"] = [p.model_dump(mode= "json") for p in valid_products.products]
            cache["last_updated"] = datetime.now()
        
    return cache