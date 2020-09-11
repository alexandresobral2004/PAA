def troco(n,lista):
    temp = n
    temp_list=[]
    tam = len(lista)
    if lista[-1] > lista[0]:
        lista.sort(reverse=True)
        for i in range(0,tam):
            if lista[i] <= temp:
                while(lista[i] <= temp):
                        temp_list.append(lista[i]) 
                        temp = temp - lista[i]   

        return temp_list
   
               
                        
            
        
            
            


lista = [1,2,5,10]
x = troco(44,lista)
print(x)   