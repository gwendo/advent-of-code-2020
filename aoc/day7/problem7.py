
def find_bags(ruleset):
    bags = {}
    for rule in ruleset:
        color = rule.split("contain")[0].strip()[:-5]
        if "no other bags" not in rule:
            bags[color] = set(map(lambda s: (int(s.strip()[0]), s.strip()[1:].strip()[:-4].strip()), rule[:-1].strip().split("contain")[1].strip().split(",")))
        else:
            bags[color] = []
    return bags


def find_bag_count(ruleset):
    bags = find_bags(ruleset)
    shiny = {"shiny gold"}
    result = set()
    filtered_bags = recurse_bags(shiny, bags, result)
    return len(filtered_bags)


def find_bag_contains(ruleset):
    bags = find_bags(ruleset)
    return recurse_count_bags("shiny gold", bags)


def recurse_count_bags(bag,bags):
    summa = 0
    if len(bags[bag]) == 0:
        return 0
    else:
        summa += sum(list(map(lambda b: b[0] + b[0] * recurse_count_bags(b[1], bags), bags[bag])))
        return summa


def recurse_bags(bag, bags, result):
    filtered_bags = list(filter(lambda k: bag.issubset(set(map(lambda v: v[1], bags[k]))), bags.keys()))
    if len(filtered_bags) == 0:
        return result
    else:
        for b in filtered_bags:
            result.add(b)
            recurse_bags({b}, bags, result)
    return result
