from fastapi import APIRouter
from app.services.fetcher import  get_cache_data
import statistics

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("")
async def get_products():
    cache = await get_cache_data()
    products = cache["products"]

    return [
        {   "id": p["id"],
            "product": p["title"],
            "brand": p["brand"],
            "category": p["category"],
            "price": p["price"],
            "stock": p["stock"],
            "rating": str(p["rating"]) + ' /5'
        }
        for p in products
    ]

@router.get("/analytics")
async def get_products():
    cache = await get_cache_data()
    products = cache["products"]

    # Brands by Avg rating
    brands_rating = {}
    for p in products:
        brand = p.get("brand")
        brands_rating[brand] = p.get("rating")

    brands_rating = {k: v for k, v in sorted(brands_rating.items(), key=lambda item: item[1])}

    # products by category
    category_counts = {}
    for p in products:
        category = p.get("category")
        category_counts[category] = category_counts.get(category, 0) + 1

    category_counts = {k: v for k, v in sorted(category_counts.items(), key=lambda item: item[1])}

    # price range by category
    priceRange_category = {}
    category = category_counts.keys()
    for c in category:
        l_p = [p["price"] for p in products if p["category"] == c]
        priceRange_category[c] = "{:.2f}".format(max(l_p) - min(l_p))
    
    price_list = [p["price"] for p in products]
    stock_list = [p["stock"] for p in products]


    return {
        "byBrands": {
            "labels": list(brands_rating.keys()),
            "values": list(brands_rating.values())
        },
        "byCategory": {
            "labels": list(category_counts.keys()),
            "values": list(category_counts.values())
        },
        "byPriceRange": {
            "labels": list(priceRange_category.keys()),
            "values": list(priceRange_category.values())
        },
        "TotalProducts": len(products),
        "AvgPrice" : statistics.mean(price_list),
        "TotalStock": sum(stock_list)
    }
