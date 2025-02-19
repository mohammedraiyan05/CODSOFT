# Contact Book
# Contact Information: Store name, phone number, email, and address for each contact.
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

names = []
phone_numbers = []

num = 3

for i in range(num):
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    
    names.append(name)
    phone_numbers.append(phone_number)
    
    
print("\tName\t\t\tPhone Number")

for i in range(num):
    print(f'\t{names[i]}\t\t\t{phone_numbers[i]}')
    
s = input("Enter the Name to search: ")
if s in names:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]
    
    print(f"Name:{name} , Phone Number:{phone_number}")
else:
    print("Name not found!")
    
    