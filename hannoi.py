def TorreHanoi(n , source, dest, aux_rod): 
	
    if n == 1: 
        print "Mover o disco 1 de ",source," para ",dest 
        return
    TorreHanoi(n-1, source, aux_rod, dest) 
    print "Mover disco",n," de ",source," para ",dest
    TorreHanoi(n-1, source, aux_rod, dest)  

n = 2
TorreHanoi(n,'A','C','B')
