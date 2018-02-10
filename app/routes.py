from calendar import monthrange
from flask import render_template, redirect, url_for
from app import app
from app.forms import MonthForm

import calendar
import datetime
import uuid

@app.route('/')
def index():
    return redirect(url_for('indexWithHandle', handle=str(uuid.uuid4())))

@app.route('/<handle>')
def indexWithHandle(handle):
    now = datetime.datetime.now()
    (weekday, daysInMonth) = monthrange(2018, 2)
    form = MonthForm()
    form.handle.data = handle
    form.year.data = now.year
    form.month.data = now.month
    form.daysInMonth.data = daysInMonth
    form.m1.data = 109
    form.e1.data = 120
    form.m2.data = 106
    form.e2.data = 116
    for field in form:
        print(field.name)
    return render_template(
        'index.html',
        year=now.year,
        monthName=calendar.month_name[now.month],
        daysInMonth=daysInMonth,
        form=form)

@app.route('/process-form', methods=['POST'])
def processForm():
    form = MonthForm()
    if form.validate_on_submit():
        print(form.handle.data)
    return 'Working...'
