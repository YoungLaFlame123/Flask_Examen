from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class ProductForm(FlaskForm):
    name = StringField('Nom du produit', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=500)])
    price = DecimalField('Prix', validators=[DataRequired()])
    image_url = StringField('URL de l\'image', validators=[DataRequired(), URL()])
    submit = SubmitField('Créer le produit')
