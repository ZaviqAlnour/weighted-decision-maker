def main():
    decision, option_count, criteria_count = firstAsk()
    options = askOption(option_count)
    askCriteria(criteria_count)
    collect_options_points(options)
    

def firstAsk():
    decision = input("Write the Decision Name: ")
    option_count = int(input("How many options do you have?: "))
    criteria_count = int(input("How many criteria will you use?: "))
    print()

    return decision, option_count, criteria_count


def askOption(option_count):
    options = []
    for i in range(option_count):
        options.append(input(f"Enter option {i + 1}: "))

    return options    
   
def askCriteria(criteria):
    criterias = []
    for i in range(criteria):
        criterias.append(input(f"Enter criteria {i + 1}: "))

    return criterias    

def collect_options_points(options):
    options_point = []
    for op in options:
        while True:
            try:
                op_point = int(input(f"Enter point (0 - 10) for {op}: "))
                if op_point < 0 or op_point > 10:
                    print("You have enter point between (0 - 10).")
                    continue
                else:
                    break
            except ValueError:
                print("This is not valid you have to give a number.")
                continue    
    options_point.append(op_point)


main()