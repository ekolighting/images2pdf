from fpdf import FPDF

title = '20,000 Leagues Under the sea'

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
        self.set_font('helvetica', 'B', 15)

        #Calculate widthe of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x( (doc_w - title_w) / 2 )

        #colors of frame, background and text
        self.set_draw_color(0, 80, 180) #border = blue
        self.set_fill_color(230, 230, 0) #background = yellow
        self.set_text_color(220, 50, 50) #text = red

        #Thickness of frame(border)
        self.set_line_width(1)


        #padding
        #self.cell(80)
        #Title
        self.cell(title_w, 10, title, border=True, ln=True, align='C', fill = True)
        #line break
        self.ln(10)

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
    def chapter_title(self, ch_num, ch_title):
        self.set_font('helvetica', '', 12)
        #bg color
        self.set_fill_color(200, 220, 255)

        chapter_title = f'Chapter {ch_num} : {ch_title}'
        self.cell(0, 10, chapter_title, ln=1, fill=1)
        self.ln()

    #chapter content
    def chapter_body(self, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')

        #set font
        self.set_font('times','', 12)
        self.multi_cell(0, 5, txt)

        self.ln()
        #end each chapter
        self.set_font('times', 'I', 12)
        self.cell(0,5, 'End of Chapter')

    def print_chapter(self, ch_num, ch_title, name):
        self.add_page()
        self.chapter_title(ch_num, ch_title)
        self.chapter_body(name)

#create FPDF object
pdf = PDF('P', 'mm', 'Letter')

#get total page numbers
pdf.alias_nb_pages()

#Set auto page break
pdf.set_auto_page_break(auto = True, margin =15)

# Add a page
#pdf.add_page()

pdf.print_chapter(1,'CAREER', 'chap_src/chap_03.txt')
pdf.print_chapter(2,'STAGECRAFT', 'chap_src/chap_04.txt')

print ('working')

pdf.output('pdf_4.pdf')