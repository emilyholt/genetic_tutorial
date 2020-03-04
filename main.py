from punnett_square import PunnettSquareSimulator
DOMINANT_ALLELE = "A"
RECESSIVE_ALLELE  = "b"
DOMINANT_TRAIT = "Brown fur"
RECESSIVE_TRAIT  = "Red fur"

ps = PunnettSquareSimulator(DOMINANT_ALLELE, RECESSIVE_ALLELE, DOMINANT_TRAIT, RECESSIVE_TRAIT)


parent_a = [DOMINANT_ALLELE, RECESSIVE_ALLELE]
parent_b = [DOMINANT_ALLELE, RECESSIVE_ALLELE]

ps_example = ps.punnett_square(parent_a, parent_b)
ps.print_punnett_square(parent_a, parent_b, ps_example)
ps.print_genotype_probabilities(ps_example)
counts = ps.calculate_genotype_probabilities(ps_example)
print(counts)
offspring = ps.generate_offspring(parent_a, parent_b)
print("offspring")
print(offspring)

#######################
number_of_offspring = 50
offspring_list = []
for number in range(number_of_offspring):
  new_offspring = ps.generate_offspring(parent_a, parent_b)
  offspring_list.append(new_offspring)

print(offspring_list)
