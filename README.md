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

5. Finally start the web server:

```
python run.py
```

### SQL Lite cmds
 
###### DB Creation
Identation is important

from application import app, db
from application.models import *

with app.app_context():
    db.create_all()
    guest_role = Role(name='guest')
    member_role = Role(name='member')
    admin_role = Role(name='admin')
    super_admin_role = Role(name='super-admin')
    db.session.add_all([guest_role, member_role, admin_role, super_admin_role])
    db.session.commit()

with app.app_context():
    db.create_all()
    roles = [
        {"name": "guest"},
        {"name": "member"},
        {"name": "admin"},
        {"name": "super-admin"}
    ]
    for role_data in roles:
        role = Role.query.filter_by(name=role_data["name"]).first()
        if not role:
            new_role = Role(name=role_data["name"])
            db.session.add(new_role)

        db.session.commit()

###### DB drop.

```
db.drop_all()
```

###### DB Migration, upgrade or change.

```
set FLASK_APP=run.py
flask db init
```
Si estás utilizando PowerShell, el comando sería:
```
$env:FLASK_APP = "run.py"
flask db init
```

```
flask db init
flask db migrate -m "some message"
flask db upgrade
```