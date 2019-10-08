import numpy as np
import string


def score(x, y):
    score = 0
    assert len(x) == len(y), "The strings are of different lengths"
    for i, j in zip(x, y):
        if i == j:
            score += 1
    return score


def generate_string(n, pool):
    x = ''
    for i in range(n):
        x += np.random.choice(pool)
    return x


def mutate(x, mutation_probability, pool):
    z = ''
    for i in range(len(x)):
        if np.random.random() < mutation_probability:
            z += np.random.choice(pool)
        else:
            z += x[i]
    return z


def crossover(x, y):
    z = ''
    for i in range(len(x)):
        if np.random.random() < 0.5:
            z += x[i]
        else:
            z += y[i]
    return z


def new_generation(generation, target, mutation_probability, pool):
    scores = [score(i, target) + 1 for i in generation]
    new_generation = []
    for i in range(len(generation) - 1):
        parent1 = np.random.choice(generation, p=np.asarray(scores) / np.sum(scores))
        parent2 = np.random.choice(generation, p=np.asarray(scores) / np.sum(scores))
        new_generation.append(mutate(crossover(parent1, parent2), mutation_probability, pool))
    best_performer = sorted(zip(scores, generation))[-1][-1]
    new_generation.append(best_performer)
    return (new_generation, best_performer)


if __name__ == '__main__':

    alphabet = list(' ' + string.ascii_lowercase)
    target_sentence = input("Enter target sentence: ")
    generation_size = 100
    mutation_probability = 0.2
    number_epochs = 1000

    generation = [generate_string(len(target_sentence), alphabet) for i in range(generation_size)]

    for epoch in range(number_epochs):
        generation, best_performer = new_generation(generation, target_sentence, mutation_probability, alphabet)
        print(best_performer)

