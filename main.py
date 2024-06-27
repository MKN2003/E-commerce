from fastapi import FastAPI
from database import Base, engine
from api.api_user.users import user_router
from api.api_product.products import product_router
from api.api_category.categories import category_router
from api.api_review.reviews import review_router
from api.api_cart.carts import cart_router
from api.api_order.orders import order_router
from api.api_photo.photos import photo_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(product_router)
app.include_router(photo_router)
app.include_router(category_router)
app.include_router(review_router)
app.include_router(cart_router)
app.include_router(order_router)
