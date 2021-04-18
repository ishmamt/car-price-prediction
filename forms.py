from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange, DataRequired
from datetime import date


class InputForm(FlaskForm):
    years_old = IntegerField("What year was it released?", validators=[InputRequired(), NumberRange(min=1980, max=date.today().year)])
    km_driven = IntegerField("How many Kilometers has it driven?", validators=[InputRequired(), NumberRange(min=0, max=9999999)])
    owner_choices = ["New car", "1", "2", "3", "4 or more"]
    num_owners = SelectField("How many owners did it have?", choices=owner_choices, validators=[DataRequired()])
    fuel_choices = ["CNG", "Diesel", "Hybrid", "LPG", "Petrol"]
    fuel_type = SelectField("What type of fuel does it have?", choices=fuel_choices, validators=[DataRequired()])
    seller_choices = ["Dealer", "Individual", "Trustmark Dealer"]
    seller_type = SelectField("Who is selling it?", choices=seller_choices, validators=[DataRequired()])
    trans_choices = ["Automatic", "Manual"]
    trans_type = SelectField("What type of transmission does it have?", choices=trans_choices, validators=[DataRequired()])
    submit = SubmitField("Predict selling price")
