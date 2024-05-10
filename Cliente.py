import asyncio
import websockets


# Direccion y puerto del cliente
URL = "wss://6f0adf2c-2d2c-4231-8233-42364cae1e1b-00-p9jj5uxhhjw4.worf.replit.dev:3000/"  

async def main():
    async with websockets.connect(URL) as websocket:

        while True:
            menu = """
            ----- CALCULADORA PRACTICA 5 -----

            [-1] => Salir
            [0] => Sumar
            [1] => Restar
            [2] => Multiplicar
            [3] => Dividir
            [4] => Exponente
            Elige: """

            print(menu)

            try:
                op = int(input())
            except ValueError:
                op = -1

            if op != -1:
                try:
                    num1 = float(input("Ingresa el número 1: "))
                    num2 = float(input("Ingresa el número 2: "))
                
                except ValueError:
                    num1 = 0
                    num2 = 0

                # Comprueba si la division es por 0
                if op == 3 and num2 == 0:
                    print("Error: La división por cero no está permitida")
                    continue

                # Envia la operacion, y el numero introducido al servidor 
                await websocket.send(f"{op},{num1},{num2}")
                result = await websocket.recv()

                # Comprueba si el resultado no esta vacio, si no lo esta lo imprime
                if result is not None:
                    print(f"Resultado => {result}")

                input("Presiona ENTER para continuar...")

            if op == -1:
                break

# Funcion de incio del cliente de forma asincrona hasta que se complete 
def iniciar_cliente():
    try:
        asyncio.get_event_loop().run_until_complete(main())
    
    # Se muestra un mensaje si se produce un error de conexion
    except (ConnectionRefusedError, OSError) as e:
        print(f"Error: No se pudo conectar al servidor. {e}")
    
    # Se muestra un mensaje si se produce cualquier otro error
    except Exception as e: 
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_cliente()

