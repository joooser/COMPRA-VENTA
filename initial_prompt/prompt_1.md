Task: Build an App, it will write a legal contract of a car sale between 2 persons, it will recieve identification from the 2 persons, the data about the car that it is being sold, the price and the currency, the the app is going to make insertions in a pre-written model contract, the result is a fully complete car-sale contract.
Details about the task: 
1.You are going to have this questions: 
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
some questions can be asked or not depending on a previous question answer:
1. questions_seller_c is gonna be asked only if questions_seller4 is "casado" regardless of the use of capital letters.
2. questions_seller5 have only two options in a dropdown menu: "Titulo INTTT" or "Documento Notariado", if the answer is "titulo inttt" questions_seller_a are going to be answered. if thw answer is "Documento Notariado" then the questions to ask are questions_seller_b


All this information is going to be taken via input bar from the front end. but some of them can be taken scanning or uploading photo, in the cases of questions_seller, questions_buyer and questions_seller_c	the info can be taking uploadng a photo of the id card for every set. and questions_car can be taken via uploading the car title photography.

After taken the information user is going to be sent to the payment page. and then we continue with the workflow:

All this information is gonna be taken in the frontend, fter that all this info is gonna be send to the backend in a json file and it is going to be inserted in database and in a document in the following way: 

	documento = "Yo, [questions_seller1], de nacionalidad [questions_seller2], mayor de edad, de estado civil [questions_seller4], domiciliado en [questions_seller5], y titular de la Cédula de Identidad No. [questions_seller3], por medio del presente documento expresamente declaro: Que doy en venta, pura y simple, perfecta e irrevocable a la ciudadana [questions_buyer1], de nacionalidad [questions_buyer2], mayor de edad, de estado civil [questions_buyer4], domiciliada en [questions_buyer5], titular de la Cédula de Identidad No.[questions_buyer3]., un vehículo de mi exclusiva propiedad, de las siguientes características: CLASE: [questions_car9]; MODELO: [questions_car2]; MARCA: [questions_car1]; AÑO: [questions_car6]; COLOR: [questions_car8]; USO: [questions_car10]; TIPO: [questions_car7]; SERIAL DEL MOTOR: [questions_car4]; SERIAL DE CARROCERÍA: [questions_car5]; PLACA DEL VEHÍCULO: [questions_car3]. El referido vehículo me pertenece según se evidencia de Certificado de Registro de Vehículo No. [questions_seller_a1], número de forma [questions_seller_a2] emanado del Instituto Nacional de Tránsito y Transporte Terrestre de fecha de emisión el [questions_seller_a3]., dicho vehículo se encuentra libre de gravámenes y nada debe por concepto de  impuestos nacionales, ni municipales. El precio de esta venta es por la cantidad de [questions_transaction1] [questions_transaction2], los cuales recibo en este acto, de manos del comprador mediante instrumento [questions_transaction3] girado contra BANESCO Banco Universal. Con el otorgamiento de este documento hago la tradición legal al comprador del bien vendido. Yo, [questions_buyer1], arriba identificada, declaro: Que acepto la venta que se me hace y en los términos anteriormente expuestos. En la ciudad de San Antonio de Los Altos, en la fecha de su otorgamiento. \n\n[questions_seller1]     \n                  [questions_buyer1]"

After the document has all the information inserted, there is going to other steps: 

	1. it will be created an url and a name for the document that is not created yet.
	2. create a QR code pointing to the url in the numeral befor this.
	3. create a pdf document, with 3 images in the header, the qr code on the left, an image on the center and an image on the right.