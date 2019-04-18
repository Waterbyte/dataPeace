#Description
The backend is made with Python Flask and the default development server. Webargs are used for argument parsing and Flask_restful for routing.
Mongodb is used as a database.
Docker is used for deployment. 

#Setup

Follow these steps:
1. cd dataPeace
2. create virtualenv and pip install -r backendAPI/requirements.txt
3. Setup database(check DB_init.txt) and in db.py change the ip of database.
3. run python backendAPI/app_run.py

Server will be hosted on localhost:5000
Hit with postman or any other tool.