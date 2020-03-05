import random

DOMINANT_ALLELE = "B"
RECESSIVE_ALLELE = "b"
NUMBER_OF_OFFSPRING = 50

def punnett_square(parent_a, parent_b):
  square_1 = [parent_a[0], parent_b[0]]
  square_2 = [parent_a[1], parent_b[0]]
  square_3 = [parent_a[0], parent_b[1]]
  square_4 = [parent_a[1], parent_b[1]]
  return [square_1, square_2, square_3, square_4]

def print_punnett_square(parent_a, parent_b, ps):
  print(f"""
          {parent_a[0]}             {parent_a[1]}
    ----------------------------
  {parent_b[0]} | {ps[0]} |  {ps[1]} |
    ----------------------------
  {parent_b[1]} | {ps[2]} |  {ps[3]} |
    ----------------------------
  """)

def calculate_punnett_square_probabilities(ps):
  counts = dict(("".join(i), ps.count(i) / len(ps)) for i in ps)
  return counts

def calculate_genotype_probabilities(ps):
  counts = {
    "hetero": (ps.count([DOMINANT_ALLELE, RECESSIVE_ALLELE]) + ps.count([RECESSIVE_ALLELE, DOMINANT_ALLELE])) / len(ps),
    "homozygous_dominant": ps.count([DOMINANT_ALLELE, DOMINANT_ALLELE]) / len(ps),
    "homozygous_recessive": ps.count([RECESSIVE_ALLELE, RECESSIVE_ALLELE]) / len(ps)
  }
  return counts

def generate_offspring(parent_a, parent_b):
  ps = punnett_square(parent_a, parent_b)
  genotype_probabilities = calculate_punnett_square_probabilities(ps)
  choices = []
  weights = []
  for key in genotype_probabilities.keys():
    choices.append(key)
    weights.append(genotype_probabilities[key])
  offspring = random.choices(choices, weights)[0]
  return list(offspring)

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

# def genotype_statistics(popualtion):
#   stats = {
#     "BB":
#   }

# def phenotype_statistic(population):
