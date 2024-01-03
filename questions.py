from IPython.display import HTML, display, clear_output

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
    "Bajo que numero quedo autenticado el el documento?",
    "Bajo que tomo quedo autenticado el el documento?",
    "en que fecha fue autenticado el documento?"
]

questions_seller_c = [
    "Cual es el nombre del conyuge del vendedor?",
    "Cual es la nacionalidad del conyuge del vendedor?",
    "Cual es la cedula del conyuge del vendedor?",
    "Cual es el domicilio conyuge del vendedor?",
]

questions_buyer = [
    "Cual es el nombre del comprador?",
    "Cual es la nacionalidad del comprador?",
    "Cual es la cedula del comprador?",
    "Cual es el estado civil del comprador?",
    "Cual es el domicilio del comprador?"
]

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

questions_transaction = [
    "Cual es el precio del vehiculo?",
    "En que moneda se hizo el pago el vehiculo?",
    "con que instrumento se pago el vehiculo?"
]

documento = "Yo, [questions_seller1], de nacionalidad [questions_seller2], mayor de edad, de estado civil [questions_seller4], domiciliado en [questions_seller5], y titular de la Cédula de Identidad No. [questions_seller3], por medio del presente documento expresamente declaro: Que doy en venta, pura y simple, perfecta e irrevocable a la ciudadana [questions_buyer1], de nacionalidad [questions_buyer2], mayor de edad, de estado civil [questions_buyer4], domiciliada en [questions_buyer5], titular de la Cédula de Identidad No.[questions_buyer3]., un vehículo de mi exclusiva propiedad, de las siguientes características: CLASE: [questions_car9]; MODELO: [questions_car2]; MARCA: [questions_car1]; AÑO: [questions_car6]; COLOR: [questions_car8]; USO: [questions_car10]; TIPO: [questions_car7]; SERIAL DEL MOTOR: [questions_car4]; SERIAL DE CARROCERÍA: [questions_car5]; PLACA DEL VEHÍCULO: [questions_car3]. El referido vehículo me pertenece según se evidencia de Certificado de Registro de Vehículo No. [questions_seller_a1], número de forma [questions_seller_a2] emanado del Instituto Nacional de Tránsito y Transporte Terrestre de fecha de emisión el [questions_seller_a3]., dicho vehículo se encuentra libre de gravámenes y nada debe por concepto de  impuestos nacionales, ni municipales. El precio de esta venta es por la cantidad de [questions_transaction1] [questions_transaction2], los cuales recibo en este acto, de manos del comprador mediante instrumento [questions_transaction3] girado contra BANESCO Banco Universal. Con el otorgamiento de este documento hago la tradición legal al comprador del bien vendido. Yo, [questions_buyer1], arriba identificada, declaro: Que acepto la venta que se me hace y en los términos anteriormente expuestos. En la ciudad de San Antonio de Los Altos, en la fecha de su otorgamiento. \n\n[questions_seller1]     \n                  [questions_buyer1]"


### Tengo estas variables que son preguntas, quiero hacer un workflow con las preguntas: Primero hacer las preguntas de questions_seller,
### cada pregunta tendra un input box, la ultima pregunta de questions_seller ( "El vehiculo me pertenece en virtud de que documento?") no tendra un input box sino una lista desplegable con dos opciones:
### "titulo del inttt", "documento notariado", si la respuesta es "titulo del inttt" se haran las preguntas questions_seller_a, si la respuesta es "documento notariado" se haran las preguntas questions_seller_b, nunca ambos set de preguntas.
### si a la pregunta ( "Cual es el estado civil del vendedor?") la respuesta es "Casado" se hacen las preguntas de question_seller_c, en cualquir otro caso no.
### luego se haran las preguntas de questions_buyer, questions_car, questions_transactions.
### cada respuesta se guardara con un nombre de variable: Por ejemplo: questions_seller1, questions_seller2 ,questions_seller3, etc
### luego con cada respuesta se realizara un insert en el string documento