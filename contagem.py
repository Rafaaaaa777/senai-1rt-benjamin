from time import sleep 
def contagem_regressiva(tempo):
  while tempo > 0:
         tempo = tempo -1 
         print(tempo)
         sleep (1)
        

        

p = int(input("declare o valor inicial: "))

contagem_regressiva(p)