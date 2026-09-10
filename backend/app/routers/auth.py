from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import RegisterRequest,LoginRequest
from ..auth_utils import hash_password,verify_password,create_token,current_user
router=APIRouter(prefix='/auth',tags=['Authentication'])
@router.post('/register')
def register(data:RegisterRequest,db:Session=Depends(get_db)):
 if data.role not in {'farmer','retailer'}: raise HTTPException(400,'Role must be farmer or retailer')
 if db.query(User).filter(User.email==data.email).first(): raise HTTPException(400,'Email already registered')
 if len(data.password)<6: raise HTTPException(400,'Password must be at least 6 characters')
 u=User(name=data.name,email=data.email,password_hash=hash_password(data.password),role=data.role);db.add(u);db.commit();db.refresh(u)
 return {'message':'Registration successful'}
@router.post('/login')
def login(data:LoginRequest,db:Session=Depends(get_db)):
 u=db.query(User).filter(User.email==data.email).first()
 if not u or not verify_password(data.password,u.password_hash): raise HTTPException(401,'Invalid email or password')
 return {'access_token':create_token(u),'token_type':'bearer','user':{'id':u.id,'name':u.name,'email':u.email,'role':u.role}}
@router.get('/me')
def me(u:User=Depends(current_user)): return {'id':u.id,'name':u.name,'email':u.email,'role':u.role}
