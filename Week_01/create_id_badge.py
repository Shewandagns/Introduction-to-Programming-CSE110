
# Prompt user for information
first_name = input('Enter your First Name: ')
last_name = input('Enter your Last Name: ')
email = input('Enter your Email Address: ')
phone_number = input('Enter your Phone Number: ')
job_title = input('Enter your Job Title: ')
id_number = input('Enter your ID Number: ')
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
month = input('Starting Month: ')
training = input('Training (Yes/No): ')
print()

 # Format and display ID badge
print('The ID Card is: ')
print('----------------------------------------')
print(f'{last_name.upper()}, {first_name}')
print(f'job_title')
print(f'ID: {id_number}')
print()

print(f'{email}')
print(f'{phone_number}')
print()

print(f'\nHair: {hair_color}    Eyes: {eye_color}')
print(f'Month: {month}     Training: {training}')
print('----------------------------------------')