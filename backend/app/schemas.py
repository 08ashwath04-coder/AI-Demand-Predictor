from pydantic import BaseModel,EmailStr
class RegisterRequest(BaseModel): name:str; email:EmailStr; password:str; role:str
class LoginRequest(BaseModel): email:EmailStr; password:str
class ProductCreate(BaseModel): name:str; category:str|None=None; description:str|None=None
class InventoryCreate(BaseModel): product_id:int; current_stock:float; minimum_stock:float
class DemandRequest(BaseModel): product:str; date:str; location:str
