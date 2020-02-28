import random

parent_a = 'BB'
parent_b = 'BR'

def punnett_square(parent_a, parent_b):
  square_1 = parent_a[0] + parent_b[0]
  square_2 = parent_a[1] + parent_b[0]
  square_3 = parent_a[0] + parent_b[1]
  square_4 = parent_a[1] + parent_b[1]
  return [square_1,square_2, square_3, square_4]

def print_punnett_square(ps):
  print(" | ", ps[0], " | ", ps[1], " | ",        "\n----------------\n", 
  "| ", ps[2], " | ", ps[3], " | ")

def calculate_probablities(ps):
  counts = dict((i, ps.count(i) * .25) for i in ps)
  return counts

def print_probablities(ps):
  counts = dict((i, str(ps.count(i) * 25) + "%") for i in ps)
  print(counts)

def predict_offspring(counts):
  choices = []
  weights = []
  for key in counts.keys():
    choices.append(key)
    weights.append(counts[key])
  offspring = random.choices(choices, weights)
  return offspring
    

ps = punnett_square(parent_a, parent_b)
print_punnett_square(ps)
print_probablities(ps)
counts = calculate_probablities(ps)
offspring = predict_offspring(counts)
print(offspring)

