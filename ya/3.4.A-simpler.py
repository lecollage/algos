def TowerOfHanoi(n, from_rod, to_rod, aux_rod1, aux_rod2): 
    if n == 0: 
        return
    
    TowerOfHanoi(n-2, from_rod, aux_rod1, to_rod, aux_rod2)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    TowerOfHanoi(n-2, aux_rod1, to_rod, from_rod, aux_rod2) 

N = 3
  
TowerOfHanoi(N, 'A', 'D', 'B', 'C')

'''
Input : 3
Output :
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 3 from rod A to rod D
Move disk 2 from rod C to rod D
Move disk 1 from rod B to rod D

Input : 5
Output : 
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod D
Move disk 3 from rod A to rod B
Move disk 2 from rod D to rod B
Move disk 1 from rod C to rod B
Move disk 4 from rod A to rod C
Move disk 5 from rod A to rod D
Move disk 4 from rod C to rod D
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 3 from rod B to rod D
Move disk 2 from rod C to rod D
Move disk 1 from rod A to rod D
'''