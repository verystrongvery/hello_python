from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db" # 디비 경로 설정
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # 커넥션 풀 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 디비 세션 생성
Base = declarative_base() # ORM 클래스 생성

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()