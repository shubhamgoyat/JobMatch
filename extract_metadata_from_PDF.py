from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('edited_pdf_part1/7_Cisco_edited.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print doc.info  # The "Info" metadata