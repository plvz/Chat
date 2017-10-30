# Chat
Direct chat python channel

First of all you need python pip and redis server you can install them with the command :
sudo apt-get install python-pip redis-server

secondly install the python libraries such as Django:
pip install django channels redis asgi_redis 

Then run the command for set up the sqlite database:
python manage.py migrate

Finally you an run the server:
python manage.py runserver

You can enjoy the Py chat at http://localhost:8000
You will have to be login, so create an user and sign in for access to the chat 
