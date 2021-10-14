import matplotlib.pyplot as plt
import math
import random
import numpy as np
import array
from functools import reduce
from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp
import concurrent.futures as future


def första(n):
    
    i = 0 #Så man vet att while-loopen ska gå framåt
    nc = 0 #Räknar kordinater inanför cirkeln
    x = [] #Har lagras x-koordinater för plot
    y = [] #Har lagras y-koordinater för plot
    pi = math.pi
    
    while i < n: #sålänge index är mindre än totala kordinater skapa koordinater
        
        x1 = np.random.uniform(-1,1) #randomtal på intervall -1:1
        y2 = np.random.uniform(-1,1) #annat randomtal på intervall -1:1
        x.append(x1) #lägg till det första som x-koordinat
        y.append(y2) # det andra som y-koordinat
        i += 1 #öka index så whileloopen går frammåt
        
        if math.sqrt(x1 ** 2 + y2 ** 2) < 1: # om sqrt(x^2 + y^2) < 1 så ligger koordinaterna inanför linjen 
            nc +=1 #addera isf 1 till nc
            
    #gör om listan till array för att kunna plota
    x = np.array(x) 
    y = np.array(y)

    
    #Arean för cirkeln
    area = pi * (np.random.rand(n))**2
    
    #Beskriver vad radien av cirkeln är
    r = np.sqrt(x ** 2 + y ** 2)
    
    #Delar upp i två areor
    
    area1 = np.ma.masked_where(1 < r, area) #innanför cirkeln
    area2 = np.ma.masked_where(1 >= r, area) #på eller utanför cirkeln
    
    plt.scatter(x, y, s=area1, marker='o', color='r') #plott för punkter innanför cirkeln
    plt.scatter(x, y, s=area2, marker='o', color='b' ) # plott för punkter utanför cirkeln
    plt.show()
    

    pi = 4 * (nc/n) #approximera pi
    
    return pi
    


def andra(n, d):
    r = 1
    nc = 0
    
    x = [np.random.uniform(-1,1) for ii in range(0,n)] #List comprehensions
    
    l = map(lambda z: z**2, x) #map
    
    for e in l:
        if (lambda z: d*z)(e) <= 1: #Lambda högre ordning
            nc += 1 
    
    vdr = ((math.pi**(d/2))/(math.gamma((d/2)+1)))*(r**d)
    #print(vdr)
    
    
    v = 4 * (nc/n) #approximera pi
    
    return v

#Tredje
with future.ProcessPoolExecutor() as ex:
    p1 = ex.submit(andra, 10000, 2) # Starts first→ process
    p2 = ex.submit(andra, 10000, 2) # Starts second,→ process

    r1 = p1.result() # Program waits until p1 is complete before assigning r2
    r2 = p2.result()

print("all done") # Will be printed once all processes are completed
      
if __name__ == "__main__":
    start = pc()
    andra(100000, 2)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

# Anrop        
#print(första(1000))
# approximationen för n=1000 blev 3.156
# approximationen för n=10000 blev 3.1612
# approximationen för n=100000 blev 3.145

#print(andra(100000, 2))
# Med n=100000 och d=2, Vdr=3.141592653589793, approx = 2.82044
# Med n=100000 och d=11, Vdr=1.8841038793898994, approx = 1.20664

        
