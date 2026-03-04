from octagon import Octagon

def main():
    Octagon_storona=Octagon(float(input('Введите длину стороны октагона:')))
    Octagon_storona.opis()
    Octagon_storona.vpis()
    Octagon_storona.oct()
    Octagon_storona.grafik()

if __name__ == '__main__':
    main()