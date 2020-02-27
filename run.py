import experiment

crossover_rate=0.5
mutation_rate=0.2
population_size=20
total_generations=100
total_genes=20
GENES = ['BLUE', 'GREEN', 'BROWN']

resulting_population = experiment.run(GENES, crossover_rate, mutation_rate, population_size, total_generations, total_genes)
experiment.print_population(resulting_population, GENES)