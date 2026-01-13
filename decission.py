def main():
    data = {} 

    decision, option_count, criteria_count = firstAsk()
    options = askOption(option_count)
    criterias = askCriteria(criteria_count)
    collect_criteria_points(options, criterias, data)
    

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
    print()    
    return options    
   
def askCriteria(criteria):
    criterias = {}

    for i in range(criteria):
        crt = (input(f"Enter criteria {i + 1}: "))
        criterias[crt] = {}
        while True:
                try:
                    Weight = int(input("Weight (1–10): "))
                    if Weight < 0 or Weight > 10:
                        print("You have enter point between (0 - 10).")
                        continue
                    else:
                        break
                except ValueError:
                    print("This is not valid you have to give a number.")
                    continue 
        criterias[crt] = Weight
    print(criterias)
    return criterias    

def collect_criteria_points(options, criteria, data):
    for op in options:
        print(f"\n------ point for {op} --------\n")
        data[op] = {}

        for cr in criteria:
            while True:
                try:
                    op_point = int(input(f"Enter point (0 - 10) for {cr}: "))
                    if op_point < 0 or op_point > 10:
                        print("You have enter point between (0 - 10).")
                        continue
                    else:
                        break
                except ValueError:
                    print("This is not valid you have to give a number.")
                    continue 
            data[op][cr] = op_point

main()