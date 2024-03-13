import tkinter as tk
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

class RICAService:
    def __init__(self):
        self.applicant_citizenship = None
        self.identification_document_number = None
        self.other_names = None
        self.surname = None
        self.nationality = None
        self.passport_number = None
        self.phone_number = None
        self.email_address = None
        self.business_owner_address = None
        self.business_type = None
        self.company_name = None
        self.tin_number = None
        self.registration_date = None
        self.business_address = None
        self.purpose_of_importation = None
        self.specify_purpose = None
        self.product_category = None
        self.product_name = None
        self.weight_kg = None
        self.description_of_products = None
        self.unit_of_measurement = None
        self.quantity_of_products = None

    def get_applicant_details(self, form_data=None):
        if form_data:
            self.applicant_citizenship = form_data.get("citizenship")
            self.identification_document_number = form_data.get("identification_document_number")
            self.other_names = form_data.get("other_names")
            self.surname = form_data.get("surname")
            self.nationality = form_data.get("nationality")
            self.passport_number = form_data.get("passport_number")
        else:
            print(" Welcome to RICA Service application Portal ")
            print("Enter Applicant Details:")
            self.applicant_citizenship = input("Citizenship (Rwandan/Foreigner): ").capitalize()
            self.identification_document_number = input("Identification Document Number: ")
            self.other_names = input(" Given Name: ")
            self.surname = input("Surname: ")
            self.nationality = input("Nationality: ")

            if self.applicant_citizenship == 'Foreigner':
                self.passport_number = input("Passport Number: ")
            elif self.applicant_citizenship == "Rwandan":
                self.passport_number = input(" National Identification Number ")

    def get_contact_details(self, form_data=None):
        if form_data:
            self.phone_number = form_data.get("phone_number")
            self.email_address = form_data.get("email_address")
        else:
            print("\nEnter Contact Details:")
            self.phone_number = input("Phone Number: ")
            self.email_address = input("Email Address: ")

    def get_business_details(self, form_data=None):
        if form_data:
            self.business_owner_address = form_data.get("business_owner_address")
            self.business_type = form_data.get("business_type")
            self.company_name = form_data.get("company_name")
            self.tin_number = form_data.get("tin_number")
            self.registration_date = form_data.get("registration_date")
            self.business_address = form_data.get("business_address")
        else:
            print("\nEnter Business Details:")
            self.business_owner_address = input("Business Owner Address: ")
            self.business_type = input("Business Type (Retailer/Wholesale/Manufacturer): ").capitalize()
            self.company_name = input("Company Name: ")
            self.tin_number = input("TIN Number (9 digits): ")
            self.registration_date = input("Registration Date: ")
            self.business_address = input("Business Address: ")

    def get_product_details(self, form_data=None):
        if form_data:
            self.purpose_of_importation = form_data.get("purpose_of_importation")
            self.specify_purpose = form_data.get("specify_purpose")
            self.product_category = form_data.get("product_category")
            self.product_name = form_data.get("product_name")
            self.weight_kg = form_data.get("weight_kg")
            self.description_of_products = form_data.get("description_of_products")
            self.unit_of_measurement = form_data.get("unit_of_measurement")
            self.quantity_of_products = form_data.get("quantity_of_products")
        else:
            print("\nEnter Product Details:")
            self.purpose_of_importation = input("Purpose of Importation (Direct sale/Personal use/Trial use/Other): ").capitalize()

            if self.purpose_of_importation == 'Other':
                self.specify_purpose = input("Specify Purpose of Importation: ")

            self.product_category = input("Product Category (General purpose/Construction materials/Chemicals): ").capitalize()
            self.product_name = input("Product Name: ")
            self.weight_kg = input("Weight (kg): ")
            self.description_of_products = input("Description of Products: ")
            self.unit_of_measurement = input("Unit of Measurement (Kgs/Tonnes): ").capitalize()
            self.quantity_of_products = input("Quantity of Products: ")

    def display_application_summary(self):
        print("\nApplication Summary:")
        print(f"Citizenship: {self.applicant_citizenship}")
        print(f"ID Document Number: {self.identification_document_number}")
        print(f"Surname: {self.surname}")
        print(f"Nationality: {self.nationality}")
        print(f"Passport Number: {self.passport_number}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email_address}")
        print(f"Business Owner Address: {self.business_owner_address}")
        print(f"Business Type: {self.business_type}")
        print(f"Company Name: {self.company_name}")
        print(f"TIN Number: {self.tin_number}")
        print(f"Registration Date: {self.registration_date}")
        print(f"Business Address: {self.business_address}")
        print(f"Purpose of Importation: {self.purpose_of_importation}")
        print(f"Specify Purpose: {self.specify_purpose}")
        print(f"Product Category: {self.product_category}")
        print(f"Product Name: {self.product_name}")
        print(f"Weight (kg): {self.weight_kg}")
        print(f"Description of Products: {self.description_of_products}")
        print(f"Unit of Measurement: {self.unit_of_measurement}")
        print(f"Quantity of Products: {self.quantity_of_products}")

    def send_email(self, summary_text, to_email):
        # Set up the SMTP server details
        smtp_server = 'your_smtp_server'
        smtp_port = 587
        smtp_username = ''
        smtp_password = ''

        # Create the email message
        subject = 'RICA Service Application Summary'
        body = summary_text
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = smtp_username
        message['To'] = to_email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, message.as_string())

    def run_service(self, form_data=None):
        self.get_applicant_details(form_data)
        self.get_contact_details(form_data)
        self.get_business_details(form_data)
        self.get_product_details(form_data)
        self.display_application_summary()

# Creating an instance of the RICA Service class and run the service
irembo_service = RICAService()
irembo_service.run_service()

class RICAApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create labels and entry widgets for applicant details
        self.label_citizenship = tk.Label(self, text="Citizenship (Rwandan/Foreigner):")
        self.entry_citizenship = tk.Entry(self)
        self.label_citizenship.grid(row=0, column=0, padx=10, pady=5)
        self.entry_citizenship.grid(row=0, column=1, padx=10, pady=5)

        # Add other labels and entry widgets for other details
        # ... Add similar code for other attributes

        # Create a submit button
        self.submit_button = tk.Button(self, text="Submit Application", command=self.submit_application)
        self.submit_button.grid(row=20, column=0, columnspan=2, pady=10)

    def submit_application(self):
        # Create an instance of the RICAService class
        irembo_service = RICAService()

        # Set the attributes based on the user input
        form_data = {
            "citizenship": self.entry_citizenship.get(),
            # Set other attributes similarly
        }

        # Display the application summary (you can adapt this part based on your needs)
        irembo_service.run_service(form_data)

@app.route("/")
def index():
    rica_app = RICAApp()
    rica_app.mainloop()  # This will run the Tkinter application

    return render_template("index.html", summary=rica_app.submit_application())

if __name__ == "__main__":
    app.run(debug=True)
#
# pip3 install secure-mime
# Make sure to use pip3 if you have both pip and pip3 installed


