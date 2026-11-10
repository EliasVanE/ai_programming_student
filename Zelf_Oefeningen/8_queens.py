# Opgave: Eight Queens – Genetisch Algoritme (20 punten)
# In deze opdracht pas je genetic programming toe op het klassieke 8 Queens Problem:

# Plaats 8 queens op een schaakbord zodanig dat geen enkele queen een andere aanvalt. Voor de volledigheid herhalen we wat een Queen (koningin) op een schaakbord mag doen tijdens 1 beweging:

# Ofwel zo ver als ze wil horizontaal verplaatsen
# Ofwel zo ver als ze wil verticaal verplaatsen
# Ofwel zo ver als ze wil diagonaal verplaatsen
# Je krijgt een reeds voorbereide Python‐klasse EightQueens, waarin jij zelf fitness, crossover, mutatie en de GA-loop verder moet implementeren.

# Het doel is om het genetisch algoritme zo te laten werken dat het een geldige oplossing vindt, of op zijn minst een zeer goede fitness bereikt.

# Representatie van een individu
# In deze opdracht wordt een oplossing (individu) voorgesteld als een lijst van 8 getallen:

# Index = rij
# Waarde = kolom waarin de queen staat
# Voorbeeld:

# example_individu = [4, 2, 7, 3, 6, 0, 5, 1]
# Dit betekent:

# Rij	Kolom
# 0	4
# 1	2
# 2	7
# 3	3
# 4	6
# 5	0
# 6	5
# 7	1
# De klasse bevat een functie print_board(individual) waarmee je de oplossing als schaakbord ziet:

#  .  .  .  .  Q  .  .  .
#  .  .  Q  .  .  .  .  .
#  .  .  .  .  .  .  .  Q
#  ...
# Deze functie hoef je niet te programmeren, enkel te gebruiken. Dit kan nuttig zijn voor eventuele debugging.

# Fitness functie invullen (8 punten)
# In de functie calculate_fitness() schrijf je de checks die bepalen of twee queens elkaar aanvallen. Hints zijn in de code voorzien – vul enkel de ontbrekende blokken aan.

# Crossover implementeren (3 punten)
# Schrijf een eenvoudige crossover, analoog met wat we in de les hebben gedaan.

# Mutatie implementeren (3 punten)
# met kans mutation_rate
# vervang je de kolom door een willekeurige waarde tussen 0 en 7
# Genetisch Algoritme schrijven (4 punten)
# Schrijf hier het genetisch algoritme en zorg dat het vroegtijdig stopt als je een oplossing voor 8 Queens bereikt.

# Korte beschrijving in comment (2 punten)
# Voeg onderaan je code commentaar toe over wat je in de output van je code ziet (werkt het ? Zo ja, leg kort uit; zo nee, leg uit wat je misschien zou kunnen veranderen om het wél te doen werken)

# Puntenverdeling (20 punten)
# Onderdeel	Punten
# Fitness functie correct afgewerkt	8
# Crossover correct geïmplementeerd	3
# Mutatie correct geïmplementeerd	3
# Genetisch algoritme correct opgebouwd	4
# Kort uitleggen wat de code uiteindelijk doet	2
# Totaal	20
# Uiteindelijk resultaat
# Wanneer je code correct is, zal het programma iets tonen zoals:

# Gen 40: beste fitness = 25
# Opgelost in generatie 57!
# Beste oplossing: [4, 2, 7, 3, 6, 0, 5, 1]
# Fitness: 28
# En het bord:

#  .  .  .  .  Q  .  .  .
#  .  .  Q  .  .  .  .  .
#  .  .  .  .  .  .  .  Q
#  ...

import random

