# create_pdf.py
from fpdf import FPDF

class PDFWithHeader(FPDF):
    def header(self):
        # Asegúrate de que las rutas a las imágenes sean correctas y accesibles
        img_a_path = "path_to_image_a.jpg"
        img_b_path = "path_to_image_b.jpg"

        # Colocación de imágenes en el encabezado
        self.image(img_a_path, 10, 8, 33)
        self.image(img_b_path, 165, 8, 33)

    def footer(self):
        # Opcional: Agregar un pie de página si es necesario
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def create_pdf(documento, output_filename):
    pdf = PDFWithHeader()
    pdf.add_page()

    # Establecer fuente y agregar el texto del documento
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, documento)
    
    pdf.output(output_filename)

# Ejemplo de uso:
# create_pdf(documento_final, "output.pdf")