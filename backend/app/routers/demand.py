from fastapi import APIRouter,Depends
from ..auth_utils import current_user
from ..schemas import DemandRequest
from ..services.demand_service import get_demo_demand,predict_demand
router=APIRouter(prefix='/demand',tags=['Demand'])
@router.get('/')
def demand(u=Depends(current_user)): return get_demo_demand()
@router.post('/predict')
def prediction(data:DemandRequest,u=Depends(current_user)): return predict_demand(data.model_dump())
