## Environment setup
mkvirtualenv glover  
pip install -r requirements.txt 
workon glover

## Populating the database
python population_script.py

## Running tests
python manage.py test

## Login as an admin after populating the database
username: yourname  
password: 1234