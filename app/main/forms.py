from flask_wtf import FlaskForm
from wtforms import DateTimeField, StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class InputData(FlaskForm):
    startdate = DateTimeField('开始时间', validators=[Required()])
    enddate = StringField('结束时间', validators=None)
    address = StringField('抢修地址', validators=[Required()])
    area = TextAreaField('影响范围', validators=[Required()])
    type_id = SelectField('类型', choices=[['1','抢修停水'],['2','计划停水']])
    submit = SubmitField('确认提交')
    
class PostForm(FlaskForm):

    submit = SubmitField('Submit')