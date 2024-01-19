from repository.contacts_repo import ContactsRepo
from schemas.contacts_schemas import Contact, ContactCreate, ContactUpdate
from models.contacts_model import ContactModel


class ContactService():

    def __init__(self, db):
        self.repo = ContactsRepo(db=db)

    async def get_all_contacts(self) -> list[Contact]:
        all_contacts_from_db = await self.repo.get_all()
        return [Contact.from_orm(item) for item in all_contacts_from_db]

    async def get_by_id(self, id: int) -> Contact:
        contact = await self.repo.get_by_id(id)
        return Contact.from_orm(contact)

    async def create_contact(self, contact_item: ContactCreate) -> Contact:
        new_contact_for_db = await self.repo.create(contact_item)
        return Contact.from_orm(new_contact_for_db)

    async def update(self, contact_item: ContactUpdate, id: int):
        updated_contact = await self.repo.update(id, contact_item)
        return Contact.from_orm(updated_contact)

    async def remove(self, id: int):
        removed_contact = await self.repo.remove(id)
        return Contact.from_orm(removed_contact)

    async def get_by_first_name(self, first_name: str):
        contact = await self.repo.get_by_first_name(first_name)
        return Contact.from_orm(contact)

    async def get_by_last_name(self, last_name: str):
        contact = await self.repo.get_by_last_name(last_name)
        return Contact.from_orm(contact)

    async def get_by_email(self, email: str):
        contact = await self.repo.get_by_email(email)
        return Contact.from_orm(contact)

    async def contacts_birthdays_in_7_days(self):
        contacts = await self.repo.contacts_birthdays_in_7_days()
        return [Contact.from_orm(item) for item in contacts]
