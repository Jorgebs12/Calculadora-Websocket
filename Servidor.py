import asyncio
import websockets
from Calculadora import Calculadora


async def server(websocket):  
    
    miCalculadora = Calculadora()
   
    async for message in websocket:
       
        operation, num1, num2 = map(float, message.split(","))
       
        if operation == 0:
            result = miCalculadora.sumar(num1, num2)
        
        elif operation == 1:
            result = miCalculadora.restar(num1, num2)
        
        elif operation == 2:
            result = miCalculadora.multiplicar(num1, num2)
        
        elif operation == 3:
            result = miCalculadora.dividir(num1, num2)
        
        elif operation == 4:
            result = miCalculadora.exponente(num1, num2)
        
        else:
            result = "Opcion no valida, introduce una opcion valida entre el -1 y 4"
        
        await websocket.send(str(result))

# Direccion y puerto del servidor
IP = "127.0.0.1"
port = 3000
start_server = websockets.serve(server, IP, port)

asyncio.get_event_loop().run_until_complete(start_server)

print("El servidor está en ejecución en: " + IP + ":" + str(port) + " ...")

asyncio.get_event_loop().run_forever()  