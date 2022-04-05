module = input("Enter Module Code: ")

match module:
    case "CSC1006":
        print("Mathematics 2")
    case "CSC1007":
        print("Operating System")
    case "CSC1008":
        print("Data Structures and Algorithms")
    case "CSC1009":
        print("Object Oriented Programming")
    case "CSC1010":
        print("Computer Networks")
    case _:
        print("Unknown Module")

num = []
for x in range(66,103):
    if(x%2 == 1):
        num.append(x)

num.reverse()
for x in range(len(num)):
    print(num[x])