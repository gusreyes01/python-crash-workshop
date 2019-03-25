import carpeta.mi_modulo as m

NUMERO_DE_AMIGOS = 5

if __name__ == "__main__": 
	m.saludar("Jaime")
	print('Name mi_modulo 2: {}'.format(__name__))
	print('Name mi_modulo: {}'.format(m.__name__))
