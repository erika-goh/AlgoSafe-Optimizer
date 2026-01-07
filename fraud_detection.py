import random
import copy

# GA Parameters (you can adjust these)
POP_SIZE = 20
GENES = 3
GENERATIONS = 50
MUTATION_RATE = 0.1

def fitness(rule, transactions, profile):
    errors = 0
    for t in transactions:
        risk_score = (t['amount'] / profile['avg_amount'] * rule[0]) + \
                     (1 if t['location'] not in profile['common_locations'] else 0) * rule[1] + \
                     (1 if t['time_of_day'] > 20 or t['time_of_day'] < 6 else 0) * rule[2]
        predicted_fraud = risk_score > 1.5
        if predicted_fraud != t['is_fraud']:
            errors += 1
    return 1 - (errors / len(transactions))

def optimize_fraud_rule(transactions, profile):
    population = [[random.uniform(0.5, 2.0) for _ in range(GENES)] for _ in range(POP_SIZE)]
    
    for _ in range(GENERATIONS):
        fitness_scores = [fitness(ind, transactions, profile) for ind in population]
        sorted_pop = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        parents = sorted_pop[:POP_SIZE // 2]
        
        children = []
        for _ in range(POP_SIZE // 2):
            parent1, parent2 = random.choice(parents), random.choice(parents)
            child = copy.deepcopy(parent1)
            crossover_point = random.randint(1, GENES - 1)
            child[crossover_point:] = parent2[crossover_point:]
            
            for j in range(GENES):
                if random.random() < MUTATION_RATE:
                    child[j] += random.uniform(-0.5, 0.5)
            children.append(child)
        
        population = parents + children
    
    best_rule = population[0]
    return best_rule
