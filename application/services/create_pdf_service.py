#import os
#from datetime import datetime
#from weasyprint import HTML
#from flask import current_app, current_app as app
#import logging
#
#def generate_pdf(content, document_id):
#    try:
#        today = datetime.utcnow()
#        year_dir, month_dir, day_dir = today.strftime('%Y'), today.strftime('%m'), today.strftime('%d')
#        date_str = today.strftime('%d%m%Y')
#        base_dir = current_app.config.get('PDF_STORAGE_PATH', 'G:/GitHub/COMPRA-VENTA/application/Storage/pdf_storage')
#        dir_path = os.path.join(base_dir, year_dir, month_dir, day_dir)
#        os.makedirs(dir_path, exist_ok=True)
#        filename = f"{document_id}_{date_str}.pdf"
#        file_path = os.path.join(dir_path, filename)
#        HTML(string=content).write_pdf(file_path)
#        return os.path.relpath(file_path, base_dir)
#    except Exception as e:
#        app.logger.error(f"PDF Generation Error: {e}")
#        return None
#