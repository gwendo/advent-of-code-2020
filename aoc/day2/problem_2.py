def find_valid_passwords(password_lines, policy):
    return len(list(filter(lambda pw: policy(pw), password_lines)))


def is_password_valid(password_line):
    policy, password = password_line.split(':')
    counts, character = policy.split(' ')
    min_count, max_count = map(int, counts.split('-'))
    return min_count <= password.count(character) <= max_count


def is_password_valid2(password_line):
    policy, password = password_line.split(':')
    password = password.strip()
    counts, character = policy.split(' ')
    min_count, max_count = map(int, counts.split('-'))
    return (password[min_count - 1] == character or password[max_count - 1] == character) \
           and not (password[max_count - 1] == password[min_count - 1])

