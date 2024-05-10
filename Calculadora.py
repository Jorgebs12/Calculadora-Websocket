class Calculadora:
    def sumar(self, numero1, numero2):
        return numero1 + numero2

    def restar(self, numero1, numero2):
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):
        return numero1 * numero2

    def dividir(self, numero1, numero2):
        ##Comprueba si la multiplicacion es por 0 no se puede hacer
        if numero2 == 0:
            raise ZeroDivisionError("No se pude dividir por 0")
        return numero1 / numero2

    def exponente(self, base, exponente):
        return base ** exponente 
