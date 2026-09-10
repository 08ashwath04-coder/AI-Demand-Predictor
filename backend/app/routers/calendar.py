from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import CalendarEvent
from ..auth_utils import current_user
router=APIRouter(prefix='/calendar',tags=['Calendar'])
@router.get('/')
def get_calendar(db:Session=Depends(get_db),u=Depends(current_user)): return db.query(CalendarEvent).order_by(CalendarEvent.date).all()
@router.get('/{month}')
def get_month(month:int,db:Session=Depends(get_db),u=Depends(current_user)):
 return [e for e in db.query(CalendarEvent).all() if e.date and e.date.month==month]
