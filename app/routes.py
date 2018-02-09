from calendar import monthrange
from flask import render_template, redirect, url_for
from app import app

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
    print(now.year, now.month, daysInMonth)
    return render_template(
        'index.html', 
        handle=handle,
        year=now.year,
        month=now.month,
        monthName=calendar.month_name[now.month],
        daysInMonth=daysInMonth)
