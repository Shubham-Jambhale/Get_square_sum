def get_square_sum (M,N) :
    output=0
    for i in range(1,N):
        square_root = i ** 0.5
        if square_root.is_integer():
             output += i            
    if M == 1:
        #print("in if",output)
        return output
    else:
        #print("in else",output)
        return get_square_sum(M-1,output)