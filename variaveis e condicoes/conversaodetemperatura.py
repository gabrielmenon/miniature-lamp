grausCelsius = (float);
grausFahrenheit = (float);

grausCelsius = float(input("Digite a temperatura em °C: "));

grausFahrenheit = (grausCelsius * 1.8) + 32;
grausFahrenheit = round(grausFahrenheit, 2);

print(f'{grausCelsius} °C é igual {grausFahrenheit} graus Fahrenheit');
