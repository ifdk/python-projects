def temp_avg(file_name):
    # Opens the file
    file = open(file_name, "r")
    # Sets total to 0
    total = 0.0
    # Sets num_records to 0
    num_records = 0
    # sets lines to a function that reads each line in the .csv
    lines = file.readlines()
    # sets is_first_record to true
    is_first_record = True
    # for the current line in the file, if the first record or the length
    # of the current line, which had all empty spaces removed via strip, is
    # equal to zero, then first record is false. it will ignore the above if
    #it fits these pre reqs
    for current_line in lines:
        if is_first_record or len(current_line.strip()) == 0:
            is_first_record = False
            continue
        else:
            num_records += 1

        cur_line_list = current_line.split(',')
        cur_temp_str = cur_line_list[1]
        cur_temp_float = float(cur_temp_str[1:-1])
        total = cur_temp_float + total
    avg = total / num_records
    return avg


x = "temp.csv"

print(temp_avg(x))
