
# Initialize variables
min_age = float('inf')
min_country = ""
min_year = 0
max_age = float('-inf')
max_country = ""
max_year = 0

selected_year = int(input("Enter the year of interest: ").strip())

# List to store ages for the selected year
age_list = []

# Variables to store specific minimum and maximum age for the selected year
spec_min_age = float('inf')
spec_min_country = ""
spec_max_age = float('-inf')
spec_max_country = ""

# Open the file and read line by line
with open("Week 06/life-expectancy.csv") as file:
    # Skip the header
    next(file)
    
    for line in file:
        # Strip and split the line
        data = line.strip().split(',')
        
        # Extract data
        country = data[0]
        year = int(data[2])
        age = float(data[3])
        
        # Update overall minimum age and its details
        if age < min_age:
            min_age = age
            min_country = country
            min_year = year
        
        # Update overall maximum age and its details
        if age > max_age:
            max_age = age
            max_country = country
            max_year = year
            
        # Check if it's the selected year
        if year == selected_year:
            age_list.append(age)
            
            # Update specific minimum age and its details
            if age < spec_min_age:
                spec_min_age = age
                spec_min_country = country
            
            # Update specific maximum age and its details
            if age > spec_max_age:
                spec_max_age = age
                spec_max_country = country

# Calculate average age for the selected year
spec_avg = sum(age_list) / len(age_list) if age_list else 0

# Print results
print(f"\nThe overall max life expectancy is: {max_age} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_age} from {min_country} in {min_year}")

print(f"\nFor the year {selected_year}:")
print(f"The average life expectancy across all countries was {spec_avg:.2f}")
print(f"The max life expectancy was in {spec_max_country} with {spec_max_age}")
print(f"The min life expectancy was in {spec_min_country} with {spec_min_age}")
