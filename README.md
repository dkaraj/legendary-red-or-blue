## Quick Start
```
git clone https://github.com/dkaraj/legendary-red-or-blue.git
 ```

1. Install  virtualenv
`pip install virtualenv` <br>
2. Create a virtual environment
   ` virtualenv venv` <br>
3. Activate it
   ` \venv\Scripts\activate.bat`
4. Install packages:
    `pip install -r requirements.txt` <br>
5. Commands for db
   1. Make migration:`python manage.py makemigrations`
   2. Exe migration:`python manage.py migrate`
   3. Exe command to populate db: `python manage.py init_dummy_data -a`
   4. Run application:`python manage.py runserver`
   
    
## Testing:

 - You can also run some  tests about this api. Tests are located in /api/tests


# Dependencies

- DRF (DJANGO REST FRAMEWORK)
- DJANGO MTV (Model Template View)

- Everything is organized based on Django and DRF.

# Docs:
  http://localhost:8000/redoc/