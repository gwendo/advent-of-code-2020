
def group_answers(lines):
    groups = []
    group = set()
    for l in lines:
        if not l:
            groups.append(group)
            group = set()
        else:
            for c in l:
                group.add(c)
    groups.append(group)
    return sum(map(lambda g: len(g), groups))


def group_answers_all(lines):
    groups = []
    group = set()
    curr_group = set()
    first = True
    for l in lines:
        if not l:
            groups.append(group)
            group = set()
            first = True
        else:
            for c in l:
                curr_group.add(c)
            if first:
                group = curr_group
                curr_group = set()
                first = False
            else:
                group = group.intersection(curr_group)
                curr_group = set()

    groups.append(group)
    return sum(map(lambda g: len(g), groups))
