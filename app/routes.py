from calendar import monthrange
from flask import render_template, redirect, url_for
from app import app, db
from app.forms import MonthForm
from app.models import BloodSugarMonth

import calendar
import datetime
import uuid

def populateMonthForm(handle, year, month):
    (weekday, daysInMonth) = monthrange(year, month)
    form = MonthForm()
    form.handle.data = handle
    form.year.data = year
    form.month.data = month
    form.daysInMonth.data = daysInMonth

    # see if database record exists
    record = db.session.query(BloodSugarMonth)\
        .filter(BloodSugarMonth.uuid == handle)\
        .filter(BloodSugarMonth.year == year)\
        .filter(BloodSugarMonth.month == month)\
        .first()

    if record:
        for n in range(1, 32):
            mValue = record.__getattribute__('morning'+str(n))
            if mValue != 0 and mValue != None:
                for field in form:
                    if field.name == 'morning' + str(n):
                        field.data = mValue
            eValue = record.__getattribute__('evening'+str(n))
            if eValue != 0 and eValue != None:
                for field in form:
                    if field.name == 'evening' + str(n):
                        field.data = eValue

    return form, record

@app.route('/')
def index():
    handle = str(uuid.uuid4())
    return redirect(url_for('indexWithHandle', handle=handle))

# just the handle defaults to the current year and month.
@app.route('/<handle>')
def indexWithHandle(handle):
    now = datetime.datetime.now()
    form, record = populateMonthForm(handle, now.year, now.month)
    if record:
        minimum, maximum = record.getGraphInfo()
    return render_template(
        'index.html',
        monthName=calendar.month_name[now.month],
        daysInMonth=int(form.daysInMonth.data),
        minimum=minimum,
        maximum=maximum,
        form=form)

@app.route('/<handle>/<int:year>/<int:month>')
def indexWithHandleAndDate(handle, year, month):
    form, record = populateMonthForm(handle, year, month)
    if record:
        minimum, maximum = record.getGraphInfo()
    return render_template(
        'index.html',
        monthName=calendar.month_name[month],
        daysInMonth=int(form.daysInMonth.data),
        minimum=minimum,
        maximum=maximum,
        form=form)

@app.route('/process-form', methods=['POST'])
def processForm():
    form = MonthForm()
    if form.validate_on_submit():
        BloodSugarMonth.save(form)
    return redirect(url_for('indexWithHandle', handle=form.handle.data))
