def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División por cero no permitida."
    return x / y

def power(x, y):
    return x ** y

def calculator():
    print("Bienvenido a la Calculadora")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    
    while True:
        try:
            choice = input("Elige la operación (1/2/3/4/5) o 'q' para salirte: ")
            if choice == 'q':
                print("Gracias por usar la calculadora más god del mundo!")
                break
            
            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ** {num2} = {power(num1, num2)}")
            else:
                print("Haga bien la operación. Por favor, selecciona una opción correcta.")
        
        except ValueError:
            print("Error: Entrada no válida. Asegúrese usar el cerebro y de introducir números.")

if __name__ == "__main__":
    calculator()
