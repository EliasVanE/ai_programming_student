import math
import random

class ExamScheduler:
    def __init__(self, conflict_matrix, num_timeslots=3, initial_temperature=100.0, cooling_rate=0.99, num_iterations=5000):
        self.conflict_matrix = conflict_matrix
        self.num_exams = len(conflict_matrix)
        self.num_timeslots = num_timeslots
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations

    def calculate_cost(self, state: list[int]) -> int:
        """Berekent het totaal aantal conflicten in het huidige rooster."""
        # TODO
        pass

    def random_neighbor(self, state: list[int]) -> list[int]:
        """Kiest 1 willekeurig examen en wijst er een nieuw, willekeurig tijdslot aan toe."""
        # TODO
        pass

    def simulated_annealing(self) -> tuple[list[int], int]:
        """Zoekt het rooster met de minste conflicten."""
        # TODO: start met een willekeurige toewijzing van examens aan tijdsloten (bijv. random tussen 0 en num_timeslots-1)
        pass

if __name__ == "__main__":
    # Conflict matrix: entry (i, j) toont hoeveel studenten examen i EN examen j hebben.
    # We willen zo min mogelijk overlappende studenten in hetzelfde tijdslot.
    conflict_matrix = [
        [0, 10,  0,  5,  2],
        [10, 0,  8,  0,  4],
        [0,  8,  0, 12,  0],
        [5,  0, 12,  0,  7],
        [2,  4,  0,  7,  0]
    ]

    scheduler = ExamScheduler(conflict_matrix)
    best_schedule, min_conflicts = scheduler.simulated_annealing()

    print("Beste rooster:", best_schedule)
    print("Aantal conflicten (kosten):", min_conflicts)