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

    # next month
    if now.month == 12:
        next_year = now.year + 1
        next_month = 1
    else:
        next_year = now.year
        next_month = now.month + 1

    # previous month
    if month == 1:
        previous_year = now.year - 1
        previous_month = 12
    else:
        previous_year = now.year
        previous_month = now.month - 1

    minimum = 70
    maximum = 200
    if record:
        minimum, maximum = record.getGraphInfo()
    return render_template(
        'index.html',
        monthName=calendar.month_name[now.month],
        daysInMonth=int(form.daysInMonth.data),
        minimum=minimum,
        maximum=maximum,
        target_morning=app.config['TARGET_MORNING'],
        target_evening=app.config['TARGET_EVENING'],
        next_year=next_year,
        next_month=next_month,
        previous_year=previous_year,
        previous_month=previous_month,
        form=form)

@app.route('/<handle>/<int:year>/<int:month>')
def indexWithHandleAndDate(handle, year, month):
    # next month
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1

    # previous month
    if month == 1:
        previous_year = year - 1
        previous_month = 12
    else:
        previous_year = year
        previous_month = month - 1

    form, record = populateMonthForm(handle, year, month)
    minimum = 70
    maximum = 200
    if record:
        minimum, maximum = record.getGraphInfo()
    return render_template(
        'index.html',
        monthName=calendar.month_name[month],
        daysInMonth=int(form.daysInMonth.data),
        minimum=minimum,
        maximum=maximum,
        target_morning=app.config['TARGET_MORNING'],
        target_evening=app.config['TARGET_EVENING'],
        next_year=next_year,
        next_month=next_month,
        previous_year=previous_year,
        previous_month=previous_month,
        form=form)

@app.route('/process-form', methods=['POST'])
def processForm():
    form = MonthForm()
    if form.validate_on_submit():
        BloodSugarMonth.save(form)
    return redirect(url_for('indexWithHandleAndDate', handle=form.handle.data, year=form.year.data, month=form.month.data))
