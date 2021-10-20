def show_menu():
    print("1. Citire lista")
    print("2. Afisarea tuturor numerelor negative nenule din lista")
    print("3. Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura")
    print("4. Afisarea tuturor numerelor din lista care sunt superprime")
    print("5. Afisarea listei obtinute din lista initiala in care nr pozitive si nenule au fost inlocuite cu cmmdc ul lor si nr negative au cifrele in ordine inversa")
    print("x. Iesire")

def read_list():
    #citirea listei
    lst = []
    lst_str = input("Dati numerele separate prin spatiu: ")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def cerinta_2(lst):
    #afiseaza toate nr negative nenule din lista
    lista = []
    for nr in lst:
        if nr<0:
            lista.append(nr)
    return lista

def test_cerinta_2():
    assert(cerinta_2([5, 6, -2, -1, 7, -3])) == [-2, -1, -3]
    assert (cerinta_2([1, -9, 4, -16, 7, 19])) == [-9, -16]

def cerinta_3(lst, n):
    mic_nr = 10000
    l = len(lst)
    for i in range(0,l):
       if lst[i] % 10 == n:
            mic_nr = lst[i]

    return mic_nr

def cerinta_4(lst):
    #afiseaza toate numerele superprime din lista
    lista = []
    for nr in lst:
        if is_superprime(nr):
            lista.append(nr)
    return lista

def test_cerinta_4():
    assert(cerinta_4([173, 13, 239, 17, 6 ,7])) == [173, 13, 239, 17, 7]

def is_superprime(n):
    # verifica daca un numar este superprim sau nu
    while n:
        nrdiv = 0
        for i in range(2, n):
            if (n % i == 0):
                nrdiv = nrdiv + 1
            if (nrdiv):
                return False
        n = n // 10
    return True

def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Comanda: ")
        if cmd == "1":
            lst = read_list()
        elif cmd == "2":
            print(cerinta_2(lst))
        elif cmd == "3":
            n = int(input("Introduceti n = "))
            print(cerinta_3(lst,n))
        elif cmd == "4":
            print(cerinta_4(lst))
        elif cmd == "5":
            pass
        elif cmd == "x":
            break
        else:
            print("Comanda invalida.")

def run_tests():
    test_cerinta_2()
    test_cerinta_4()

if __name__ == '__main__':
    run_tests()
    main()