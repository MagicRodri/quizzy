# quizzy
### A basic application for multiple choice quizzes
## Installation

### - Clone this repository
### - cd into quizzy directory
```bash
cd quizzy/
```
### - Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```
### - Create .env and provide postgres credentials
```bash
(venv) touch .env
```
### .env sample
```
SECRET_KEY = mysecret
DEBUG = 1
ALLOWED_HOSTS=localhost

DATABASE_NAME=my_db_name
DATABASE_USER=my_db_user
DATABASE_PASSWORD=my_db_password
DATABASE_HOST = my_db_localhost
DATABASE_PORT = my_db_5434
```
### - Run migrations and run server
```bash
(venv) python manage.py migrate
(venv) python manage.py runserver
```

### 

## Features to add/improve :
    - [] Illustrative image for quizzes
    - [] Answers viewing after test complete
    - [] Answers editing before test ends up