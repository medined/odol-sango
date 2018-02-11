from app import app, db
from app.models import BloodSugarMonth
import uuid

print('Database Tables')
print(db.engine.table_names())
print('---------------')

record = db.session.query(BloodSugarMonth)\
    .filter(BloodSugarMonth.uuid=='90967832-c334-47d3-864a-8a3f7e4baf82')\
    .filter(BloodSugarMonth.year==2019)\
    .filter(BloodSugarMonth.month==2)\
    .first()

if record is None:
    print('n')
else:
    print('y')

print(record)

# b = BloodSugarMonth(uuid=str(uuid.uuid4()), year=2018, month=2, morning1=0, evening1=114, morning2=99, evening2=117)
# print(b)
# db.session.add(b)
# db.session.commit()
