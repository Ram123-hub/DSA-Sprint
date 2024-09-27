def generate_square_matrix(size):
    matrix = []
    num = 1
    for i in range(size):
        rows = []  
        for j in range(size):
            rows.append(num)
            num += 1
        matrix.append(rows) 
    
   
    for row in matrix:
        print(" ".join(map(str, row)))  

 
size = 3  
generate_square_matrix(size)
