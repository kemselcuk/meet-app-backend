from sqlalchemy.orm import Session
from . import models, schemas, auth
from fastapi import HTTPException

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Check if user already exists
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    existing_username = get_user_by_username(db, user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Hash the password
    hashed_password = auth.get_password_hash(user.password)
    
    # Create new user
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_group(db: Session, group: schemas.GroupCreate):
    # Check if group name already exists
    existing_group = db.query(models.Group).filter(models.Group.name == group.name).first()
    if existing_group:
        raise HTTPException(status_code=400, detail="Group name already exists")

    db_group = models.Group(
        name=group.name,
        description=group.description
    )
    
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def join_group(db: Session, user_id: int, group_id: int):
    # Check if group exists
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    # Check if user-group relationship already exists
    existing_membership = db.query(models.UserGroup).filter(
        models.UserGroup.user_id == user_id,
        models.UserGroup.group_id == group_id
    ).first()

    if existing_membership:
        raise HTTPException(status_code=400, detail="User already in group")

    # Create user-group relationship
    user_group = models.UserGroup(
        user_id=user_id,
        group_id=group_id
    )
    
    db.add(user_group)
    db.commit()
    db.refresh(user_group)
    return user_group

def create_meeting(db: Session, meeting: schemas.MeetingCreate):
    # Check if group exists
    group = db.query(models.Group).filter(models.Group.id == meeting.group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    db_meeting = models.Meeting(
        group_id=meeting.group_id,
        title=meeting.title,
        description=meeting.description,
        location=meeting.location,
        meeting_time=meeting.meeting_time
    )
    
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting