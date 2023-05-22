# stock-trading
# STEPS TO RUNNING THIS PROGRAM
- Install redis for your os. ensure your redis is running and active.
- clone this repository to your local computer with the below command.
```
git clone https://github.com/aayobam/stock-trading.git
```
- open project with any of your prefered ide, ensure you are in the project root where manage.py is visible.
- install your preferred virtual environment and activate it.
- run the below command to install all dependencies and packages.
```
pip install -r requirements.py
```
```
python manage.py migrate
```
- run the below command to auto generate 10 traders. this is to ease you of manually creating users.you can check the implementation in the the management/commands folder of the traders.
```
python manage.py createdummyusers
```
- manually create an admin user with the below command and log in to view all users created on the user model and trade model.
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
- to simulate the trading, open a new terminal and type the below command, if everything goes well, you should see nice messages. the command starts celery and django-celery-beats for scheduling the simulation.
```
celery -A config worker -l info -B
```
- head to the login page to view the trading graph.
> Note1: the username:password format goes thus.
- testuser1:password1
> Note2: the program excludes admin or staffs from trading.