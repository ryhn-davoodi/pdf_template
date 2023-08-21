import pandas
from fpdf import FPDF
df=pandas.read_csv("topics.csv")
pdf=FPDF(orientation="P",unit="mm",format="A4")
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(size=24,family="Times",style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=18,txt=row["Topic"],align="L",ln=1)
    pdf.line(10,25,200,25)
    for number in range(1,row["Pages"]):
        pdf.add_page()

pdf.output("output.pdf")