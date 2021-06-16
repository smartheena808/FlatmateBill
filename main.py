from flatReport import PdfReport
from flatmate import Bill, Flatmate
from filesharer import FileSharer

def main():
    print("Flatmate Bill App")
    print("=================")
    bill_amount = float(input("Enter the bill amount:$"))
    bill_period = input("Enter the bill's period, such as March 2021: ")
    the_bill = Bill(bill_amount, bill_period)

    # Enter the flatmate's details
    flatmate1_name = input("Enter firt flatmate name: ")
    flatmate1_stay = int(input(f"How long {flatmate1_name} stay in the house: "))
    flatmate1 = Flatmate(flatmate1_name, flatmate1_stay)

    flatmate2_name = input("Enter another flatmate name: ")
    flatmate2_stay = int(input(f"How long {flatmate2_name} stay in the house: "))
    flatmate2 = Flatmate(flatmate2_name, flatmate2_stay)

    # Calculate the bill
    print("\nThe amount of bill that need to be paid each:")
    print(f"{flatmate1.name} pays:$ {round(flatmate1.pays(the_bill, flatmate2),2)}")
    print(f"{flatmate2.name} pays:$ {round(flatmate2.pays(the_bill, flatmate1),2)}")

    # Generate the report bill
    report = PdfReport(f'{the_bill.period}.pdf')
    report.generate(flatmate1, flatmate2, the_bill)

    # Create filelink to open the pdf report in webbrowser
    print("You can download the report from link below:")
    file_share = FileSharer(filepath=report.filename)
    print(file_share.share())

if __name__ == '__main__': main()
