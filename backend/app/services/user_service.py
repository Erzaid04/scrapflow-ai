from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegisterSchema
from app.auth.security import hash_password


def check_email_exists(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()


def check_phone_exists(
    db: Session,
    phone_number: str
):
    return db.query(User).filter(
        User.phone_number == phone_number
    ).first()


def create_user(
    user_data: UserRegisterSchema,
    hashed_password: str
):
    return User(
        name=user_data.name,
        email=user_data.email,
        phone_number=user_data.phone_number,
        password_hash=hashed_password,
        role="owner",
        is_active=True
    )
def register_user(
    db: Session,
    user_data: UserRegisterSchema
):
    try:

        # Check email
        if check_email_exists(
            db,
            user_data.email
        ):
            raise ValueError(
                "Email already registered"
            )

        # Check phone
        if check_phone_exists(
            db,
            user_data.phone_number
        ):
            raise ValueError(
                "Phone number already registered"
            )

        # Hash password
        hashed_password = hash_password(
            user_data.password
        )

        # Create user object
        user = create_user(
            user_data,
            hashed_password
        )

        # Save user
        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    except Exception:
        db.rollback()
        raise