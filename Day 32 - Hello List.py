import random

greetings = ["Olá!", "Hello there!", "¡Hola!", "Bonjour!", "Hallo!", "Ciao!", "こんにちは", "你好", "Здравствуйте", "مرحبا"]
sayHello = random.randint(0, 9)
print(f"{greetings[sayHello]}")
