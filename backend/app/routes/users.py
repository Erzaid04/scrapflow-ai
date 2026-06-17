from fastapi import APIRouter,Depends
from app.dependencies.roles import require_roles

from app.dependencies.auth import get_current_user
router = APIRouter(
    prefix = "/api/v1/users",
    tags = ["Users"]
    
)

@router.get("/me")
def get_me(
    current_user = Depends(get_current_user)
):
    return {
        "id":current_user.id,
        "name":current_user.name,
        "email":current_user.email,
        "role":current_user.role
    }
    
@router.get("/owner_only")
def owner_only(
    current_user = Depends(
        require_roles("owner")
    )
):
    return {
        "message":"Owner Access Granted",
        "user":current_user.name
    }
    
@router.get("/worker-only")
def worker_only(
    current_user = Depends(require_roles("worker"))
):
    return{
        "message":"Worker Access Granted",
        "user":current_user.name
    }
@router.get("/accountant-only")
def accountant_only(
    current_user = Depends(require_roles("accountant"))
):
    return{
        "message":"Accountant Access Granted",
        "user":current_user.name
    }
    
@router.get("/inventry-access")
def inventry_access(
    current_user = Depends(
        require_roles("owner","worker")
    )
):
    return{
        "message": "Inventry Access Granted",
        "user":current_user.name,
        "role":current_user.role
    }