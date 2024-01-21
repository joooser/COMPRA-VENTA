from .base import (
    FlaskForm,
    StringField,
    IntegerField,
    SelectField,
    DateField,
    validators,
    RecaptchaField,
    SubmitField,
    DataRequired,
    Length,
    FloatField
    )

class VehicleSaleForm(FlaskForm):

    # Questions for the seller
    seller_name = StringField('Cual es el nombre del vendedor?', validators=[DataRequired(), Length(min=2, max=40)])
    seller_nationality = StringField('Cual es la nacionalidad del vendedor?', validators=[DataRequired(), Length(max=50)])
    seller_id = StringField('Cual es la cedula del vendedor?', validators=[DataRequired(), Length(min=2, max=10)])
    seller_marital_status = SelectField('Cual es el estado civil del vendedor?', choices=[('soltero(a)', 'Soltero(a)'), ('casado(a)', 'Casado(a)'), ('viudo(a)', 'Viudo(a)')], validators=[DataRequired()])
    seller_address = StringField('Cual es el domicilio del vendedor?', validators=[DataRequired(), Length(max=100)])
    vehicle_document_type = SelectField('El vehiculo me pertenece en virtud de que documento?', choices=[('titulo_inttt', 'Titulo INTTT'), ('documento_notariado', 'Documento Notariado')], validators=[DataRequired()])
        
    # Additional questions if the document type is 'titulo inttt'
    vehicle_title_number = StringField('Cual es el numero del titulo del vehiculo?', validators=[DataRequired(), Length(max=20)])
    vehicle_form_number = StringField('Cual es el numero de forma titulo del vehiculo?', validators=[DataRequired(), Length(max=20)])
    vehicle_title_date = DateField('De que fecha es el titulo?', format='%d/%m/%Y', validators=[DataRequired()])
    
    # Additional questions if the document type is 'documento notariado'
    notary_name = StringField('Que notaria autentico el documento?', validators=[DataRequired(), Length(max=50)])
    document_authentication_number = IntegerField('Bajo que numero quedo autenticado el documento?', validators=[DataRequired()])
    document_authentication_volume = SelectField('Bajo que tomo quedo autenticado el documento?', choices=[('1ro', 'Primero'), ('2do', 'Segundo'), ('3ro', 'Tercero')], validators=[DataRequired()])
    document_authentication_date = DateField('En que fecha fue autenticado el documento?', format='%d/%m/%Y', validators=[DataRequired()])

    # Fields for questions_seller_c
    seller_spouse_name = StringField('Cual es el nombre del conyuge del vendedor?', validators=[DataRequired(), Length(max=40)])
    seller_spouse_nationality = StringField('Cual es la nacionalidad del conyuge del vendedor?', validators=[DataRequired(), Length(max=50)])
    seller_spouse_id = StringField('Cual es la cedula del conyuge del vendedor?', validators=[DataRequired(), Length(max=10)])
    seller_spouse_address = StringField('Cual es el domicilio conyuge del vendedor?', validators=[DataRequired(), Length(max=100)])

    # Fields for questions_buyer
    buyer_name = StringField('Cual es el nombre del comprador?', validators=[DataRequired(), Length(max=40)])
    buyer_nationality = StringField('Cual es la nacionalidad del comprador?', validators=[DataRequired(), Length(max=50)])
    buyer_id = StringField('Cual es la cedula del comprador?', validators=[DataRequired(), Length(max=10)])
    buyer_marital_status = SelectField('Cual es el estado civil del comprador?', choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('viudo', 'Viudo')], validators=[DataRequired()])
    buyer_address = StringField('Cual es el domicilio del comprador?', validators=[DataRequired(), Length(max=100)])

    # Fields for questions_car
    car_brand = StringField('Cual es la marca del vehiculo?', validators=[DataRequired(), Length(max=50)])
    car_model = StringField('Cual es el modelo del vehiculo?', validators=[DataRequired(), Length(max=50)])
    car_plate = StringField('Cual es la placa del vehiculo?', validators=[DataRequired(), Length(max=10)])
    car_engine_serial = StringField('Cual es el serial motor del vehiculo?', validators=[DataRequired(), Length(max=20)])
    car_chassis_serial = StringField('Cual es el serial de carroceria del vehiculo?', validators=[DataRequired(), Length(max=20)])
    car_year = IntegerField('Cual es el año del vehiculo?', validators=[DataRequired()])
    car_type = StringField('Cual es el tipo del vehiculo?', validators=[DataRequired(), Length(max=50)])
    car_color = StringField('Cual es el color del vehiculo?', validators=[DataRequired(), Length(max=20)])
    car_class = StringField('Cual es la clase del vehiculo?', validators=[DataRequired(), Length(max=50)])
    car_use = StringField('Cual es el uso del vehiculo?', validators=[DataRequired(), Length(max=50)])

    # Fields for questions_transaction
    vehicle_price = FloatField('Cual es el precio del vehiculo?', validators=[DataRequired()])
    transaction_currency = StringField('En que moneda se hizo el pago del vehiculo?', validators=[DataRequired(), Length(max=20)])
    payment_instrument = StringField('Con que instrumento se pago el vehiculo?', validators=[DataRequired(), Length(max=50)])
    bank = StringField('En que Banco?', validators=[DataRequired(), Length(max=50)])
    city = StringField('En que ciudad realiza la transacción?', validators=[DataRequired(), Length(max=50)])

    #recaptcha = RecaptchaField()
    submit    = SubmitField(label='Crear')