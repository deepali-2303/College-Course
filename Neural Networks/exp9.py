def membership_low(x, a, b):
    return max(0, min((b - x) / (b - a), 1))

def membership_medium(x, a, b, c, d):
    if a < x <= b:
        return (x - a) / (b - a)
    else:
        return max(0, min((d - x) / (d - c), 1))

def membership_high(x, a, b):
    return max(0, min((x - a) / (b - a), 1))

def apply_rules(dirt, grease):
    rules = [
        max(membership_high(dirt, 50, 100), membership_high(grease, 50, 100)),
        max(membership_high(dirt, 50, 100), membership_medium(grease, 0, 50, 50, 100)),
        max(membership_high(dirt, 50, 100), membership_low(grease, 0, 50)),
        max(membership_medium(dirt, 0, 50, 50, 100), membership_high(grease, 50, 100)),
        max(membership_medium(dirt, 0, 50, 50, 100), membership_medium(grease, 0, 50, 50, 100)),
        max(membership_medium(dirt, 0, 50, 50, 100), membership_low(grease, 0, 50)),
        max(membership_low(dirt, 0, 50), membership_high(grease, 50, 100)),
        max(membership_low(dirt, 0, 50), membership_medium(grease, 0, 50, 50, 100)),
        max(membership_low(dirt, 0, 50), membership_low(grease, 0, 50))
    ]
    return rules

def aggregate_output(rules, wash_time_values):
    aggregated_output = [rule * value for rule, value in zip(rules, wash_time_values)]
    return max(aggregated_output)

def defuzzify(aggregated_output, rules):
    numerator = aggregated_output
    denominator = sum(rules)
    return numerator / denominator

dirt_level = 60
grease_level = 70

rules = apply_rules(dirt_level, grease_level)

wash_time_values = [0, 10, 15, 40, 60]

aggregated_output = aggregate_output(rules, wash_time_values)

wash_time_output = defuzzify(aggregated_output, rules)

print(f"Wash Time: {wash_time_output}")
