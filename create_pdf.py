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
#ln( 0 False, 1 True - move cursor down to next line)
#border ( 0 False , 1 True - add border around cell)

pdf.cell(120, 100, 'Hello World, working now', ln=True, border = 1)
pdf.cell(80, 10, 'Good night')

pdf.output('pdf_2.pdf')