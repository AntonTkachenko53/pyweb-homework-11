from fastapi import APIRouter, Depends, HTTPException
from typing import Optional, List
from dependencies.database import get_db, SessionLocal
from schemas.contacts_schemas import Contact, ContactCreate, ContactUpdate
from services.contacts_service import ContactService

router = APIRouter()


@router.get('/')
async def list_contacts(first_name: Optional[str] = None, last_name: Optional[str] = None,
                        email: Optional[str] = None, db: SessionLocal = Depends(get_db)) -> List[Contact]:
    contact_service = ContactService(db=db)
    result = []
    if first_name:
        contact = await contact_service.get_by_first_name(first_name)
        result.append(contact)
    elif last_name:
        contact = await contact_service.get_by_last_name(last_name)
        result.append(contact)
    elif email:
        contact = await contact_service.get_by_email(email)
        result.append(contact)
    else:
        contact = await contact_service.get_all_contacts()
        result.append(contact)
    return result


@router.get('/{id}')
async def get_contact_by_id(id: int, db: SessionLocal = Depends(get_db)) -> Contact:
    contact_item = await ContactService(db=db).get_by_id(id)
    return contact_item


@router.post('/')
async def create_contact(contact_item: ContactCreate, db: SessionLocal = Depends(get_db)) -> Contact:
    new_contact = await ContactService(db=db).create_contact(contact_item)
    return new_contact


@router.put('/{id}')
async def update_contact(id: int, contact_item: ContactUpdate, db: SessionLocal = Depends(get_db)) -> Contact:
    updated_contact = await ContactService(db=db).update(id, contact_item)
    return updated_contact


@router.delete('/{id}')
async def delete_contact(id: int, db: SessionLocal = Depends(get_db)) -> Contact:
    removed_contact = await ContactService(db=db).remove(id)
    return removed_contact


@router.get('/birthdays_in_7_days')
async def contacts_birthdays_in_7_days(db: SessionLocal = Depends(get_db)) -> list[Contact]:
    contacts = ContactService(db=db).contacts_birthdays_in_7_days()
    return contacts
