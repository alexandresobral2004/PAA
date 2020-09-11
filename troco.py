def troco(n,lista):
    temp = n
    temp_list=[]
    tam = len(lista)
    for i in range(0,tam):
        if lista[i] <= temp:
            while(lista[i] <= temp):
                temp_list.append(lista[i]) 
                temp = temp - lista[i]   

            
           
                
       
    return temp_list
            
            


lista = [25,10,5,1]
x = troco(1,lista)
print(x)   