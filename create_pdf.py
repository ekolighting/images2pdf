from fpdf import FPDF

#Layout('P', 'L')
#Unit('mm', 'cm', 'in')
#format( 'A3', 'A4' default, 'A5', 'Letter', 'Legal', (100, 150))

#create FPDF object
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

#specify font
#font ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B'(bold), 'U' (underline), 'I'(italics), ''(regular), some combination ('BU')

pdf.set_font('helvetica', '', 16)

# Add text
#w = width
#h = height
pdf.cell(40, 10, 'Hello World, working now')

pdf.output('pdf_1.pdf')