class EightQueens:
    def __init__(self, population_size=100, mutation_rate=0.01, num_generations=200):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.n = 8  # 8x8 bord

    # -------------------------------------------------------
    # 1. Individu genereren
    # -------------------------------------------------------
    def generate_individual(self):
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    # -------------------------------------------------------
    # 2. Fitness berekenen
    # -------------------------------------------------------
    def calculate_fitness(self, individual):
        """
        Fitness = aantal NIET-aanvallende paren.
        
        We hebben 8 queens → aantal mogelijke paren = 28.
        Voor elk paar dat elkaar aanvalt, trekken we 1 punt af.
        
        Twee queens vallen elkaar aan wanneer:
        - ze in dezelfde KOLOM staan
        - ze op dezelfde DIAGONAAL staan
        (Horizontaal is onmogelijk in deze representatie, want 
        elke rij heeft precies 1 queen.)
        """

        non_attacking = 28  # maximaal aantal niet-aanvallende paren

        for i in range(self.n):
            for j in range(i + 1, self.n):
                # TODO 1:
                # Controleer of queens i en j in dezelfde kolom staan.
                # individual[i] bevat kolom van rij i.
                # Hint: gewone vergelijking volstaat.

                # if ...:
                #     non_attacking -= 1
                if individual[i] == individual[j]:
                    non_attacking -= 1

                # TODO 2:
                # Controleer of queens i en j op dezelfde DIAGONAAL staan.
                # Queens staan diagonaal als het hoogteverschil gelijk is
                # aan het kolomverschil.
                # Hint: gebruik abs()

                # if ...:
                #     non_attacking -= 1
                if abs(individual[i] - individual[j]) == abs(i -j ):
                    non_attacking -= 1

        return non_attacking


    # -------------------------------------------------------
    # 3. Populatie genereren
    # -------------------------------------------------------
    def generate_population(self):
        return [self.generate_individual() for _ in range(self.population_size)]

    # -------------------------------------------------------
    # 4. Crossover
    # -------------------------------------------------------
    def crossover(self, parent1, parent2):
        #TODO
        # schrijf een crossover functie
        punt = random.randint(1, self.n - 1)
        nieuwe_ouder = parent1[:punt] + parent2[punt:]
        return nieuwe_ouder

    # -------------------------------------------------------
    # 5. Mutatie
    # -------------------------------------------------------
    def mutate(self, individual):
        # TODO
        # schrijf code die bij het individu, op basis van de mutation rate, af en toe een queen van plaats verandert.
        # doe dit door voor elke waarde van de array 'individual' met bepaalde kans een random getal te kiezen tussen 0 en 7
        rate= self.mutation_rate
        for i in range(len(individual)):
            kans  = random.random()
            if kans < rate:
                individual[i] = random.randint(0,7)
            
        return individual

    # -------------------------------------------------------
    # 6. Bord printen
    # -------------------------------------------------------
    def print_board(self, individual):
        """
        Print het bord visueel:
        Een 'Q' op de positie van de dame,
        en '.' op lege vakken.
        """
        print("\nBordrepresentatie:\n")
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if individual[row] == col:
                    line += " Q "
                else:
                    line += " . "
            print(line)
        print("\n")
        print("Representatie:", individual)
        print("\n")


    # -------------------------------------------------------
    # 7. Genetisch algoritme
    # -------------------------------------------------------
    def genetic_algorithm(self):
        populatie = self.generate_population()
        beste_fitness = 0
        beste_zet = None

        for generatie in range(self.num_generations):

            populatie.sort(key=self.calculate_fitness, reverse=True)

            if self.calculate_fitness(populatie[0]) > beste_fitness:
                beste_zet = populatie[0].copy()
                beste_fitness = self.calculate_fitness(beste_zet)

            if beste_fitness == 28:
                break

            aantal_ouders = max(2, self.population_size // 2)
            ouders = populatie[:aantal_ouders]

            volgende = []

            while len(volgende) < self.population_size:
                p1, p2 = random.sample(ouders, 2)

                kind = self.crossover(p1, p2)
                kind = self.mutate(kind)

                volgende.append(kind)

            populatie = volgende

            if generatie % 10 == 0:
                print(f"Generatie {generatie}: {beste_zet} ({beste_fitness}/28)")
        print(f"Opgelost in generatie {generatie}: {beste_zet} ({beste_fitness}/28)")
        return beste_zet

# -------------------------------------------------------
# Voorbeeldgebruik
# -------------------------------------------------------
if __name__ == "__main__":
    queens = EightQueens()

    # Voorbeeld van een 'individu' in dit probleem:
    example_individu = [4, 2, 7, 3, 6, 0, 5, 1]
    queens.print_board(example_individu)

    solution = queens.genetic_algorithm()

    print("\nBeste oplossing:", solution)
    print("Fitness:", queens.calculate_fitness(solution))

    queens.print_board(solution)