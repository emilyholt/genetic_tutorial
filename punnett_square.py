import random

DOMINANT_ALLELE = "B"
RECESSIVE_ALLELE = "b"
DOMINANT_TRAIT = "Brown Fur"
RECESSIVE_TRAIT = "Red Fur"
NUMBER_OF_OFFSPRING = 50

class PunnettSquareSimulator():
  def __init__(self, dominant_allele, recessive_allele, dominant_trait, recessive_trait):
    self.dominant_allele = dominant_allele
    self.recessive_allele = recessive_allele
    self.dominant_trait = dominant_trait
    self.recessive_trait = recessive_trait

  def punnett_square(self, parent_a, parent_b):
    square_1 = [parent_a[0], parent_b[0]]
    square_2 = [parent_a[1], parent_b[0]]
    square_3 = [parent_a[0], parent_b[1]]
    square_4 = [parent_a[1], parent_b[1]]
    return [square_1, square_2, square_3, square_4]

  def print_punnett_square(self, parent_a, parent_b, ps):
    print(f"""
            {parent_a[0]}             {parent_a[1]}
      ----------------------------
    {parent_b[0]} | {ps[0]} |  {ps[1]} |
      ----------------------------
    {parent_b[1]} | {ps[2]} |  {ps[3]} |
      ----------------------------
    """)


  def calculate_punnett_square_probabilities(self, ps):
    counts = dict(("".join(i), ps.count(i) / len(ps)) for i in ps)
    return counts

  def print_punnett_square_probabilities(self, ps):
    counts = dict(("".join(i), str(ps.count(i) / len(ps)) + "%") for i in ps)
    print(counts)

  def calculate_genotype_probabilities(self, ps):
    counts = {
      "hetero": (ps.count([self.dominant_allele, self.recessive_allele]) + ps.count([self.recessive_allele, self.dominant_allele])) / len(ps),
      "homozygous_dominant": ps.count([self.dominant_allele, self.dominant_allele]) / len(ps),
      "homozygous_recessive": ps.count([self.recessive_allele, self.recessive_allele]) / len(ps)
    }
    return counts

  def print_genotype_probabilities(self, ps):
    counts = {
      "hetero": str((ps.count([self.dominant_allele, self.recessive_allele]) + ps.count([self.recessive_allele, self.dominant_allele])) / len(ps)) + "%",
      "homozygous_dominant": str(ps.count([self.dominant_allele, self.dominant_allele]) / len(ps)) + "%",
      "homozygous_recessive": str(ps.count([self.recessive_allele, self.recessive_allele]) / len(ps)) + "%"
    }
    print(counts)

  def calculate_phenotype_probabilities(self, ps):
    counts = {
      self.dominant_trait: sum(map(lambda x: self.is_homozygous_dominant(x) or self.is_heterozygous(x), ps))
      self.dominant_trait: sum(map(lambda x: self.is_homozygous_recessive(x), ps))
      self.recessive_trait: []
    }
    return counts

  def print_phenotype_probabilities(self, ps):
    counts = dict(("".join(i), str(ps.count(i) / len(ps)) + "%") for i in ps)
    print(counts)

  def calculate_phenotype_probabilities(self, ps):
    print(ps)
    counts = {
      "hetero": (ps.count([self.dominant_allele, self.recessive_allele]) + ps.count([self.recessive_allele, self.dominant_allele])) / len(ps),
      "homozygous_dominant": ps.count([self.dominant_allele, self.dominant_allele]) / len(ps),
      "homozygous_recessive": ps.count([self.recessive_allele, self.recessive_allele]) / len(ps)
    }
    return counts

  def print_phenotype_probabilities(self, ps):
    counts = {
      "hetero": str((ps.count([self.dominant_allele, self.recessive_allele]) + ps.count([self.recessive_allele, self.dominant_allele])) / len(ps)) + "%",
      "homozygous_dominant": str(ps.count([self.dominant_allele, self.dominant_allele]) / len(ps)) + "%",
      "homozygous_recessive": str(ps.count([self.recessive_allele, self.recessive_allele]) / len(ps)) + "%"
    }
    print(counts)

  def generate_offspring(self, parent_a, parent_b):
    ps = self.punnett_square(parent_a, parent_b)
    punnett_square_probabilities = self.calculate_punnett_square_probabilities(ps)
    choices = []
    weights = []
    for key in punnett_square_probabilities.keys():
      choices.append(key)
      weights.append(punnett_square_probabilities[key])
    offspring = random.choices(choices, weights)[0]
    return list(offspring)

  def is_heterozygous(self, individual):
    return individual == [self.dominant_allele, self.recessive_allele] or individual == [self.recessive_allele, self.dominant_allele]

  def is_homozygous_dominant(self, individual):
    return individual == [self.dominant_allele, self.dominant_allele]

  def is_homozygous_recessive(self, individual):
    return individual == [self.recessive_allele, self.recessive_allele]

  def has_dominant_phenotype(self, individual):
    return self.dominant_allele in individual

  def has_recessive_phenotype(self, individual):
    return not has_dominant_phenotype(individual)

  # def self, genotype_statistics(popualtion):
  #   stats = {
  #     "BB":
  #   }

  # def self, phenotype_statistic(population):
