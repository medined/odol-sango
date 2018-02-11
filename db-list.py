from app import app, db
from app.models import BloodSugarMonth

records = BloodSugarMonth.query.all()
for record in records:
    print(record)
    print('------------------------')
