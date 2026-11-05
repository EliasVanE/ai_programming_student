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
            zin += "".join(random.choice(string.ascii_letters))
        return zin

    def calculate_fitness(self, phrase):
        score = 0
        for i in range(len(phrase) ):
            if phrase[i] == self.target_phrase[i]:
                score += 1
        return score

    def generate_population(self, size, phrase_length):
        zinnen = []
        for i in  range(1,size+1):
            zin = self.generate_phrase(phrase_length)
            zinnen.append(zin)
        return zinnen

    def crossover(self, phrase1, phrase2):
        split = random.randint(0, len(phrase1))
        child = phrase1[:split] + phrase2[split:]
        return child

    def mutate(self, phrase, rate):
        result = ""

        for char in phrase:
            if random.random() < rate:
                result += random.choice(string.printable)
            else:
                result += char

        return result

    def select_best(self, population):
        population.sort(key=self.calculate_fitness,reverse=True)
        return population[0]
    def genetic_algorithm(self):
        population = self.generate_population(
            self.population_size, len(self.target_phrase))
        for generation in range(self.num_generations):
            population.sort(key=self.calculate_fitness, reverse=True)
            best_phrase = population[0]

            if generation % 100 == 0:
                print(
                f"Generatie {generation}: {best_phrase} "
                f"(fitness: {self.calculate_fitness(best_phrase)})"
            )

            if best_phrase == self.target_phrase:
                print(f"Doelzin bereikt in generatie {generation}: {best_phrase}")
                return best_phrase

            new_population = [best_phrase]

            helft = population[:len(population) // 2]

            while len(new_population) < self.population_size:
                parent1 = random.choice(helft)
                parent2 = random.choice(helft)

                child = self.crossover(parent1, parent2)
                child = self.mutate(child, self.mutation_rate)

                new_population.append(child)

            population = new_population

        population.sort(key=self.calculate_fitness, reverse=True)
        return population[0]    
            


def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    # print(puzzle.generate_phrase(5))
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")
    

if __name__ == "__main__":
    main()