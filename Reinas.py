import random
import matplotlib.pyplot as plt

def create_initial_population(size, board_size):
    population = []
    for _ in range(size):
        board = [random.randint(0, board_size - 1) for _ in range(board_size)]
        population.append(board)
    return population

def fitness(board):
    conflicts = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(i + 1, board_size):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    roulette_value = random.uniform(0, total_fitness)
    cumulative_fitness = 0

    for i, board in enumerate(population):
        cumulative_fitness += fitness_values[i]
        if cumulative_fitness >= roulette_value:
            return board

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(board, mutation_rate):
    for i in range(len(board)):
        if random.random() < mutation_rate:
            board[i] = random.randint(0, len(board) - 1)
    return board

def genetic_algorithm(board_size, population_size, num_generations, mutation_rate):
    population = create_initial_population(population_size, board_size)
    average_fitness_history = []
    best_fitness_history = []

    for generation in range(num_generations):
        fitness_values = [fitness(board) for board in population]
        average_fitness = sum(fitness_values) / population_size
        average_fitness_history.append(average_fitness)

        best_fitness = min(fitness_values)
        best_fitness_history.append(best_fitness)

        population.sort(key=lambda x: fitness(x))

        new_population = []
        for _ in range(population_size):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return average_fitness_history, best_fitness_history

def plot_fitness_evolution(average_fitness_history, best_fitness_history, population_size):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(range(len(average_fitness_history)), average_fitness_history)
    plt.xlabel("Generation")
    plt.ylabel("Average Fitness")
    plt.title(f"Population Size: {population_size}")

    plt.subplot(1, 2, 2)
    plt.plot(range(len(best_fitness_history)), best_fitness_history)
    plt.xlabel("Generation")
    plt.ylabel("Fitness of the Best Individual")
    plt.title(f"Population Size: {population_size}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    n = int(input("Numero de n reinas que se desea probar: "))
    population_sizes = []
    num_poblaciones = int(input("Numero de poblaciones que se desea probar: "))
    for _ in range(num_poblaciones):
        population_sizes.append(int(input("Tamaño de la población: ")))
    # population_sizes = [int(input("Tamaño de la población: "))]
    generations = 100
    crossover_probability = 0.8
    mutation_probability = 0.2
    elitism = bool(input("¿Elitismo? (True: 1/False: 0): "))
    maximise_fitness = False
    mutation_rate = 0.2
    # population_sizes = [10, 100, 200, 500]
    
    for population_size in population_sizes:
        average_fitness_history, best_fitness_history = genetic_algorithm(n, population_size, generations, mutation_rate)
        plot_fitness_evolution(average_fitness_history, best_fitness_history, population_size)
    

