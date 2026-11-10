"""
Oefening 2: Knapsack Probleem met pygad
=========================================
Los het knapsack probleem op met een genetisch algoritme.
"""
import pygad
import numpy as np

# Data
capaciteit = 10
gewichten = np.array([5, 4, 6, 3])
waarden = np.array([10, 40, 30, 50])
n_voorwerpen = len(gewichten)


def fitness_func(ga_instance, solution, solution_idx):
    # TODO: bereken totale waarde, straf als gewicht > capaciteit
    totaal_gewicht = float(np.dot(solution, gewichten))
    totaal_waarde = float(np.dot(solution, waarden))
    if totaal_gewicht > capaciteit:
        return totaal_waarde - 1000
    return totaal_waarde


# TODO: configureer pygad.GA (zie OneMax.py uit de cursus)
ga_instance = pygad.GA(
    num_generations=100,
    num_parents_mating=4,
    fitness_func=fitness_func,
    sol_per_pop=10,
    num_genes=n_voorwerpen,
    mutation_percent_genes=5,
    gene_space=[0, 1],
    gene_type=int,
)
ga_instance.run()

# Oplossing tonen
solution, solution_fitness, _ = ga_instance.best_solution()
print("Gekozen voorwerpen:", solution)
print("Totale waarde:", solution_fitness)