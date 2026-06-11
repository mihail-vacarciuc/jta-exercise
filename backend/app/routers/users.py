from fastapi import APIRouter
from app.services.fetcher import get_cache_data
import collections

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("")
async def get_users():
    cache = await get_cache_data()
    users = cache["users"]

    return [
        {
            "id": u["id"],
            "name": u["firstName"] +" "+ u["lastName"],
            "age": u["age"],
            "gender": u["gender"],
            "university": u["university"],
            "role": u["role"],
            "state": u["address"]["state"]
        }
        for u in users]

@router.get("/analytics")
async def get_users():
    cache = await get_cache_data()
    users = cache["users"]

    # Distribution by state
    state_counts = {}
    for u in users:
        state = u["address"]["state"]
        state_counts[state] = state_counts.get(state, 0) + 1

    # Distribution by university
    uni_counts = {}
    for u in users:
        uni = u.get("university", "Unknown")
        uni_counts[uni] = uni_counts.get(uni, 0) + 1

    state_counts = {k: v for k, v in sorted(state_counts.items(), key=lambda item: item[1], reverse=True)}
    uni_counts = {k: v for k, v in sorted(uni_counts.items(), key=lambda item: item[1])}

    return {
        "byState": {
            "labels": list(state_counts.keys()),
            "values": list(state_counts.values())
        },
        "byUniversity": {
            "labels": list(uni_counts.keys()),
            "values": list(uni_counts.values())
        },
        "TotalUsers": len(users)
    }