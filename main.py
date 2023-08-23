import pandas
from fpdf import FPDF
df=pandas.read_csv("topics.csv")
pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
for index,row in df.iterrows():
    # create first page of each topic and set the header
    pdf.add_page()
    pdf.set_font(size=24,family="Times",style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=18,txt=row["Topic"],align="L",ln=1)
    # pdf.line(10,25,200,25)
    # pdf.ln(10)
    for i in range(30,290,10):
        pdf.line(10, i, 200, i)

    # set the footer
    pdf.ln(252)
    pdf.set_font(size=10,family="times")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")


    # create other pages of each topic
    for number in range(1,row["Pages"]):
        pdf.add_page()
        for i in range(20, 290, 10):
            pdf.line(10, i, 200, i)

        pdf.ln(270)
        pdf.set_font(size=10, family="times")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")