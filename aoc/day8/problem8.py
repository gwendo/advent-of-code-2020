def find_loop(instr):
    executed = set()
    i = 0
    result = 0
    curr_instr = instr[i]
    while not {i}.issubset(executed):
        executed.add(i)
        if curr_instr[:3] == "acc":
            result = chang_val(curr_instr, result)
            i += 1
        if curr_instr[:3] == "jmp":
            i = chang_val(curr_instr, i)
        if curr_instr[:3] == "nop":
            i += 1
        curr_instr = instr[i]
    return result


def fix_loop(instr):
    tested = set()
    clean = False
    while not clean:
        clean = True
        executed = set()
        i = 0
        result = 0
        changed = False
        while not {i}.issubset(executed):
            curr_instr = instr[i]
            executed.add(i)
            if curr_instr[:3] == "acc":
                result = chang_val(curr_instr, result)
                i += 1
            elif curr_instr[:3] == "jmp":
                if {i}.issubset(tested) or changed:
                    i = chang_val(curr_instr, i)
                else:
                    tested.add(i)
                    changed = True
                    i += 1
            elif curr_instr[:3] == "nop":
                if {i}.issubset(tested) or changed:
                    i += 1
                else:
                    tested.add(i)
                    changed = True
                    i = chang_val(curr_instr, i)
            print(i)
            if i == len(instr):
                break
            if {i}.issubset(executed) or i > len(instr):
                print(executed, result)
                clean = False
                changed = False
                break

    return result


def chang_val(curr_instr, result):
    if curr_instr[4:5] == "+":
        result += int(curr_instr[5:])
    else:
        result -= int(curr_instr[5:])
    return result
