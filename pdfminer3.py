from io import StringIO
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.pdfpage import PDFPage

def extract_text(file_path):
    output_string = StringIO()

    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    with open(file_path, 'rb') as file:
        pages = PDFPage.get_pages(file)
        for page in pages:
            interpreter.process_page(page)

    text = output_string.getvalue()
    return text