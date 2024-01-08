# variables.py
import logging

# ################## Questions for Seller ##################
questions_seller = [
    "Cual es el nombre del vendedor?",
    "Cual es la nacionalidad del vendedor?",
    "Cual es la cedula del vendedor?",
    "Cual es el estado civil del vendedor?",
    "Cual es el domicilio del vendedor?",
    "El vehiculo me pertenece en virtud de que documento?",
]

questions_seller_a = [
    "Cual es el numero del titulo del vehiculo?",
    "Cual es el numero de forma titulo del vehiculo?",
    "De que fecha es el titulo?"
]

questions_seller_b = [
    "Que notaria autentico el documento?",
    "Bajo que numero quedo autenticado el documento?",
    "Bajo que tomo quedo autenticado el documento?",
    "En que fecha fue autenticado el documento?"
]

questions_seller_c = [
    "Cual es el nombre del conyuge del vendedor?",
    "Cual es la nacionalidad del conyuge del vendedor?",
    "Cual es la cedula del conyuge del vendedor?",
    "Cual es el domicilio conyuge del vendedor?",
]

# ################## Questions for Buyer ##################
questions_buyer = [
    "Cual es el nombre del comprador?",
    "Cual es la nacionalidad del comprador?",
    "Cual es la cedula del comprador?",
    "Cual es el estado civil del comprador?",
    "Cual es el domicilio del comprador?"
]

# ################## Questions for Car ##################
questions_car = [
    "Cual es la marca del vehiculo?",
    "Cual es el modelo del vehiculo?",
    "Cual es la placa del vehiculo?",
    "Cual es el serial motor del vehiculo?",
    "Cual es el serial de caroceria del vehiculo?",
    "Cual es el año del vehiculo?",
    "Cual es el tipo del vehiculo?",
    "Cual es el color del vehiculo?",
    "Cual es la clase del vehiculo?",
    "Cual es el uso del vehiculo?"
]

# ################## Questions for Transaction ##################
questions_transaction = [
    "Cual es el precio del vehiculo?",
    "En que moneda se hizo el pago el vehiculo?",
    "Con que instrumento se pago el vehiculo?"
]

# ################## Document Template ##################
documento = """
Yo, [questions_seller1], de nacionalidad [questions_seller2], mayor de edad, de estado civil [questions_seller4], domiciliado en [questions_seller5], y titular de la Cédula de Identidad No. [questions_seller3], por medio del presente documento expresamente declaro: Que doy en venta, pura y simple, perfecta e irrevocable a la ciudadana [questions_buyer1], de nacionalidad [questions_buyer2], mayor de edad, de estado civil [questions_buyer4], domiciliada en [questions_buyer5], titular de la Cédula de Identidad No.[questions_buyer3].
\nUn vehículo de mi exclusiva propiedad, de las siguientes características: CLASE: [questions_car9]; MODELO: [questions_car2]; MARCA: [questions_car1]; AÑO: [questions_car6]; COLOR: [questions_car8]; USO: [questions_car10]; TIPO: [questions_car7]; SERIAL DEL MOTOR: [questions_car4]; SERIAL DE CARROCERÍA: [questions_car5]; PLACA DEL VEHÍCULO: [questions_car3].
\nEl referido vehículo me pertenece según se evidencia de Certificado de Registro de Vehículo No. [questions_seller_a1], número de forma [questions_seller_a2] emanado del Instituto Nacional de Tránsito y Transporte Terrestre de fecha de emisión el [questions_seller_a3]., dicho vehículo se encuentra libre de gravámenes y nada debe por concepto de impuestos nacionales, ni municipales.
\nEl precio de esta venta es por la cantidad de [questions_transaction1] [questions_transaction2], los cuales recibo en este acto, de manos del comprador mediante instrumento [questions_transaction3] girado contra BANESCO Banco Universal.
\nCon el otorgamiento de este documento hago la tradición legal al comprador del bien vendido.
\nYo, [questions_buyer1], arriba identificada, declaro: Que acepto la venta que se me hace y en los términos anteriormente expuestos.
\nEn la ciudad de San Antonio de Los Altos, en la fecha de su otorgamiento.
\n\n[questions_seller1]
\n\n[questions_buyer1]
"""



logging.basicConfig(filename='app.log', level=logging.INFO)

# Use logging in your application
logging.info('Info message')
logging.error('Error message')