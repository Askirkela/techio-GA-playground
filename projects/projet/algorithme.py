import random
from secret import est_solution
# Vous pouvez red�finir ces fonctions avec celles que vous avez �crites pr�c�demment.
# Une impl�mentation diff�rente est fournie.
from codage import creer_chromosome
from tools import selection, croisement, mutation

size = int(input())
population = 0

def creer_population():
    chrom = creer_chromosome(size)
    return []
    
def generation(population):

    # s�lection
    select = selection([])
    
    # reproduction
    ## croisement
    parent1 = bytearray()
    parent2 = bytearray()
    enfant = croisement(parent1, parent2)
    
    ## mutation
    mutation(bytearray())
    
    # retourner la nouvelle g�n�ration
    return []

def algorithme():
    # cr�er la population
    creer_population()
    
    solutions = []
    
    # tant qu'une solution n'est pas trouv�e:
    while not solutions:
    ## cr�er la generation suivante
        generation([])
    
    ## v�rifier si une solution est trouv�e
        if est_solution(bytearray()):
            solutions.append(bytearray())
    
    # afficher la solution
    print("SOLUTION")
    