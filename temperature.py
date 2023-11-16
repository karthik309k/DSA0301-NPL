temperature_celsius = int(input("enter the temperature"))
print(f"The room temperature is {temperature_celsius} degrees Celsius.")
word = "temperature"
conical_form = word.capitalize()
print(f"The conical form of {word} is '{conical_form}'")
temperature_in_farenheit = (temperature_celsius * 9/5) + 32
print("temperature in farenheit is ",temperature_in_farenheit)

def analyze_temperature(temp):
    if temp < 0:
        return "It is freezing."
    elif 0 <= temp < 20:
        return "It is cold."
    else:
        return "It is warm."

temperature = 25
analysis = analyze_temperature(temperature)
print(f"The temperature of {temperature} degrees Celsius: {analysis}")
