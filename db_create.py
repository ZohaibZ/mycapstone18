from application import db
from application.models import *

db.create_all()
print "Db created"
