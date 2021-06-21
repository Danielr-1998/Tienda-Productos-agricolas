from CRUD import Shop


def main():
    shop = Shop()
    shop.addProductPlague(1, "ProductPlague", 30, 15000, 15)
    shop.addProductFertilizer(1, "ProductFertilizer", 30, 13000, 15)
    shop.addAntibiotic(5,"Antibiotic", "Bovino", 20000)
    print("Opción: \n1.Agregar producto a la factura.\n2.Generar Factura.")
    x = input()
    while int(x) > 0 and int(x) < 3:
        if int(x) == 1:
            shop.addToOrder()
        if int(x) == 2:
            shop.endOrder()
        print("Opción: \n1.Agregar producto a la factura.\n2.Generar Factura.")
        x = input()

if __name__ == "__main__":
    main()

		