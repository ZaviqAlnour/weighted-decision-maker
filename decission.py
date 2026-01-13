def main():
    decision, option_count, criteria_count = firstAsk()
    askOption(option_count)
    askCriteria(criteria_count)
    

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




main()