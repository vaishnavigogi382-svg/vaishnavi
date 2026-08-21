print("contact book!")
details = ["vaishnavi",9535678231,123456789,147258369,"vaishnavigogi@gmail.com", "bidar"]

a=int(input("enter a newcontact:"))
details.append(a)
print("contact added successfully!")
print("updated details:",details)

search =int(input("enter the contact to search:"))
if search in details:
    print("contact found!")
else:
    print("not found!")

c= int(input("delete a contact:"))
if c in details:
    details.remove(c)
print("contact deleted successsfully!")
print("updated details:",details)
print("exit!")

