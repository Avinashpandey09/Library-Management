from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get("/")
def get_auth():
    return {
        "message": "Auth router working"
    }

@router.get("/users")
def get_users():
    return {
        "message": "Get all users"
    }

@router.get("/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "Get user by ID"
    }
