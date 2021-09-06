import cowsay
import random
import time


cowsay.daemon("Bienvenido a Blackjack, creado por: Johann!")

print("Presiona enter para continuar")
input()


menu = ""

while menu != "1":
	print("Menu: (Elije el numero)\n")
	print("1. Jugar")
	print("2. Como se juega")
	print("3. Salir")
	menu = input("Elije: ") 
	if menu == "2":
		print("\n---------------------INSTRUCCIONES------------------------------\n")
		print("El sistema te entrega dos cartas y el se entrega dos cartas")
		print("El que logre tener cartas que sumen 21, gana")
		print("Puedes pedir otra carta con \"Pedir\"")
		print("Si no quieres mas cartas, puedes escribir \"ya\"\n")
		print("-------------------------------------------------------------\n")
		continue
	if menu == "3":
		print(":(")
		exit()

if menu == "1":
	sistema = [random.randint(1, 10), random.randint(1, 10)]

	usuario = [random.randint(1,10), random.randint(1,10)]
	print("Repartiendo cartas...\n")
	time.sleep(2)
	print(f'Oponente: **, {sistema[1]}\n')
	print(f'Tus cartas: {usuario[0]}, {usuario[1]}')
	juego = "xd"
	if usuario[0] + usuario[1] == 21:
		print("Ganaste, sacaste 21!")
	elif sistema[0] + sistema[1] == 21:
		print("Gana el sistema, saco 21!")

	while juego != "ya" or juego != "Ya":
		juego = input("Elije (Pedir, Ya): ")
		if juego == "Pedir" or juego == "pedir":
			carta_nueva = random.randint(1,10)
			usuario.append(carta_nueva)
			print(f'Tus cartas: {usuario}')
			res = 0
			for num in usuario:
				res = res + num
				if res == 21:
					print("Ganaste, sacaste 21")
					exit()
				elif res > 21:
					print("Perdiste! te pasaste de 21")
					exit()
				elif res < 21:
					continue


		elif juego == "ya" or juego == "Ya":
			break

usuario_fin = 0
for numero in usuario:
	usuario_fin += numero

print(f'Te has plantado en: {usuario_fin}\n')
print("Ahora juga el sistema\n")
print(f'Las cartas del sistema son: {sistema}')

if sistema[0] + sistema[1] == 21:
	print("Perdiste! El sistema saco 21")
	exit()


while sum(sistema) < 21:
	if sum(sistema) >= usuario_fin and sum(sistema) <= 21:
		print(f'El sistema se ha plantado en {sum(sistema)}, y eso es mas que lo que tu sacaste, gana el sistema')
		exit()
	else:
		carta_nueva = random.randint(1,10)
		sistema.append(carta_nueva)
		print("El sistema pide otra carta\n")
		time.sleep(2)
		print(f'Las cartas del sistema son: {sistema}')
		continue

if sum(sistema) == 21:
	print("El sistema ha sacado 21, tu pierdes")
	exit()

if sum(sistema) > 21:
	print(f'El sistema ha sacado {sum(sistema)} y eso es mas que 21, tu ganas')
	exit()
