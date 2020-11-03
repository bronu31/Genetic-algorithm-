import time
import random
import numpy as np
import copy
import matplotlib.pyplot  as plt


def fit_func(populationS,rect):# checking survivabiluty
    ones=0
    clona=copy.copy(a)
    z=0
    for j in range(len(a)): # creating array with population
         if(a[j]=="-"):
            clona[j]=populationS[z]
            z+=1
    clona=np.asarray(clona,dtype=int)
    for i in range(len(clona)): # counting number of 1 to check with numbert of 0
      if(clona[i]==0):
          n=int(bin(i)[2:])
          while n>0:
              Clone=n%10
              if (Clone==1):
                  ones+=1
              n//=10
    return abs(rect[1]-ones)

def mutatiom(populationS): #mutating population based on something
  for i in range(popsize):
    if random.random()<mut:
      count=random.randint(1,notd-1)
      for j in range(count):
        z=random.randint(0,notd-1)
        if populationS[i][z]==0:
          populationS[i][z]=1
        else:
          populationS[i][z]=0
  return populationS
 
def selection(populationS): # checking strong subjects to select them 
   populationS=sorted(populationS,key=lambda fit: fit[notd])
   for i in range(0,children,2):
      place=random.randint(1,notd-1)
      for j in range(place,notd):
          if populationS[i][j]!=populationS[i+1][j]:
              populationS[i][j]=1-populationS[i][j]
              populationS[i+1][j]=1-populationS[i+1][j]
   for i in range(children,popsize):
      ch=random.randint(0,children-1)
      populationS[i]=copy.copy(populationS[ch])
   return populationS

def main(a,rect):
    generation=1
    gen_array=[]
    surv=[]
    MID=0
    check=True
    print("What must evolve: "+ rect[0])
    print(rect[1])
    global notd
    notd=0
    for i in range (len(a)):
        if(a[i]=="-"):
            notd+=1
    
    populationS=[[0 for j in range(notd+1)]for i in range(popsize)]
    for i in range(popsize):
        for j in range(notd):
            populationS[i][j]=random.randint(0,1)
    while check:
      for i in range(popsize):
          populationS[i][notd]=fit_func(populationS[i],rect)
          if(populationS[i][notd])==0:
              print("solution: %s " %(populationS[i][:-1]))
              print("generation: %s " %(generation))
              fig, ax = plt.subplots()
              ax.plot(gen_array,surv)
              check=False
              ax.set_xlabel('number of generations')
              ax.set_ylabel('Average fitness function ')
              plt.show()
              return
      MID=sum(row[notd] for row in populationS)/popsize
      surv.append(MID)
      gen_array.append(generation)
      populationS=selection(populationS)
      mutatiom(populationS)
      generation+=1

start_time = time.time()
f1 = open('data.txt','r')
i=0
global popsize #population size
global mut #mutation chance
global children #number of children per generation
for line in f1:
    if i==0: popsize=line
    if i==1: mut=line
    if i==2: children=line
    i+=1
f1.close()
popsize=int(popsize)
mut=float(mut)
children=int(children)
f2 = open('vectors.txt', 'r')
for line in f2:
    rect=line.split(' ')
    rect[1]=int(rect[1])
    a=list(rect[0])
    for i in range(len(a)):
        if a[i]!='-': a[i]=int(a[i])
    main(a,rect)
f2.close()
 
print("--- %s seconds ---" % (time.time() - start_time))