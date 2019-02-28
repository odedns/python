N = 8
 
def sum_quare_difference(n):
    # Your code here...
    i = 0;
    sumsq =0;
    sqsum =0;
    while(i <= N):
        sumsq += i*i;
        sqsum += i;
        i = i + 1
    sqsum = sqsum * sqsum
    print("sumsq", sumsq)
    print("sqsum", sqsum)
    return(sqsum - sumsq)
   
print(sum_quare_difference(N))