def calculate_wind_chill(temperature, wind_speed):
    
    # Function to calculate wind chill
    if temperature < 50:
        # Check if the temperature is below 50 degree Fahrenheit
        # Calculate the winf=d chill using the appropriate formula
        wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
        # ROund the wind chill to 2 decimal places
        return round(wind_chill, 2)
    
    else:
        #if temperature is not below 50 degrees Fahrenheit, return the temperature itself
        return temperature

def convert_to_fahrenheit(celsius):
    # Function to convert temperature from Celsius to Fahrenheit
    return celsius * 9/5 + 32

def main():
    # Main function to take user input and display wind chill values
    temperature = float(input("What is the temperature? "))
    # Ask user to input the temperature
    unit = input("Fahrenheit or Celsius (F/C)? ")

    if unit.upper() == "C":
        # If the input is Celsius, convert the temperature to Fahrenheit
        temperature = convert_to_fahrenheit(temperature)

    print("Wind Chill Values:")
    print("_" * 20)

    # Loop through wind chill for each wind speed
    for wind_speed in range(5, 65, 5):
        # Calculate wind chill for each wind speed
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        # Print the wind chill value for the current temperature and wind speed
        print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    main()
