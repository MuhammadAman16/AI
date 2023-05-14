import random
from deap import base, creator, tools


def eval_func(individual):
    target_sum = 15
    return len(individual)-abs(sum(individual) - target_sum),


def create_toolbox(num_bits):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.attr_bool, num_bits)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_func)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

    toolbox.register("select", tools.selTournament, tournsize=3)
    return toolbox


if __name__ == "_main_":
    num_bits = 45
    toolbox = create_toolbox(num_bits)
    random.seed(7)
    population = toolbox.population(n=500)
    probab_crossing, probab_mutating = 0.5, 0.2
    num_generations = 10
    print('\nEvolution process starts')

# Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit
    print('\nEvaluated', len(population), 'individuals')

# create and iterate through generations
    for g in range(num_generations):
        print("\n- Generation", g)
# selecting the next generation individuals;
        offspring = toolbox.select(population, len(population))

# now clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

# apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < probab_crossing:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

# now, apply mutation:
        for mutant in offspring:
            if random.random() < probab_mutating:
                toolbox.mutate(mutant)
                del mutant.fitness.values

# evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print('Evaluated', len(invalid_ind), 'individuals')

# Now, replace population with next generation individuals

# print the statistics for current generations
        population[:] = offspring
        fits = [ind.fitness.values[0] for ind in population]
        length = len(population)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean*2)*0.5
        print('Min =', min(fits), ', Max =', max(fits))
        print('Average =', round(mean, 2),
              ', Standard deviation =', round(std, 2))
    print("\n- Evolution ends")
    best_ind = tools.selBest(population, 1)[0]
    print('\nBest individual:\n', best_ind)
    print('\nNumber of ones:', sum(best_ind))
