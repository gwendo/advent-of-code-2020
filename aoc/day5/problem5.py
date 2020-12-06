
def find_seat_id(seat):
    seat = find_seat(seat)
    return (seat[0] * 8) + seat[1]


def find_available_seat(seat_list):
    available_seats = set(range(min(seat_list), max(seat_list))) - set(seat_list)
    return available_seats.pop()


def find_seat(seat):
    rows = list(range(0, 128))
    row = split_list(seat[:7], rows, 'F')
    seats = list(range(0, 8))
    seat = split_list(seat[-3:], seats, 'L')
    return row[0], seat[0]


def split_list(c, seat_list, front_char):
    if len(c) == 0:
        return seat_list
    else:
        half = len(seat_list)//2
        if c[0] == front_char:
            return split_list(c[1:], seat_list[:half], front_char)
        else:
            return split_list(c[1:], seat_list[half:], front_char)
