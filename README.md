# COMPRA-VENTA

PROYECTO APP COMPRA VENTA DE VEHICULOS. 

Desarrollo de una app que, que permita realizar documentos "on the go"  de compraventa de vehiulos en Venezuela para personas naturales sin la necesidad de requerir a un abogado, utilizando tecnologia y firma digital como mecanismo para utenticar los documentos realizados.

1. El documento en una primera fase hara preguntas al cliente, y con el contenido de esas preguntas creara un string que sera el cuerpo del documento. que utilizara dentro de un documento pdf, que deberia compartirse o descargarse dentro del dispositivo del cliente.

2. Hasta ahora el codigo en python es en bruto, hay que aplicarle Programacion orientada a objetospara crear distintas funciones dentro del codigo que puedan llamarse.

3. Hay que averiguar como obtener una fiorma digital y como generar codigos QR aleatorios que apunten al url del documento en la web, cosa que pueda autenticarse la firma por el abogado.

4. En una sgeunda fase seria muy importante agregar Computer vision, para evitar la friccion y el error humano en el input de los datos.


### Usage

1. Navigate to the project directory.

2. Build Docker img (-f for file. -t for tag):

docker build -f dockerfile_app -t mi-aplicacion-flask-1 .

3. run the recently created docker img:

docker run -p 5000:5000 mi-aplicacion-flask-1

4. In a browser go to:

http://localhost:5000/
