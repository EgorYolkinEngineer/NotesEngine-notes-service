from fastapi import APIRouter, Depends
from middlewares.auth import validate_authorization
from fastapi import HTTPException
from core.db_models import *
from core.database import session

notes_router = APIRouter()


@notes_router.get('/notes/create/')
async def register_user(note_text: str,
                        auth: str | dict = Depends(validate_authorization)):
    if auth.get('status') != 200:
        return auth

    note = Note(
        text=note_text,
        creator=auth.get('id')
    )
    session.add(note)
    session.commit()

    return {'id': note.id,
            'text': note.text,
            'creator': note.creator,
            'created': note.created}


@notes_router.get('/notes/get/')
async def register_user(auth: str | dict = Depends(validate_authorization)):
    if auth.get('status') != 200:
        return auth

    notes = session.query(Note).filter_by(creator=auth.get('id'))

    return [_.to_dict() for _ in notes]


@notes_router.get('/notes/note/get/')
async def register_user(note_id: int, auth: str | dict = Depends(validate_authorization)):
    if auth.get('status') != 200:
        return auth

    note = session.query(Note).filter_by(id=note_id).first()

    return note.to_dict()
