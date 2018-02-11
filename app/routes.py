from calendar import monthrange
from flask import render_template, redirect, url_for
from app import app
from app.forms import MonthForm
from app.models import BloodSugarMonth

import calendar
import datetime
import uuid

@app.route('/')
def index():
    return redirect(url_for('indexWithHandle', handle=str(uuid.uuid4())))

@app.route('/<handle>')
def indexWithHandle(handle):
    now = datetime.datetime.now()
    form = BloodSugarMonth.populateMonthForm(handle, now.year, now.month)
    return render_template(
        'index.html',
        monthName=calendar.month_name[now.month],
        daysInMonth=int(form.daysInMonth.data),
        form=form)

@app.route('/process-form', methods=['POST'])
def processForm():
    form = MonthForm()
    if form.validate_on_submit():
        BloodSugarMonth.save(form)
    return redirect(url_for('indexWithHandle', handle=form.handle.data))
