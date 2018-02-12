from app import app, db
from app.models import BloodSugarMonth
import uuid

print('Database Tables')
print(db.engine.table_names())
print('---------------')

uuid = '90967832-c334-47d3-864a-8a3f7e4baf82'

b = BloodSugarMonth(uuid=uuid, year=2018, month=1,\
    morning1=109,\
    morning2=106,\
    morning3=113,\
    morning4=110,\
    morning5=136,\
    morning6=121,\
    morning7=125,\
    morning8=113,\
    morning9=117,\
    morning10=100,\
    morning11=100,\
    morning12=125,\
    morning13=113,\
    morning14=126,\
    morning15=109,\
    morning16=120,\
    morning17=114,\
    morning18=112,\
    morning19=132,\
    morning20=122,\
    morning21=143,\
    morning22=113,\
    morning23=146,\
    morning24=124,\
    morning26=197,\
    morning27=129,\
    morning28=108,\
    morning29=109,\
    morning30=163,\
    morning31=143,\
     evening1=120,\
     evening2=116,\
     evening3=141,\
     evening4=168,\
     evening5=155,\
     evening6=157,\
     evening7=124,\
     evening8=130,\
     evening10=126,\
     evening11=143,\
     evening12=128,\
     evening13=151,\
     evening14=103,\
     evening15=160,\
     evening16=151,\
     evening17=126,\
     evening18=160,\
     evening19=127,\
     evening20=149,\
     evening21=185,\
     evening22=133,\
     evening23=128,\
     evening24=137,\
     evening25=181,\
     evening26=146,\
     evening27=265,\
     evening28=128,\
     evening29=132,\
     evening30=132)

db.session.add(b)
db.session.commit()

record = db.session.query(BloodSugarMonth)\
    .filter(BloodSugarMonth.uuid==uuid)\
    .filter(BloodSugarMonth.year==2018)\
    .filter(BloodSugarMonth.month==1)\
    .first()

if record is None:
    print('Not Found')
else:
    print(record)
