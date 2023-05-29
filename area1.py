def multiplicação(comprimento, largura):
    area = comprimento  * largura  
    return area 


largura = float( input("qual a largura do terreno: ") )
comprimento = float( input("qual a o comprimento do terreno: ") )
print("area do terreno e igual a :", multiplicação(largura, comprimento), "metros quadrados")
