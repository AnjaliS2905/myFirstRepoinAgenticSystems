user_name = input("Enter your name: ")

user_age = input("Enter your age: ")
user_age = int(user_age) 

active_status_input = input("Are you an active user? (True/False): ")
is_active_user = active_status_input.strip().lower() == "true"

print(f"User {user_name} is {user_age} years old. Active status: {is_active_user}")
