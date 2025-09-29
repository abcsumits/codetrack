After cloning the repo

1.create a virtual env with python 3.9 and activate  the env


2.install requirements ```pip install -r requirements.txt``` make sure you are inside projects root



3.set up .env


4.run command ```python manage.py migrate``` (if running for the first time without db else can ignore) 


5.run command```python manage.py runserver --insecure``` , #default port will be 8000



6.open http://127.0.0.1:8000/
