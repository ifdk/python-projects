def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def temp_avg(file_name, state):
    file = open(file_name, "r")
    total = 0.0
    num_records = 0
    lines = file.readlines()
    is_first_record = True

    for current_line in lines:
        if is_first_record or len(current_line.strip()) == 0:
            is_first_record = False
            continue

        cur_line_list = current_line.split(',')
        curr_state = cur_line_list[0]
        curr_state_str = curr_state[1:-1]
        if curr_state_str == state:
            cur_temp_str = cur_line_list[2]
            cur_temp_str = cur_temp_str[1:-1]
            if is_float(cur_temp_str):
                num_records += 1
                total = float(cur_temp_str) + total
            else:
                continue
        else:
            continue
    avg = total / num_records
    return avg


x = "multi_state_temperatures.csv"
print(temp_avg(x, "VA"))
