from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from ..schemas import ProductCreate
from ..auth_utils import current_user
router=APIRouter(prefix='/products',tags=['Products'])
@router.get('/')
def get_products(db:Session=Depends(get_db),u=Depends(current_user)): return db.query(Product).all()
@router.get('/{product_id}')
def get_product(product_id:int,db:Session=Depends(get_db),u=Depends(current_user)):
 p=db.query(Product).filter(Product.id==product_id).first()
 if not p: raise HTTPException(404,'Product not found')
 return p
@router.post('/')
def create_product(data:ProductCreate,db:Session=Depends(get_db),u=Depends(current_user)):
 p=Product(**data.model_dump());db.add(p);db.commit();db.refresh(p);return p
