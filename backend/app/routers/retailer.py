from fastapi import APIRouter,Depends
from ..auth_utils import current_user
from ..models import User
from ..services.demand_service import get_demo_demand
from ..services.recommendation_service import retailer_recommendations
router=APIRouter(prefix='/retailer',tags=['Retailer'])
@router.get('/dashboard')
def dashboard(u:User=Depends(current_user)): return {'projected_demand':1250,'inventory':840,'stockout_risk':14,'sales':'5.6L','demand_chart':get_demo_demand()}
@router.get('/inventory')
def inventory(u:User=Depends(current_user)): return [{'id':1,'product':'Rice','current_stock':150,'minimum_stock':100},{'id':2,'product':'Tomato','current_stock':80,'minimum_stock':120}]
@router.get('/recommendations')
def recommendations(u:User=Depends(current_user)): return retailer_recommendations()
