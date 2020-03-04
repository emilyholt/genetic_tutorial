import random

DOMINANT_ALLELE = "B"
RECESSIVE_ALLELE = "b"

def punnett_square(parent_a, parent_b):
  square_1 = parent_a[0] + parent_b[0]
  square_2 = parent_a[1] + parent_b[0]
  square_3 = parent_a[0] + parent_b[1]
  square_4 = parent_a[1] + parent_b[1]
  return [square_1, square_2, square_3, square_4]

def print_punnett_square(parent_a, parent_b, ps):
  print(f"""
      {parent_a[0]}     {parent_a[1]}
    ------------
  {parent_b[0]} | {ps[0]} |  {ps[1]} |
    ------------
  {parent_b[1]} | {ps[2]} |  {ps[3]} |
    ------------
  """)


def calculate_genotype_probabilities(ps):
  counts = dict((i, ps.count(i) / len(ps)) for i in ps)
  return counts

def print_genotype_probabilities(ps):
  counts = dict((i, str(ps.count(i) / len(ps)) + "%") for i in ps)
  print(counts)

def generate_offspring(counts):
  choices = []
  weights = []
  for key in counts.keys():
    choices.append(key)
    weights.append(counts[key])
  offspring = random.choices(choices, weights)
  return offspring

def is_heterozygous(individual):
  return individual == [DOMINANT_ALLELE, RECESSIVE_ALLELE] or individual == [RECESSIVE_ALLELE, DOMINANT_ALLELE]

def is_homozygous_dominant(individual):
  return individual == [DOMINANT_ALLELE, DOMINANT_ALLELE]

def is_homozygous_recessive(individual):
  return individual == [RECESSIVE_ALLELE, RECESSIVE_ALLELE]

def has_dominant_phenotype(individual):
  return DOMINANT_ALLELE in individual

def has_recessive_phenotype(individual):
  return not has_dominant_phenotype(individual)
