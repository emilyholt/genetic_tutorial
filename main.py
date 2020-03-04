import punnett_square as ps
parent_a = [ps.DOMINANT_ALLELE, ps.RECESSIVE_ALLELE]
parent_b = [ps.DOMINANT_ALLELE, ps.RECESSIVE_ALLELE]

ps_example = ps.punnett_square(parent_a, parent_b)
ps.print_punnett_square(parent_a, parent_b, ps_example)
ps.print_genotype_probabilities(ps_example)
counts = ps.calculate_genotype_probabilities(ps_example)
print(counts)
offspring = ps.generate_offspring(parent_a, parent_b)
print(offspring)
