questions_seller = [
    "Cual es el nombre del vendedor?",
    "Cual es la nacionalidad del vendedor?",
    "Cual es la cedula del vendedor?",
    "Cual es el estado civil del vendedor?",
    "Cual es el domicilio del vendedor?",
]

seller_answers = {}

for question in questions_seller:
    answer = input(question)
    # Store the answer in the seller_answers dictionary
    seller_answers[question] = answer

# Handle the special case for the document type
# Display a dropdown and save the answer
document_type = input("El vehiculo me pertenece en virtud de que documento? (Elija 'titulo del inttt' o 'documento notariado')")
seller_answers["El vehiculo me pertenece en virtud de que documento?"] = document_type

if document_type == "titulo del inttt":
    # Ask questions from questions_seller_a
    questions_seller_a = [
        "Cual es el numero del titulo del vehiculo?",
        "Cual es el numero de forma titulo del vehiculo?",
        "De que fecha es el titulo?"
    ]
    for question in questions_seller_a:
        answer = input(question)
        seller_answers[question] = answer
else:
    # Ask questions from questions_seller_b
    questions_seller_b = [
        "Que notaria autentico el documento?",
        "Bajo que numero quedo autenticado el documento?",
        "Bajo que tomo quedo autenticado el documento?",
        "En que fecha fue autenticado el documento?"
    ]
    for question in questions_seller_b:
        answer = input(question)
        seller_answers[question] = answer

# Check the state civil status of the seller
civil_status = seller_answers["Cual es el estado civil del vendedor?"]

if civil_status == "Casado":
    questions_seller_c = [
        "Cual es el nombre del conyuge del vendedor?",
        "Cual es la nacionalidad del conyuge del vendedor?",
        "Cual es la cedula del conyuge del vendedor?",
        "Cual es el domicilio conyuge del vendedor?",
    ]

    for question in questions_seller_c:
        answer = input(question)
        seller_answers[question] = answer