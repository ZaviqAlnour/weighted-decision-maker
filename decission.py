def main():
    decision, option_count, criteria_count = firstAsk()
    askOption(option_count)
    

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
   





main()