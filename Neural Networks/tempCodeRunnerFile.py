import numpy as np

#membership functions
def very_bad(x):
    sigma = 0.5
    mu = 0.5 
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def bad(x):
    sigma = 0.5
    mu = 2.5  
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def average(x):
    sigma = 0.5
    mu = 5 
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def good(x):
    sigma = 0.5
    mu = 6.5  
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def very_good(x):
    sigma = 0.5
    mu = 9.5  
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2)





#rules
def rule1(p, k, s):
    return min(very_bad(p), very_bad(k), very_bad(s))

def rule2(p, k, s):
    return min(bad(p), bad(k), bad(s))

def rule3(p, k, s):
    return min(average(p), average(k), average(s))

def rule4(p, k, s):
    return min(good(p), good(k), good(s))

def rule5(p, k, s):
    return min(very_good(p), very_good(k), very_good(s))

def defuzzify(rules):
    weights = [0, 25, 50, 75, 100]
    epsilon = 1e-6  # small constant to avoid division by zero
    return sum(rules[i]*weights[i] for i in range(len(rules)))/(sum(rules) + epsilon)


#anfismdoel
def anfis(p, k, s):
    rules = [rule1(p, k, s), rule2(p, k, s), rule3(p, k, s), rule4(p, k, s), rule5(p, k, s)]
    return defuzzify(rules)


linguistic_terms = {
    'very_bad': 0.5,
    'bad': 2.5,
    'average': 5,
    'good': 6.5,
    'very_good': 9.5
}


p_input = input("Enter preparedness level (very_bad, bad, average, good, very_good): ")
k_input = input("Enter knowledge level (very_bad, bad, average, good, very_good): ")
s_input = input("Enter submission level (very_bad, bad, average, good, very_good): ")


p = linguistic_terms[p_input]
k = linguistic_terms[k_input]
s = linguistic_terms[s_input]

print(f"Score: {anfis(p,k,s)} " )
