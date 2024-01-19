from fastapi import FastAPI
from api.contacts_items import router as contacts_router
from models import contacts_model
from dependencies.database import engine

contacts_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contacts_router, prefix='/contacts')


@app.get('/')
async def health_check():
    return {'status': 'OK'}
