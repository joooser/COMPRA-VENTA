questions_buyer = [
    "Cual es el nombre del comprador?",
    "Cual es la nacionalidad del comprador?",
    "Cual es la cedula del comprador?",
    "Cual es el estado civil del comprador?",
    "Cual es el domicilio del comprador?"
]

buyer_answers = {}

for question in questions_buyer:
    answer = input(question)
    buyer_answers[question] = answer

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

car_answers = {}

for question in questions_car:
    answer = input(question)
    car_answers[question] = answer

questions_transaction = [
    "Cual es el precio del vehiculo?",
    "En que moneda se hizo el pago el vehiculo?",
    "Con que instrumento se pago el vehiculo?"
]

transaction_answers = {}

for question in questions_transaction:
    answer = input(question)
    transaction_answers[question] = answer