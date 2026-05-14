class cafeteria:
    def preparar_cafe(self):
        self.__hervir_agua()
        self.__moler__cafe()
        print("Café listo!")

    def __hervir_agua(self):
        print("Hirviendo agua...")

    def __moler__cafe(self):
        print("Moliendo café...")

def main():
    mi_cafeteria = cafeteria()
    mi_cafeteria.preparar_cafe()

if __name__ == "__main__":
    main()