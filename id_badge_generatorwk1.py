'''
Title: Id Badge Generator.
Author: Tope Jinad
Purpose: To create an Id badge generator
'''
print("Enter the following information:")

first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

print()

print("The ID  Card is: ")
print("---------------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.capitalize())
print(f"ID: {id_number}")

print()

print(email_address.lower())
print(phone_number)

print()

print("---------------------------------------------")


