"""
Oefening 1: Word Generator (Genetisch Algoritme)
==================================================
Evolueer een populatie van willekeurige zinnen naar een doelzin.
"""
import random
import string


class WordPuzzle:
    def __init__(self, target_phrase, population_size=100, mutation_rate=0.01, num_generations=10000):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations

    def generate_phrase(self, length):
        zin = ""
        for _ in range(length):
            zin += random.choice(string.ascii_letters + " ")
        return zin

    def calculate_fitness(self, phrase):
        score = 0
        for i in range(len(phrase)):
            if self.target_phrase[i] == phrase[i]:
                score += 1
        return score / len(phrase)

    def generate_population(self, size, phrase_length):
        zinnen = []
        for i in range(size):
            zin = self.generate_phrase(phrase_length)
            zinnen.append(zin)
        return zinnen

    def crossover(self, phrase1, phrase2):
        knippunt = random.randint(1,len(phrase1) -1)
        nieuwe_zin = phrase1[:knippunt] + phrase2[knippunt:]
        return nieuwe_zin

    def mutate(self, phrase, rate):
        rate= self.mutation_rate
        nieuwe_zin = ""
        for i in range(len(phrase)):
            kans  = random.random()
            if kans < rate:
               nieuwe_zin += random.choice(string.ascii_letters + " ")
            else:
                nieuwe_zin += phrase[i]
        return nieuwe_zin

    def select_best(self, population):
        score = 0
        beste_zin = ""
        for zin in population:
            fitness = self.calculate_fitness(zin)
            if score < fitness:
                beste_zin = zin
                score = fitness
        return beste_zin
    def genetic_algorithm(self):
        lengte  = len(self.target_phrase)
        populatie = self.generate_population(self.population_size, lengte)
        beste_zin = self.select_best(populatie)
        beste_fitness = self.calculate_fitness(beste_zin)

        for _ in range(self.num_generations):
            populatie.sort(key=self.calculate_fitness, reverse=True)
            
            if self.calculate_fitness(populatie[0]) > beste_fitness:
                beste_zin = populatie[0]
                beste_fitness = self.calculate_fitness(beste_zin)
                if beste_fitness == 1.0:
                    break
            aantal_ouders = max(2, self.population_size // 2)
            ouders = populatie[:aantal_ouders]
            volgende: list[str] = []
            while len(volgende) < self.population_size:
                p1, p2 = random.sample(ouders, 2)
                kind = self.crossover(p1, p2)
                kind = self.mutate(kind, self.mutation_rate)
                volgende.append(kind)
            if _ % 100 == 0:
                print(f"Generatie {_}: {beste_zin} ({beste_fitness:.2%})")
            populatie = volgende
        print(f"Opgelost in generatie {_}: {beste_zin} ({beste_fitness:.2%})")
        return beste_zin

          
            


def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    # print(puzzle.generate_phrase(5))
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")
    

if __name__ == "__main__":
    main()