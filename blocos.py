def main():
    tamanho = int(input("coloque o tamanho dos seus blocos: "))
    bloco(tamanho)

def bloco(tamanho):
     bloco =("😵" * tamanho)
     print (f"{bloco}\n" * tamanho , end = "")

main()     