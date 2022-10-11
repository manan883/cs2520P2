import timeit
def generatePrimes(n,start_val=0):
    count = 0
    #lst will be manipulated at the end but will hold the primes 
    lst = list()
    #temp will first be filled with all True values up to n+1, later on some will be turned to false which will tell which nums are prime
    temp = [True] * (1340000)
    #loop through n starting at the lowest prime number which is 2, we need it to start at 2 because temp is true at first 
    for i in range(2,1340000):
        #when temp is true it adds it to the list 
        if temp[i]:
            lst.append(i)
            count+=1
            #This loops from the current number to n+1 with a step of the current number
            #This removes any multiples of the number which greatly saves time and ram 
            for j in range(i,1340000,i):
                temp[j] = False
        
        
        if count == n:
            break
    final = [x for x in lst if x>start_val]
    global total_time
    
    yield final