Details={
 "Ravi": "9876543210",
 "Anita": "9123456780",
 "Anjali": "9424999989"
}
contact=[v for k,v in Details.items()]
print(Details)
name=input("Enter Name:")
if name in Details:
    print(Details[name])
else:
    print("Contact not found")