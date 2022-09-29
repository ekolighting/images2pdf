from fpdf import FPDF
import os
import pathlib

root_PATH = 'img_src/'
sub_PATH = '111_harbor_painter(0)'
black_bar = root_PATH + 'black_bar.png'
gray_bar = root_PATH + 'gray_bar.png'
white_bar = root_PATH + 'white_bar.png'


full_PATH = root_PATH + sub_PATH

images_list = []
file_list = os.listdir(full_PATH)
file_list.sort()
for f in file_list:
    if pathlib.Path(f).suffix == '.png':
        images_list.append(f)

print ('IMG LIST !!! ',images_list)
title = 'YEAH PLUS COLLECTION : Beyond the Imagination Series'

# Add text
#w = width
#h = height
#ln( 0 False, 1 True - move cursor down to next line)
#border ( 0 False , 1 True - add border around cell)

#Layout('P', 'L')
#Unit('mm', 'cm', 'in')
#format( 'A3', 'A4' default, 'A5', 'Letter', 'Legal', (100, 150))

#specify font
#font ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B'(bold), 'U' (underline), 'I'(italics), ''(regular), some combination ('BU')


class PDF(FPDF):
    def header(self):
        #self.image('img_src/yeah_bi.png', 10, 8, 25)

        #font
        self.set_font('helvetica', 'B', 16)

        #Calculate widthe of title and position
        title_w = self.get_string_width(title) + 30
        doc_w = self.w
        self.set_x( (doc_w - title_w) / 2 )

        #colors of frame, background and text
        self.set_draw_color(67, 117, 181) #border = blue
        self.set_fill_color(255, 225, 90) #background = yellow
        self.set_text_color(214, 81, 70) #text = red

        #Thickness of frame(border)
        self.set_line_width(1)

        #padding
        #self.cell(80)
        #Title
        self.cell(title_w, 10, title, border=True, ln=True, align='C', fill = True)
        #line break
        self.ln(3)

    def footer(self):
        #set position of the footer
        self.set_y(-15)
        #set font
        self.set_font('helvetica', 'I', 10)
        #set font color grey
        self.set_text_color(170,170,170)
        #page number
        self.cell(0,10, f'Page {self.page_no()}/{{nb}}', align = 'C')

    #Adding chapter title to start of each chapter
    def chapter_title(self, ch_num, ch_title, link):
        #Set link location
        self.set_link(link)

        self.set_font('helvetica', '', 12)
        #bg color
        self.set_fill_color(200, 220, 255)
        chapter_title = f'IAMGE {ch_num} : {ch_title}'
        self.cell(0, 10, chapter_title, ln=1, fill=0, align='C')
        self.ln(1)

    def add_blackbar(self):
        pdf.image(white_bar, x = -0.5, w= pdf.w +1)

    #chapter content
    def chapter_body(self, img_path):
        #set font
        self.set_font('times','', 12)
 
        #Add image
        self.add_blackbar()
        pdf.image(img_path, x = -0.5, w= pdf.w +1)
        self.add_blackbar()

        #self.ln()
        #end each chapter
        #self.set_font('times', 'I', 12)
        #self.cell(0,5, 'End of Chapter')
    
    def add_blank(self):
        #set fill color
        self.set_fill_color(0,0,0)
        self.cell(0, 10, 'TEST', fill = True)
        self.ln(3)

    def print_chapter(self, ch_num, ch_title, img_path, link):
        self.add_page()
        self.chapter_title(ch_num, ch_title, link)
        self.chapter_body(img_path)

#create FPDF object
pdf = PDF('L', 'mm', 'A4')

#Add metadata
pdf.set_title(title)
pdf.set_author('YEAH PLUS')

# Link
website = 'http://yeahplus.co.kr/'
ch1_link = pdf.add_link()
ch2_link = pdf.add_link()


#get total page numbers
pdf.alias_nb_pages()

#Set auto page break
pdf.set_auto_page_break(auto = True, margin =15)

# Add a page
pdf.add_page()
pdf.image('img_src/yeah_bi.png', x = (pdf.x * 16- pdf.x) / 2, w = pdf.x * 16)

# Attach Links
'''
pdf.cell(0,10, 'Text Source', ln = 1, link = website)
pdf.cell(0,10, 'Chapter 1', ln = 1, link = ch1_link)
pdf.cell(0,10, 'Chapter 2', ln = 1, link = ch2_link)
'''

for i, img in enumerate(images_list):
    img_path = img_path = full_PATH + '/' + img
    pdf.print_chapter(i,img, img_path, ch1_link)

pdf.output(sub_PATH + '.pdf')