import carpeta.mi_modulo as m

NUMERO_DE_AMIGOS = 5


def main():
    m.saludar("Jaime")
    print(f"Name mi_modulo 2: {__name__}")
    print(f"Name mi_modulo: {m.__name__}")


if __name__ == "__main__":
    main()
