import numpy as np
import matplotlib.pyplot as plt
from array import*

def Gauss_Seidel(A, p ,b):  
    #Cautam dimensiunea matricei A    
    n = len(A)                   
    for j in range(0, n):  
        #Vom stoca intr-o variabila temporara
        # vectorul b      
        temp = b[j]       
        #se actualizeaza valoarea cu solutia rezultata           
        for i in range(0, n):     
            if(j != i):
                temp -= A[j][i] * p[i]        
        p[j] = temp / A[j][j]             
    return p #functia returneaza solutia actualizata
# Introducerea numarului de muchii/intersectii pe care le are traseul
muchii = 10
# n este o variabila ce reprezinta numarul de probabilitati ce vor fi 
#generate in urma algoritmului
n = muchii 

# Matricea reprezentativa traseului
# Pe diagonala principala se afla numarul de posibilitati de miscare
#pe care le are autoturismul la intersectia/muchia respectiva
# Valoarea 0 sugereaza faptul ca la nivelul muchiei/intersectiei respec-
#tive, autoturismul nu are o conexiune directa cu muchia reprezentata
#de numarul coloanei 
A = [[4, -1, -1,  0,  0,  0,  0,  0,  0,  0],
 [-1,  5, -1, -1,  -1,  0,  0,  0,  0,  0],
 [-1, -1,  5,  0, -1, -1,  0,  0,  0,  0],
 [ 0, -1,  0,  5, -1,  0, -1, -1,  0,  0],
 [ 0, -1, -1, -1,  6, -1,  0, -1, -1,  0],
 [ 0,  0, -1,  0, -1,  5,  0,  0, -1, -1],
 [ 0,  0,  0, -1,  0,  0,  4, -1,  0,  0],
 [ 0,  0,  0, -1, -1,  0, -1,  5, -1,  0],
 [ 0,  0,  0,  0, -1, -1,  0, -1,  5, -1],
 [ 0,  0,  0,  0,  0, -1,  0,  0, -1,  4]]

#p este vectorul probabilitatilor iar p0 este solutia arbitrara pe care
#o vom considera la inceputul algoritmului
p0 = [1,1,1,1,1,1,1,1,1,1]

p = p0

b = array('i',[0,0,0,0,0,0,1,1,1,1])

#numarul de iteratii pe care il vom considera
for i in range(0,18):
    p = Gauss_Seidel(A, p, b)

# Pentru estetica output-ului dorim sa afisam probabilitatile castigatoare
# in ordine descrescatoare.
# Am utilizat urmatorul algoritm de sortare
# Vor fi sortati : vectorul cu probabilitati, si indexul corespunzator 
# al acestuia     
def sortareVector(vector,index):
    n = len(vector)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if vector[j] < vector[j + 1] :
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                index[j], index[j + 1] = index[j + 1], index[j]
 

index = np.arange(0,muchii,1)
sortareVector(p,index)

Probabilitati = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
Procentaje = [0.09,0.18,0.18,0.3,0.33,0.3,0.45,0.52,0.52,0.45]

plt.bar(Probabilitati,Procentaje)
plt.title('Probabilitati')
plt.xlabel('Vector de probabilitati')
plt.ylabel('Procentaje de castig')
plt.show()

print("Probabilitatile sunt: \n")

for i in range (len(p)):
    print("%.4f - p%d" % (p[i], index[i]+1))