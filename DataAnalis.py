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

# Variables to store the largest drop in life expectancy
largest_drop = float('-inf')
largest_drop_country = ""
largest_drop_year = 0

# Dictionary to store life expectancy data by country
country_data = {}

# Open the file and read line by line
with open("life-expectancy.csv") as file:
    # Skip the header
    next(file)
    
    prev_year_data = None
    
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
        
        # Update largest drop in life expectancy
        if prev_year_data is not None:
            prev_age = prev_year_data[3]
            # "drop = prev_age - age"
            drop = float(prev_age) - age
            if drop > largest_drop:
                largest_drop = drop
                largest_drop_country = country
                largest_drop_year = year - 1
        
        # Store data by country for future lookup
        if country not in country_data:
            country_data[country] = []
        country_data[country].append((year, age))
        
        prev_year_data = data

# Calculate average age for the selected year
spec_avg = sum(age_list) / len(age_list) if age_list else 0

# Print results
print(f"\nThe overall max life expectancy is: {max_age} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_age} from {min_country} in {min_year}")

# Print the largest drop in life expectancy
print(f"\nFor the year {selected_year}:")
print(f"The average life expectancy across all countries was {spec_avg:.2f}")
print(f"The max life expectancy was in {spec_max_country} with {spec_max_age}")
print(f"The min life expectancy was in {spec_min_country} with {spec_min_age}")

print(f"\nThe largest drop in life expectancy occurred in {largest_drop_country} from {largest_drop_year} to {largest_drop_year+1}, with a drop of {largest_drop:.2f} years.")

# Allow user to explore life expectancy data for a specific country
country_input = input("\nEnter a country to explore (leave blank to skip): ").strip()
if country_input:
    if country_input in country_data:
        country_age_data = country_data[country_input]
        country_min_age = min(country_age_data, key=lambda x: x[1])
        country_max_age = max(country_age_data, key=lambda x: x[1])
        country_avg_age = sum(age for _, age in country_age_data) / len(country_age_data)
        print(f"\nFor {country_input}:")
        print(f"Minimum life expectancy: {country_min_age[1]} in {country_min_age[0]}")
        print(f"Maximum life expectancy: {country_max_age[1]} in {country_max_age[0]}")
        print(f"Average life expectancy: {country_avg_age:.2f}")
    else:
        print("Country not found in the data.")
