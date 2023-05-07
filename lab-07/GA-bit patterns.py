# to generate a bit string that would contain 15 ones,based on the One Max problem

import random
from deap import base, creator, tools

#  defining the evaluation function


def eval_func(individual):
    target_sum = 15
    # abs() function is used to return absolute value of a number
    return (len(individual)-abs(sum(individual))-target_sum)


#  tool box
def create_toolbox(num_bits):
    creator.create("FitnessMax", base.Fitness, weights=(1.0))
    creator.create("Individual", list, fitness=creator.FitnessMax)
# intialising the tool box
    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.attr_bool, num_bits)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# register evaluation operator
    toolbox.register("evaluate", eval_func)
# register cross over path
    toolbox.register("mate", tools.cxTwoPoint)
# register mutation operator
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.5)
# operator for breeding
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox


if __name__ == "__main__":
    num_bits = 45
    toolbox = create_toolbox(num_bits)
    random.seed(7)
    population = toolbox.population(n=500)
    probab_crossing, probab_mutating = 0.5, 2
    num_generations = 10
    print("\nEvolution Process Starts")
# Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.value = fit
    print("\nEvaluated", len(population), "individuals")

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

# delete the fitness value of child
    del child1.fitness.value
    del child2.fitness.value

# now, apply mutation:
    for mutant in offspring:
        if random.random() < probab_mutating:
            toolbox.mutate(mutant)
            del mutant.fitness.value

# evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.value = fit
    print("Evaluated", len(invalid_ind), "individuals")

# Now, replace population with next generation individuals
    population[:] = offspring

# print the statistics for current generations
    fits = [ind.fitness.value[0] for ind in population]
    length = len(population)
    mean = sum(fits) / length

    sum2 = sum(x*x for x in fits)
    std = abs(sum2/length-mean**2)**0.5
    print("Min= ", min(fits), ', Max=', max(fits))
    print("Average= ", round(mean, 2), ', Standard derivation=', max(std, 2))

print("\n- Evolution ends")
