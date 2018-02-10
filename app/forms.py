from flask_wtf import FlaskForm
from wtforms import FieldList, HiddenField, IntegerField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, UUID

class DayForm(FlaskForm):
    morning = IntegerField('morning')
    evening = IntegerField('evening')

class MonthForm(FlaskForm):
    handle = HiddenField('handle', validators=[DataRequired(), UUID()])
    month = HiddenField('month', validators=[DataRequired()])
    year = HiddenField('year', validators=[DataRequired()])
    daysInMonth = HiddenField('daysInMonth', validators=[DataRequired()])
    for n in range(1, 31):
        locals()[''.join("m"+str(n))] = StringField('', [ validators.Length(min=2, max=3)])
        locals()[''.join("e"+str(n))] = StringField('', [ validators.Length(min=2, max=3)])
    submit = SubmitField('Save')
