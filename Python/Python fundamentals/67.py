# Contact Book -Project
contacts = {
    "John": "705-555-1234",
    "Sarah": "705-555-5678"
}
name=input("Enter name: ")
phone=input("Enter phone number: ")
contacts[name]=phone
searchname=input("Enter name to search: ")
if searchname in contacts:
    print("Phone:",contacts[searchname])# dict[key] gives value
else:
    print("Contact not found")
for key,value in contacts.items():
    print(key,":",value)
removeuser=input("which user you want to remove? ")
if removeuser in contacts:
    contacts.pop(removeuser)
    print("Contact removed")
else:
    print("Contact not found")
print(contacts)
print("total contacts: ",len(contacts))
