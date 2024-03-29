# COMPRA-VENTA

PROYECTO APP COMPRA VENTA DE VEHICULOS. 

Desarrollo de una app que, que permita realizar documentos "on the go"  de compraventa de vehiulos en Venezuela para personas naturales sin la necesidad de requerir a un abogado, utilizando tecnologia y firma digital como mecanismo para utenticar los documentos realizados.

1. El documento en una primera fase hara preguntas al cliente, y con el contenido de esas preguntas creara un string que sera el cuerpo del documento. que utilizara dentro de un documento pdf, que deberia compartirse o descargarse dentro del dispositivo del cliente.

2. Hasta ahora el codigo en python es en bruto, hay que aplicarle Programacion orientada a objetospara crear distintas funciones dentro del codigo que puedan llamarse.

3. Hay que averiguar como obtener una fiorma digital y como generar codigos QR aleatorios que apunten al url del documento en la web, cosa que pueda autenticarse la firma por el abogado.

4. En una sgeunda fase seria muy importante agregar Computer vision, para evitar la friccion y el error humano en el input de los datos.



## How To Run

0. On parent dyrectory.

1. Install `virtualenv`:

```
pip install virtualenv
```

2. Open a terminal in the project root directory and run:

```
virtualenv env
```

3. Then run the command:

```
.\env\Scripts\activate
```

4. Then install the dependencies:

```
pip install -r requirements.txt
```

5. Set Flaskapp env:

```
$env:FLASK_APP = "application:init_app"
or
export FLASK_APP = "application:init_app"
```

6. Initiate DB:

```
flask db init
flask db migrate -m "some message"
flask db upgrade
```

6. Seed the DB:

```
python -m scripts.seed_db
python -m scripts.seed_db_templates
```

7. Start App:

```
python run.py
```