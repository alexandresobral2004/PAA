def subSequence(lista):
    temp = 0
    count=0
    bestCount=0
    temp_list=[]
    temp_list2=[]
    tam = len(lista)
    for i in range(tam):
        for j in range(1,tam):
            if lista[i] < lista[j]:    
               
                if lista[i] > temp: 
                    temp_list.append(lista[i])
                    temp = temp_list[-1]
                if lista[j] > temp:
                    temp_list.append(lista[j])
                    temp = temp_list[-1]
                   
            
            elif lista[i] > lista[j]:    
               
                if lista[i] > temp: 
                    temp_list.append(lista[i])
                    temp = temp_list[-1]
                if lista[j] > temp:
                    temp_list.append(lista[j])
                    temp = temp_list[-1]
                    
           
        
        count= len(temp_list)
        if count > bestCount:
            bestCount = count
            temp_list2 =temp_list.copy()
            temp_list = []
            temp = 0
                
    return temp_list2
                
                
                
                
                
lista = [4,1,7,3,8,2,9,6,10,5,15,12,17,13,19,14,20,11,23,12,24,10,26,9,28]
valor = subSequence(lista)
print(valor)