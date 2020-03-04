import punnett_square as ps
parent_a = [ps.DOMINANT_ALLELE, ps.RECESSIVE_ALLELE]
parent_b = [ps.DOMINANT_ALLELE, ps.RECESSIVE_ALLELE]

ps_ex = ps.punnett_square(parent_a, parent_b)
ps.print_punnett_square(parent_a, parent_b, ps_ex)
gen = ps.calculate_genotype_probabilities(ps_ex)
print(gen)
ps.print_genotype_probabilities(ps_ex)
phen = ps.calculate_phenotype_probabilities(ps_ex)
print(phen)
ps.print_phenotype_probabilities(ps_ex)
ind = ps.generate_offspring(parent_a, parent_b)
print(ind)
print("ps.is_heterozygous(ind)")
print(ps.is_heterozygous(ind))
print("ps.is_homozygous_dominant(ind)")
print(ps.is_homozygous_dominant(ind))
print("ps.is_homozygous_recessive(ind)")
print(ps.is_homozygous_recessive(ind))
print("ps.has_dominant_phenotype(ind)")
print(ps.has_dominant_phenotype(ind))
print("ps.has_recessive_phenotype(ind)")
print(ps.has_recessive_phenotype(ind))
