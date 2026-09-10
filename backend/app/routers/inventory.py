from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Inventory
from ..schemas import InventoryCreate
from ..auth_utils import current_user
router=APIRouter(prefix='/inventory',tags=['Inventory'])
@router.get('/')
def get_inventory(db:Session=Depends(get_db),u=Depends(current_user)): return db.query(Inventory).all()
@router.post('/')
def create_inventory(data:InventoryCreate,db:Session=Depends(get_db),u=Depends(current_user)):
 i=Inventory(**data.model_dump(),updated_at=datetime.utcnow());db.add(i);db.commit();db.refresh(i);return i
@router.put('/{inventory_id}')
def update_inventory(inventory_id:int,data:InventoryCreate,db:Session=Depends(get_db),u=Depends(current_user)):
 i=db.query(Inventory).filter(Inventory.id==inventory_id).first()
 if not i: raise HTTPException(404,'Inventory item not found')
 for k,v in data.model_dump().items(): setattr(i,k,v)
 i.updated_at=datetime.utcnow();db.commit();db.refresh(i);return i
