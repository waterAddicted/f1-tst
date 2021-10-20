
def citire_lista():
    result_list = []
    lst = input('Introduceti lista:')
    str_lst = lst.split()
    for string_element in str_lst:
        element = int(string_element)
        result_list.append(element)
    return result_list


def main():
    list = []
    lista_goala = True
    while True:
        print('1.   Citire lista.')
        print('2.   ')
        print('3.   ')
        print('4.   ')
        print('5.   ')
        print('x    Exit.')
        comanda = input('Introduceti comanda:')
        if comanda == '1':
            list=citire_lista()
            lista_goala = False
        elif comanda == '2':
            if lista_goala == True:
                list = citire_lista()
                lista_goala = False
        elif comanda == '3':
            if lista_goala == True:
                list = citire_lista()
                lista_goala = False
        elif comanda == '4':
            if lista_goala == True:
                list = citire_lista()
                lista_goala = False
        elif comanda == '5':
            if lista_goala == True:
                list = citire_lista()
                lista_goala = False
        elif comanda == 'x':
            break
        else:
            print('Comanda invalida.')

main()