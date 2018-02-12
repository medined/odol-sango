from app import db
from app.forms import MonthForm
from calendar import monthrange

class BloodSugarMonth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), index=True)
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

    def getGraphInfo(self):
        minimum = 9999
        maximum = 0
        for n in range(1, 32):
            mValue = self.__getattribute__('morning'+str(n))
            eValue = self.__getattribute__('evening'+str(n))
            if mValue:
                if mValue < minimum:
                    minimum = mValue
                if mValue > maximum:
                    maximum = mValue
            if eValue:
                if eValue < minimum:
                    minimum = eValue
                if eValue > maximum:
                    maximum = eValue
        minimum = minimum - 10
        maximum = maximum + 10
        return minimum, maximum

    def save(form):

        def getMorningFormField(form, n):
            for field in form:
                if field.name == 'morning' + str(n):
                    return(field.data)

        def getEveningFormField(form, n):
            for field in form:
                if field.name == 'evening' + str(n):
                    return(field.data)

        print('--------------------saving')
        # see if database record exists
        record = db.session.query(BloodSugarMonth)\
            .filter(BloodSugarMonth.uuid == form.handle.data)\
            .filter(BloodSugarMonth.year == form.year.data)\
            .filter(BloodSugarMonth.month == form.month.data)\
            .first()

        if record == None:
            record = BloodSugarMonth(uuid=form.handle.data, year=form.year.data, month=form.month.data)

        for n in range(1, 32):
            # assign form value to database record.
            record.__setattr__('morning'+str(n), getMorningFormField(form, n))
            record.__setattr__('evening'+str(n), getEveningFormField(form, n))

        if record.id == None:
            db.session.add(record)

        db.session.commit()
