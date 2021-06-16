import webbrowser
import os
from fpdf import FPDF
import datetime

class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates,
    such as their names, their due amounts and the period of
    the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """
        Generate a pdf report for the bill in certain of period.
        :rtype: pdf file
        """
        flatmate1_to_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_to_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        # Create a new pdf object
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        # Create a new page
        pdf.add_page()
        # Add logo
        pdf.image('files/logo.png')

        # Adding the bill title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)  # ln to change to new line

        # Adding the period of the bill
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Adding the flatmate's name and bill that have to be paid
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=f"${flatmate1_to_pay}", border=0, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=f"${flatmate2_to_pay}", border=0, ln=1)

        # Position at 1.5 cm from bottom
        #pdf.set_y(-15)
        # Arial italic 8
        pdf.set_font('Arial', 'I', 8)
        # Page number
        pdf.cell(0, 10, f"generated @: {(datetime.datetime.now()).strftime('%c')}", 0, 0, 'C')

        # Change the directory to files and save the pdf file
        os.chdir('files')
        pdf.output(self.filename)
        # Open the pdf file automatically
        webbrowser.open(self.filename)