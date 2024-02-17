# Define the parts of the document
document_intro = """<p>Quien suscribe, <span data-placeholder="2">[Nombre del Vendedor]</span>, de nacionalidad <span data-placeholder="3">[Nacionalidad]</span>, mayor de edad, de estado civil <span data-placeholder="5">[Estado Civil]</span>, domiciliado en la ciudad de <span data-placeholder="6">[Domicilio]</span>, y titular de la Cédula de Identidad No. <span data-placeholder="4">[Cédula de Identidad]</span>, quien a los efectos del presente documento se denominará “PARTE VENDEDORA”., La PARTE VENDEDORA por medio del presente documento expresamente declara: Que da en venta, pura y simple, perfecta e irrevocable a <span data-placeholder="18">[Nombre del Comprador]</span>, de nacionalidad <span data-placeholder="19">[Nacionalidad del Comprador]</span>, mayor de edad, de estado civil <span data-placeholder="21">[Estado Civil del Comprador]</span>, domiciliada en la ciudad de <span data-placeholder="22">[Domicilio del Comprador]</span>, titular de la Cédula de Identidad No. <span data-placeholder="20">[Cédula de Identidad del Comprador]</span>., quien a los efectos del presente documento se denominara “PARTE COMPRADORA”,</p>"""

vehicle_details = """<p>un vehículo de la exclusiva propiedad de la PARTE VENDEDORA, el referido vehículo tiene las siguientes características:</p>
<p>CLASE: <span data-placeholder="31">[Clase]</span>;</p>
<p>MODELO: <span data-placeholder="24">[Modelo]</span>;</p>
<p>MARCA: <span data-placeholder="23">[Marca]</span>;</p>
<p>AÑO: <span data-placeholder="28">[Año]</span>;</p>
<p>COLOR: <span data-placeholder="30">[Color]</span>;</p>
<p>USO: <span data-placeholder="32">[Uso]</span>;</p>
<p>TIPO: <span data-placeholder="29">[Tipo]</span>;</p>
<p>SERIAL DEL MOTOR: <span data-placeholder="26">[Serial del Motor]</span>;</p>
<p>SERIAL DE CARROCERÍA: <span data-placeholder="27">[Serial de Carrocería]</span>;</p>
<p>PLACA DEL VEHÍCULO: <span data-placeholder="25">[Placa]</span>.</p>"""

# Define sub-document types
titulo_inttt = """<p>Certificado de Registro de Vehículo No. <span data-placeholder="37">[Número de Certificado]</span>, número de forma <span data-placeholder="38">[Número de Forma]</span> emanado del Instituto Nacional de Tránsito y Transporte Terrestre de fecha de emisión el <span data-placeholder="17">[Fecha de Emisión]</span>.</p>"""
documento_notariado = """<p>documento de fecha <span data-placeholder="17">[Fecha de Emisión]</span> autenticado por ante <span data-placeholder="14">[Notaria]</span> del Municipio <span data-placeholder="40">[Municipio]</span> del <span data-placeholder="41">[Estado]</span> quedando inserto bajo el No. <span data-placeholder="15">[No. de Registro]</span>, Tomo <span data-placeholder="16">[Tomo]</span>..,</p>"""

# Define payment types
efectivo = """<p>los cuales recibe la PARTE VENDEDORA en este acto, de manos de la PARTE COMPRADORA en dinero en efectivo.</p>"""
transferencia = """<p>los cuales recibe la PARTE VENDEDORA en este acto, mediante la transferencia No. <span data-placeholder="43">[Número de Transferencia]</span> de la cuenta <span data-placeholder="42">[Cuenta que paga]</span> a la cuenta <span data-placeholder="44">[Cuenta que recibe]</span>.</p>"""
cheque = """<p>los cuales recibe LA PARTE VENDEDORA en este acto, de manos la PARTE COMPRADORA mediante instrumento <span data-placeholder="35">[Instrumento de Pago]</span> de la cuenta <span data-placeholder="42">[Cuenta que paga]</span> girado contra <span data-placeholder="36">[Banco]</span>.</p>"""

final_clause = """<p>Con el otorgamiento de este documento hago la tradición legal al comprador del bien vendido. La PARTE COMPRADORA, arriba identificada, declara: Que acepta la venta que se le hace y en los términos anteriormente expuestos. En la ciudad de su presentación, a la fecha de su otorgamiento.</p>
<p><span data-placeholder="2">[Firma del Vendedor]</span></p>
<p><span data-placeholder="18">[Firma del Comprador]</span></p>"""

# Assemble the templates
sub_document_types = [titulo_inttt, documento_notariado]
payment_types = [efectivo, cheque, transferencia]

templates = []

for sub_doc in sub_document_types:
    for payment in payment_types:
        template_text = f"{document_intro} {vehicle_details} {sub_doc}, {payment} {final_clause}"
        templates.append(template_text)

# Example to print or use the templates
for i, template in enumerate(templates, 1):
    print(f"Template {i}:\n{template}\n\n")


def get_assembled_templates():
    # Assemble the templates using the parts defined above
    sub_document_types = [('TITULO INTTT', titulo_inttt), ('DOCUMENTO NOTARIADO', documento_notariado)]
    payment_types = [('Efectivo', efectivo), ('Cheque', cheque), ('Transferencia', transferencia)]

    templates = []

    for sub_doc_name, sub_doc_content in sub_document_types:
        for payment_name, payment_content in payment_types:
            template_text = f"{document_intro} {vehicle_details} {sub_doc_content}, {payment_content} {final_clause}"
            templates.append((sub_doc_name, payment_name, template_text))

    return templates

# For testing or direct execution
if __name__ == '__main__':
    assembled_templates = get_assembled_templates()
    for i, (sub_doc_name, payment_name, template) in enumerate(assembled_templates, 1):
        print(f"Template {i} - Sub Doc: {sub_doc_name}, Payment: {payment_name}:\n{template}\n")