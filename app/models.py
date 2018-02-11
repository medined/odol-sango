from app import db

class BloodSugarMonth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), index=True, unique=True)
    year =  db.Column(db.Integer, index=False)
    month = db.Column(db.Integer, index=False)
    for n in range(1, 32):
        locals()[''.join("morning"+str(n))] = db.Column(db.Integer, index=False)
        locals()[''.join("evening"+str(n))] = db.Column(db.Integer, index=False)

    def columns():
        return BloodSugarMonth.__table__.columns.keys()

    def __repr__(self):
        oMorning = ""
        oEvening = ""
        for n in range(1, 32):
            oMorning = oMorning + 'morning{}=({}) '.format(n, self.__getattribute__('morning'+str(n)))
            oEvening = oEvening + 'evening{}=({}) '.format(n, self.__getattribute__('evening'+str(n)))
        return '<BloodSugarMonth id({}) uuid({} year({}) month({}) {} {})>'.format(self.id, self.uuid, self.year, self.month, oMorning, oEvening)
