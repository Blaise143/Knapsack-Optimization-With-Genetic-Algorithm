import requests

problem_1 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p01_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p01_p.txt",
    "capacity": 165,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p01_s.txt"
}

problem_2 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p02_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p02_p.txt",
    "capacity": 26,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p02_s.txt"
}

problem_3 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p03_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p03_p.txt",
    "capacity": 190,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p03_s.txt"
}

problem_4 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p04_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p04_p.txt",
    "capacity": 50,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p04_s.txt"
}

problem_5 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p05_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p05_p.txt",
    "capacity": 104,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p05_s.txt"

}


problem_6 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p06_w.txt",
    "profits" : "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p06_p.txt",
    "capacity": 170,
    "optimal" : "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p06_s.txt",
    "best" : 169
}

problem_7 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p07_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p07_p.txt",
    "capacity": 750,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p07_s.txt",
    "best": 1458
}

problem_8 = {
    "weights": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p08_w.txt",
    "profits": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p08_p.txt",
    "capacity": 6404180,
    "optimal": "https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p08_s.txt",
    "best": 13549094
}

problems = [problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8]

# print(first_set)
for prob in problems:
    weights = requests.get(prob["weights"]).text.split()
    profits = requests.get(prob["profits"]).text.split()
    optimal = requests.get(prob["optimal"]).text.split()

    prob["weights"] = [int(i) for i in weights]
    prob["profits"] = [int(i) for i in profits]
    prob["optimal"] = [int(i) for i in optimal]

p1, p2, p3, p4, p5, p6, p7, p8 = problems
# for i in problems:
#     print(i)