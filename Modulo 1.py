# Impresión en pantalla 

print('Hola desde la consola')

#Variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

#Tipos de Datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string
type(distancia_a_alfa_centauri)

#Operadores <left side> <operator> <right side>
left_side = 10
right_side = 5
left_side / right_side # 2

#Operadores aritmeticos--
1+1 #SUMA->Operador de adición que suma dos valores juntos
1-2 #RESTA->Operador de resta que quita el valor del lado derecho al del lado izquierdo
10/2 #DIVISION->Operador de división que divide el lado izquierdo tantas veces como especifique el lado derecho
2*2 #MULTIPLICACION->Operador de multiplicación que multiplica ambos lados

#Operadores de asignacion (asignan valores a una variable)--
x = 2 #La variable x ahora contiene 2
x += 2 #Incrementa el valor a la variable, ahora x es 4
x -= 2 #Decrementa el valor a la variable. Si x era 2, ahora es 0
x /= 2 #Divide el valor a la variable. Si x era 2, ahora es 1
x *= 2 #Multiplica el valor a la variable. Si x era 2, ahora es 4

#Fechas
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

print("Today's date is: " + str(date.today()))

#Entrada al usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

#Trabajadr con numeros
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number)3)