from punnett_square import *
DOMINANT_ALLELE = "B"
RECESSIVE_ALLELE  = "b"
DOMINANT_TRAIT = "Brown fur"
RECESSIVE_TRAIT  = "Red fur"

parent_a = [DOMINANT_ALLELE, RECESSIVE_ALLELE]
parent_b = [DOMINANT_ALLELE, RECESSIVE_ALLELE]
number_of_offspring = 50

ps_example = punnett_square(parent_a, parent_b)
print_punnett_square(parent_a, parent_b, ps_example)
counts = calculate_genotype_probabilities(ps_example)
print(counts)
offspring = generate_offspring(parent_a, parent_b)
print("offspring")
print(offspring)

offspring_list = []
for number in range(number_of_offspring):
  new_offspring = generate_offspring(parent_a, parent_b)
  offspring_list.append(new_offspring)

print(offspring_list)
