# 파이썬 및 FastAPI 입문

# 📜 **프로젝트 요약**

- FastAPI를 활용하여 간단한 CRUD API 구현

# 📅 프로젝트 기간

- 2024.11 ~ 2024.11

# 🫙 Github

- https://github.com/verystrongvery/hello_python

# 🛠 기술 스택

- Python, FastAPI, SQLAlchemy

# 🏫 프로젝트에서 배운점

### 1. 파이썬

**venv 가상환경**

- 프로젝트별로 독립적인 파이썬 환경을 생성하고 관리할 수 있게 해주는 라이브러리 입니다.

**context manager**

- 특정 코드 블록의 실행 전후에 어떤 동작을 수행할 수 있도록 하는 기능 입니다.
- 디비 세션을 생성하고 종료하는 과정에서 사용했습니다.

**with 문법**

- context manager를 사용할 때 사용되는 구문으로, with 블록의 실행 전후에 context manager가 정의한 동작을 수행할 수 있습니다.
- 디비 세션이 팔요한 경우 사용했습니다.

**generator**

- yield 키워드가 포함된 함수로, yield 키워드를 만나면 함수의 실행을 일시 중단하고, 값을 반환합니다.
- 수많은 데이터를 한번에 처리하지 않고, 필요할 때마다 하나씩 처리하므로 메모리를 효율적으로 사용할 수 있습니다.
- 디비 세션을 생성하고 종료하는 context manager를 생성할 때 사용했습니다.

### 2. FastAPI

**라우터**

- 특정 경로의 그룹화를 위한 라우터를 생성 및 등록 했습니다,

**Pydantic 라이브러리**

- API의 Request Body, Response Body를 정의했습니다.
- @field_validator를 활용하여 Request Body의 유효성 검사를 했습니다.
- Field를 활용하여 스키마 필드의 제약조건을 설정했습니다.

**Depends 함수**

- 의존성을 주입받은 함수를 먼저 실행시키고, 그 결과를 전달 하는 기능 입니다.
- 디비 세션을 생성하고 종료하는 방식을 변경했습니다.
    - 기존: context manager를 활용하여 디비 세션이 필요한 로직 전후에 디시 세션 생성 및 종료 로직 추가
    - 변경: Depends 함수를 활용하여 디비 세션을 생성 및 종료하는 함수 주입

# 📕 파이썬 및 FastAPI 학습 과정

### 1. 환경 구축(우분투 환경)

1. 파이썬 프로젝트 환경을 편히 구축하기 위해 venv 모듈로 가상환경 생성  
    - `python3 -m venv myapi`
2. 가상환경 활성화  
    - `source myapi/bin/activate`

3. API를 만들기 위한 파이썬 웹 프레임워크인 FastAPI 설치  

- `pip install fastapi`

4. 파이참 설치  

- 파이썬 인터프리터 위치 설정

### 2. 파이썬 및 FastAPI 입문

1. FastAPI 서버를 쉽게 구축하기 위해 uvicorn 모듈 설치
    - `pip install "uvicorn[standard]"`
2. uvicorn로 FastAPI 서버 실행
    - `uvicorn main:app --reload`

### 3. 데이터베이스 설정

1. SQLAlchemy ORM 설치
    - `pip install sqlalchemy`
2. 데이버테이스 설정 파일 작성   
    - 디비 경로 설정, 커넥션 풀 생성, 디비 세션 생성, ORM 클래스 생성
3. 데이터를 관리하는데 사용하는 ORM 클래스인 모델 클래스 생성
4. 데이터베이스 마이그레이션을 위해 alembic 설치  
    - `pip install alembic`
5. alembic 초기화하여 alembic.ini 파일, migration 폴더 생성  
    - `alembic init migrations`
    - alembic.ini: 데이터베이스 파일 경로 설정을 담당
    - migration/env.py: 마이그레이션시, 생성한 모델 클래스를 참조하여 데이터베이스 스키마를 생성할 수 있도록 설정
6. 데이터베이스 마이그레이션 스크립트 생성
    - `alembic revision --autogenerate`
7. 데이터베이스 마이그레이션 스크립트 실행하여 데이터베이스 스키마 생성
    - `alembic upgrade head`
8. 서버가 필요 없이 파일 기반으로 동작하는 데이터베이스 sqlite3 설치
    - `sudo apt-get install sqlite3`
9. 데이터베이스 접속
    - `sqlite3 myapi.db`
    - `.tables`: 테이블 목록 확인

### 4. CRUD API 구현

1. SQLAlchemy ORM을 활용하여 간단한 CRUD API 구현
2. docs 페이지를 통해 API 테스트

# 🏀 앞으로 해야할 공부

### 멀티 쓰레드 환경에서 데이터 무결성을 유지하는 방법

SQLAlchemy에서 데이터베이스 연결시 사용되는 옵션중 하나인 `check_same_thread`은 멀티 쓰레드 환경 지원 여부를 결정하는 옵션 입니다.   

`check_same_thread`를 false로 설정하여, 멀티 쓰레드 환경에서 데이터 무결성을 유지하기 위해 데이터베이스 락, 데이터베이스 격리 수준 설정 등을 어떻게 하는지 공부할 계획 입니다.

### SQLAlchemy ORM

ORM을 통해 UPDATE 쿼리가 필요할 때, update()를 직접적으로 호출하는 방법과 디비를 통해 조회한 데이터의 값을 변경한 후 commit()을 호출하여 변경사항을 자동으로 반영되는 두 가지 방법이 있습니다. 

디비를 통해 조회한 데이터의 값을 변경한 후 어떻게 자동으로 반영되는지에 대한 원리를 공부할 계획 입니다.  

(JPA ORM 에서는 영속성 컨텍스트, 1차 캐시 등을 통해 변경된 데이터를 자동으로 반영합니다.)

# 🤩 느낀점

파이썬이 어색하긴 하지만, 자바에 비해 문볍이 간결하고 직관적인 느낌이 들었고,

FastAPI도 Spring에 비해 설정도 간편하고, 로딩 속도도 빠르며, 코드 변경시 리로딩이 자동으로 되는 기능이 있어서 개발이 편리했습니다.

기회가 된다면, 파이썬 및 FastAPI를 활용하여 실무 프로젝트를 진행해보고 싶습니다.