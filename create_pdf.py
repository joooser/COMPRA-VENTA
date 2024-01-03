from fpdf import FPDF

class PDFWithHeader(FPDF):
    def header(self):
        # Image "a" centrada
        img_a_path = "/content/b.jpg"  # Reemplaza con la ruta de tu imagen "a"
        self.image(img_a_path, (self.w - 40) / 2, 10, 40)

        # Image "b" justificada a la derecha
        img_b_path = "/content/gnido logo.png"  # Reemplaza con la ruta de tu imagen "b"
        self.image(img_b_path, self.w - 50, 10, 40)

        # Move to the bottom of the images
        self.ln(35)



    def chapter_body(self, body):
        # Body text
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_pdf(output_filename):
    pdf = PDFWithHeader()

    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)


    text = documento
    pdf.chapter_body(text)

    pdf.output(output_filename)

if __name__ == "__main__":
    create_pdf("output.pdf")