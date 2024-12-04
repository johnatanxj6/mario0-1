def  main():
    coluna(pegar_numero())
def coluna(colunas):
    print("😊\n" * colunas, end="")
def pegar_numero():
    while true:
        coluna = int(input("quantas colunas você quer?"))
        if coluna > 0:
         return coluna
main()                