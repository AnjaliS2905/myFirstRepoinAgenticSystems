Age=int(input("Age:"))
has_id_input=input("Has ID(True/False):").strip().lower()
if has_id_input == "true":
        has_id = True
elif has_id_input == "false":
    has_id = False
if Age>=18 and has_id==True:
    print("Entry Allowed")
else:
    print("Entry Not Allowed")