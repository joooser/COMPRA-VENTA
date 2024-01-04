# COMPRA-VENTA
PROYECTO APP COMPRA VENTA DE VEHICULOS. 

Desarrollo de una app we, que permita realizar documentos "on the go"  de compraventa de vehiulos en Venezuela para personas naturales sin la necesidad de requerir a un abogado,
utilizando tecnologia y firma digital como mecanismo para utenticar los documentos realizados.

1. El documento en una primera fase hara preguntas al cliente, y con el contenido de esas preguntas creara un string que sera el cuerpo del documento. que utilizara dentro de un
   documento pdf, que deberia compartirse o descargarse dentro del dispositivo del cliente.
2. Hasta ahora el codigo en python es en bruto, hay que aplicarle Programacion orientada a objetospara crear distintas funciones dentro del codigo que puedan llamarse.
3. Hay que averiguar como obtener una fiorma digital y como generar codigos QR aleatorios que apunten al url del documento en la web, cosa que pueda autenticarse la firma por el
   abogado.
5. En una sgeunda fase seria muy importante agregar Computer vision, para evitar la friccion y el error humano en el input de los datos.


### Usage

1. Navigate to the project directory.history

2. Build Docker img (-f for file. -t for tag):

docker build -f dockerfile -t dockerhost .

3. run the recently created docker img:

docker run -v ./app:/gpt-pilot/workspace -v /var/run/docker.sock:/var/run/docker.sock --privileged dockerhost

4. In a browser go to:

http://localhost:7681/

5. run:

python db_init.py (initialize the database)
python main.py (start GPT Pilot). For advance architecture python main.py advanced=True

6. follow gpt-pilot instructions.

7. to enter our environment or in this case our docker host in a CLI do:

docker ps (look for the line with IMAGE == dockerhost and copy "CONTAINER ID")

8. to enter the container run (The container ID goes without ""):

docker exec -it "CONTAINER ID" /bin/bash 


#### For more info. 
Source: https://github.com/Pythagora-io/gpt-pilot#how-to-start-using-gpt-pilot