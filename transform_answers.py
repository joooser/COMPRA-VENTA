# Replace placeholders in 'documento' with seller's answers
documento = documento.replace("[questions_seller1]", f"{seller_answers['Cual es el nombre del vendedor?'].upper()}")
documento = documento.replace("[questions_seller2]", f"{seller_answers['Cual es la nacionalidad del vendedor?'].upper()}")
documento = documento.replace("[questions_seller3]", f"{seller_answers['Cual es la cedula del vendedor?'].upper()}")
documento = documento.replace("[questions_seller4]", f"{seller_answers['Cual es el estado civil del vendedor?'].upper()}")
documento = documento.replace("[questions_seller5]", f"{seller_answers['Cual es el domicilio del vendedor?'].upper()}")

# Replace placeholders in 'documento' based on the document type
document_type = seller_answers["El vehiculo me pertenece en virtud de que documento?"]
if document_type == "titulo del inttt":
    documento = documento.replace("[questions_seller_a1]", f"{seller_answers['Cual es el numero del titulo del vehiculo?'].upper()}")
    documento = documento.replace("[questions_seller_a2]", f"{seller_answers['Cual es el numero de forma titulo del vehiculo?'].upper()}")
    documento = documento.replace("[questions_seller_a3]", f"{seller_answers['De que fecha es el titulo?'].upper()}")
else:
    documento = documento.replace("[questions_seller_b1]", f"{seller_answers['Que notaria autentico el documento?'].upper()}")
    documento = documento.replace("[questions_seller_b2]", f"{seller_answers['Bajo que numero quedo autenticado el documento?'].upper()}")
    documento = documento.replace("[questions_seller_b3]", f"{seller_answers['Bajo que tomo quedo autenticado el documento?'].upper()}")
    documento = documento.replace("[questions_seller_b4]", f"{seller_answers['En que fecha fue autenticado el documento?'].upper()}")

# Check the state civil status of the seller and replace placeholders if married
civil_status = seller_answers["Cual es el estado civil del vendedor?"]
if civil_status == "Casado":
    documento = documento.replace("[questions_seller_c1]", f"{seller_answers['Cual es el nombre del conyuge del vendedor?'].upper()}")
    documento = documento.replace("[questions_seller_c2]", f"{seller_answers['Cual es la nacionalidad del conyuge del vendedor?'].upper()}")
    documento = documento.replace("[questions_seller_c3]", f"{seller_answers['Cual es la cedula del conyuge del vendedor?'].upper()}")
    documento = documento.replace("[questions_seller_c4]", f"{seller_answers['Cual es el domicilio conyuge del vendedor?'].upper()}")

# Replace placeholders in 'documento' with buyer's answers
documento = documento.replace("[questions_buyer1]", f"{buyer_answers['Cual es el nombre del comprador?'].upper()}")
documento = documento.replace("[questions_buyer2]", f"{buyer_answers['Cual es la nacionalidad del comprador?'].upper()}")
documento = documento.replace("[questions_buyer3]", f"{buyer_answers['Cual es la cedula del comprador?'].upper()}")
documento = documento.replace("[questions_buyer4]", f"{buyer_answers['Cual es el estado civil del comprador?'].upper()}")
documento = documento.replace("[questions_buyer5]", f"{buyer_answers['Cual es el domicilio del comprador?'].upper()}")

# Replace placeholders in 'documento' with car details
documento = documento.replace("[questions_car1]", f"{car_answers['Cual es la marca del vehiculo?'].upper()}")
documento = documento.replace("[questions_car2]", f"{car_answers['Cual es el modelo del vehiculo?'].upper()}")
documento = documento.replace("[questions_car3]", f"{car_answers['Cual es la placa del vehiculo?'].upper()}")
documento = documento.replace("[questions_car4]", f"{car_answers['Cual es el serial motor del vehiculo?'].upper()}")
documento = documento.replace("[questions_car5]", f"{car_answers['Cual es el serial de caroceria del vehiculo?'].upper()}")
documento = documento.replace("[questions_car6]", f"{car_answers['Cual es el año del vehiculo?'].upper()}")
documento = documento.replace("[questions_car7]", f"{car_answers['Cual es el tipo del vehiculo?'].upper()}")
documento = documento.replace("[questions_car8]", f"{car_answers['Cual es el color del vehiculo?'].upper()}")
documento = documento.replace("[questions_car9]", f"{car_answers['Cual es la clase del vehiculo?'].upper()}")
documento = documento.replace("[questions_car10]", f"{car_answers['Cual es el uso del vehiculo?'].upper()}")

# Replace placeholders in 'documento' with transaction details
documento = documento.replace("[questions_transaction1]", f"{transaction_answers['Cual es el precio del vehiculo?'].upper()}")
documento = documento.replace("[questions_transaction2]", f"{transaction_answers['En que moneda se hizo el pago el vehiculo?'].upper()}")
documento = documento.replace("[questions_transaction3]", f"{transaction_answers['Con que instrumento se pago el vehiculo?'].upper()}")

# Finally, print or display the 'documento' string with all the answers
print(documento)