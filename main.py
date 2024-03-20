#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
import json
expenses = []
expenses_file = open('expenses.json')
expenses = json.load(expenses_file) 
expenses_file.close()
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    command = input("\nChoose command:")
    if command == "1":
        expenses_name = str(input("What's the name of the thing you bought?"))
        expenses_cost = int(input("How much did it cost?")) 
        expenses_category = str(input("In which category was this expense?"))
        x = {
            "name": expenses_name,
            "cost": expenses_cost,
            "category": expenses_category,
        }
        expenses.append(x)
        
        pass
    elif command == "2":
        print(expenses)
        pass
    elif command == "3":
        def sorting(lielakie_izdevumi):
            return int(lielakie_izdevumi["cost"])
        expenses.sort(key = sorting, reverse = True)
        print(expenses[0:10])
        pass
    elif command == "4":
        def sorting(mazakie_izdevumi):
            return int(mazakie_izdevumi["cost"])
        expenses.sort(key = sorting)
        print(expenses[0:10])
        pass
    elif command == "5":
        for expense in expenses:
            total_avg = 0
            total = total_avg + int(expenses[1])
        print("Average expenses of the list = ", total_avg/total)
        pass
    elif command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

