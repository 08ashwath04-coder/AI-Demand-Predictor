from datetime import datetime,timedelta,timezone
from jose import jwt
from passlib.context import CryptContext
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import JWT_SECRET
from .database import get_db
from .models import User
pwd_context=CryptContext(schemes=['pbkdf2_sha256'],deprecated='auto'); oauth2=OAuth2PasswordBearer(tokenUrl='/auth/login')
def hash_password(p): return pwd_context.hash(p)
def verify_password(p,h): return pwd_context.verify(p,h)
def create_token(user): return jwt.encode({'sub':str(user.id),'role':user.role,'exp':datetime.now(timezone.utc)+timedelta(hours=12)},JWT_SECRET,algorithm='HS256')
def current_user(token:str=Depends(oauth2),db:Session=Depends(get_db)):
 try: data=jwt.decode(token,JWT_SECRET,algorithms=['HS256']); uid=int(data['sub'])
 except Exception: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid or expired token')
 user=db.query(User).filter(User.id==uid).first()
 if not user: raise HTTPException(status_code=401,detail='User not found')
 return user
