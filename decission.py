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
   
def askCriteria(criteria_count):
    criteria = {}
    for i in range(criteria_count):
        crt = input(f"Enter criteria {i + 1}: ")
        while True:
            try:
                weight = int(input("Weight (1–10): "))
                if weight < 0 or weight > 10:
                    print("You have to enter a number between 0 and 10.")
                    continue
                else:
                    break
            except ValueError:
                print("This is not valid. You have to give a number.")
                continue 
        criteria[crt] = weight
    print()
    return criteria    

def collect_criteria_points(options, criteria, data):
    for op in options:
        print(f"\n------ Points for {op} --------\n")
        data[op] = {}
        for cr in criteria:
            while True:
                try:
                    op_point = int(input(f"Enter point (0 - 10) for {cr}: "))
                    if op_point < 0 or op_point > 10:
                        print("You have to enter a number between 0 and 10.")
                        continue
                    else:
                        break
                except ValueError:
                    print("This is not valid. You have to give a number.")
                    continue 
            data[op][cr] = op_point

def decisionMAKING(data, criteria):
    data_point = {}
    option_net_point = {}
    for option, criteria_dict in data.items():
        data_point[option] = {}
        for cr, point in criteria_dict.items():
            weight = criteria[cr]
            data_point[option][cr] = weight * point
    for option, dict_point in data_point.items():
        option_net_point[option] = sum(dict_point.values())
    return data_point, option_net_point

def main():
    data = {} 
    decision, option_count, criteria_count = firstAsk()
    options = askOption(option_count)
    criteria = askCriteria(criteria_count)
    collect_criteria_points(options, criteria, data)
    data_point, option_net_point = decisionMAKING(data, criteria)
    best_option = max(option_net_point, key=option_net_point.get)
    best_score = option_net_point[best_option]

    print(f"\nDecision: {decision}\n")
    print("Result:")
    print(f"Best Option: {best_option}")
    print(f"Total Score: {best_score}\n")

    for choice, dict_point in data_point.items():
        print(f"Breakdown for {choice}:")
        total = 0
        for criterion, weighted_score in dict_point.items():
            weight = criteria[criterion]
            score = weighted_score
            total += score
            print(f"{criterion}: {score // weight} × {weight} = {score}")
        print("-" * 24)
        print(f"Total = {total}")
        print("______________________________________________________")

if __name__ == "__main__":    
    main()
