import os
import shutil
from config.settings import BASE_DIR
from pathlib import Path



path1= Path(os.path.normpath(str(BASE_DIR)+"/FilDrop/__pycache__"))
path2= Path(os.path.normpath(str(BASE_DIR)+"/FilDrop/migrations"))
path3=Path(os.path.normpath(str(BASE_DIR)+'/db.sqlite3'))
path4= Path(os.path.normpath(str(BASE_DIR)+"/1"))


try:
    shutil.rmtree(path1)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

try:
    shutil.rmtree(path2)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

try:
    os.remove( path3)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))


try:
    shutil.rmtree( path4)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

cmd1= "python manage.py makemigrations"
cmd2= "python manage.py makemigrations FilDrop"
cmd3="python manage.py migrate"
cmd4="python manage.py runserver"
cmd5="python manage.py createsuperuser --username admin --email admin@g.com --skip-checks"
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd5)
os.system(cmd4)

