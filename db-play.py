from app.models import BloodSugarMonth

import uuid
uuid = str(uuid.uuid4())

b = BloodSugarMonth(uuid=uuid, year=2018, month=2, m1=0, e1=114, m2=99, e2=117)
print(b)
