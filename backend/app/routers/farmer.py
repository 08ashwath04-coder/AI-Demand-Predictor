from fastapi import APIRouter,Depends
from ..auth_utils import current_user
from ..models import User
from ..services.demand_service import get_demo_demand
from ..services.recommendation_service import farmer_recommendations
router=APIRouter(prefix='/farmer',tags=['Farmer'])
@router.get('/dashboard')
def dashboard(u:User=Depends(current_user)): return {'projected_demand':420,'confidence':92,'revenue':'2.8L','active_crops':6,'demand_chart':get_demo_demand()}
@router.get('/crops')
def crops(u:User=Depends(current_user)): return [{'id':1,'name':'Tomato','season':'Winter'},{'id':2,'name':'Potato','season':'Winter'},{'id':3,'name':'Onion','season':'Winter'}]
@router.get('/recommendations')
def recommendations(u:User=Depends(current_user)): return farmer_recommendations()
