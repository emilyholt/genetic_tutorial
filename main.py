from punnett_square import *

dominant_allele = 'B'
recessive_allele = 'b'

dominant_phenotype = 'Brown Fur'
recessive_phenotype = 'White Fur'

bunny_a = [dominant_allele, recessive_allele]
bunny_b = [dominant_allele, recessive_allele]

ps = punnett_square(bunny_a, bunny_b)
print_punnett_square(bunny_a, bunny_b, ps)

punnett_square_probabilities = calculate_punnett_square_probabilities(ps)
print(punnett_square_probabilities)
genotype_probabilities = calculate_genotype_probabilities(ps)
print(genotype_probabilities)

offspring = generate_offspring(bunny_a, bunny_b)
print(offspring)
offspring_phenotype = get_offspring_phenotype(offspring, dominant_phenotype, recessive_phenotype)

print(offspring_phenotype)
for num in range(5):
	print(num)

offspring_list = []
for num in range(5):
	offspring = generate_offspring(bunny_a, bunny_b)
	offspring_list.append(offspring)
print(offspring_list)

stats = genotype_statistics(offspring_list)
print(stats)
