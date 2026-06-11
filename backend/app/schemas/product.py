from pydantic import BaseModel, EmailStr, AnyHttpUrl
from typing import Optional, List
from datetime import datetime

class ReviewSchema (BaseModel):
    rating: int | float
    comment: Optional[str]
    date: datetime
    reviewerName: str
    reviewerEmail: EmailStr

class ProductSchema (BaseModel):
    id: int
    title: str
    description: Optional[str]
    category: str
    price: float
    discountPercentage: Optional[float]
    rating: float
    stock: int
    brand: Optional[str] = None
    availabilityStatus: str
    reviews: List[ReviewSchema]
    images: Optional[List[AnyHttpUrl]]
    thumbnail: AnyHttpUrl

class ProductsResponseSchema(BaseModel):
    products: List[ProductSchema]
    total: int
    skip: int
    limit: int