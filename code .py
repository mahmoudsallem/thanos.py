from  os import *
from  random import *

chdir(r"C:\Users\7ouda\Desktop\lecturs_epsilon")

def list_univers(plase):
    univers = listdir(plase)
    return univers


def thanod (univers):
    half_of_univers=int(len(univers) / 2)
    for i in range(half_of_univers):
        univers = list_univers("Universe/") 
        remove("Universe/" + choice(univers))
    print("the filles deleted ")


    univers = list_univers("Universe/")
    
    
    print(univers)
    
    
    thanod(univers)
    
    
    NewUnivers = list_univers("Universe/")
    
    
    print(len(NewUnivers))
    
