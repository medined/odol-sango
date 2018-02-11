from app import app, db
from app.models import BloodSugarMonth

print('Database Tables')
print(db.engine.table_names())
print('---------------')

import uuid
uuid = str(uuid.uuid4())

b = BloodSugarMonth(uuid=uuid, year=2018, month=2, morning1=0, evening1=114, morning2=99, evening2=117)
print(b)
db.session.add(b)
db.session.commit()
