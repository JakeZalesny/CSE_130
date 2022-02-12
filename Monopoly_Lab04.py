"""
1. Jake Zalesny

2. Lab 04 Monopoly

3. This program is meant to be able to tell the user whether or not a hotel is available
for purchase on Pennsylvania Avenue

4. The hardest part was understanding the test cases and the expected output

5. This took me about 2 hours to complete

"""
# I set these two as constants, because their value will not change
COST_HOUSE = 200
COST_HOTEL = 200

# This asks the user for all the data needed, it then stores it in prompts and returns it. 
def prompt_the_user() :
    prompts = []
    
    #0
    pc_ave = int(input("What is on Pacific Avenue? "))
    prompts.append(pc_ave)
    
    #1
    nc_ave = int(input("What is on North Carolina Avenue? "))
    prompts.append(nc_ave)
    
    #2
    penn_ave = int(input("What is on Pennsylvania Avenue? "))
    prompts.append(penn_ave)
    
    #3
    cash = int(input("How much cash do you have to spend? $"))
    prompts.append(cash)
    
    #4
    houses = int(input("How many houses are there to purchase? "))
    prompts.append(houses)
    
    #5
    hotels = int(input("How many hotels are there to purchase? "))
    prompts.append(hotels)
    
    #6
    color_group = input("Do you own all of the green properties? (y/n) ")
    prompts.append(color_group.lower())

    return prompts

# This runs through all the options that would stop you from making a purchase
def decisions(prompts) :
    
    if prompts[6] == "n" :
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        return False
    
    elif prompts[0] == 5 and prompts[2] == 4 and prompts[6] == "y" :
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        return False
    
    elif prompts[1] == 5 and prompts[2] == 4 and prompts[6] == "y" :
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
        return False
    
    elif prompts[2] == 5 :
        print("You cannot purchase a hotel if the property already has one.")
        return False
   
    elif prompts[4] == 0:
            print("There are not enough houses available for purchase at this time.")
    
    elif prompts[5] == 0 :
        print("There are not enough hotels available for purchase at this time.")
        return False
    
    else :
        return True

#  This is runs through all the purchase cases    
def purchases(prompts) : 
    if prompts[0] < 4 and prompts[1] < 4 and prompts[2] < 4 :
        factor1 = 4 - prompts[0]
        factor2 = 4 - prompts[1]
        factor3 = 4 - prompts[2]
        house_total = (COST_HOUSE * factor1) + (COST_HOUSE * factor2) + (COST_HOUSE * factor3)
        
        if house_total + COST_HOTEL > prompts[3] :
            return print("You do not have sufficient funds to buy a hotel at this time.")
        
        else :
            print(f"This will cost ${house_total + COST_HOTEL}")
            print(f"\tPurchase 1 hotel and {factor1 + factor2 + factor3} house(s).")
            print(f"\tPut 1 hotel on Pennsylvania and return houses to the bank.")
            print(f"\tPut {factor2} house(s)on North Carolina")
            print(f"\tPut {factor1} house(s) on Pacific.")
            print(f"\tPut {factor3} house(s) on Pennsylvania.")
            return
            
    
    elif prompts[0] < 4 and prompts[1] < 4 :
        factor1 = 4 - prompts[0]
        factor2 = 4 - prompts[1]
        house_total = (COST_HOUSE * factor1) + (COST_HOUSE * factor2)
        
        if house_total + COST_HOTEL > prompts[3] :
            return print("You do not have sufficient funds to buy a hotel at this time.")

        else : 
            print(f"This will cost ${house_total + COST_HOTEL}")
            print(f"\tPurchase 1 hotel and {factor1 + factor2} house(s).")
            print(f"\tPut 1 hotel on Pennsylvania and return houses to the bank.")
            print(f"\tPut {factor2} house(s)on North Carolina")
            print(f"\tPut {factor1} house(s) on Pacific.")
            return
        
    elif prompts[1] < 4 :
        factor1 = 4 - prompts[1]
        house_total = COST_HOUSE * factor1
        
        if house_total + COST_HOTEL > prompts[3] :
            return print("You do not have sufficient funds to buy a hotel at this time.")

        else :
            print(f"This will cost ${house_total + COST_HOTEL}")
            print(f"\tPurchase 1 hotel and {factor1} house(s).")
            print("\tPut 1 hotel on Pennsylvania and return houses to the bank.")
            print(f"\tPut {factor1} house(s) on North Carolina")
            return
        
    elif prompts[0] < 4 :
        factor1 = 4 - prompts[0]
        house_total = COST_HOUSE * factor1
        
        if house_total + COST_HOTEL > prompts[3] :
            return print("You do not have sufficient funds to buy a hotel at this time.") 
        
        else :
            print(f"This will cost ${house_total + COST_HOTEL}")
            print(f"\tPurchase 1 hotel and {factor1} house(s).")
            print("\tPut 1 hotel on Pennsylvania and return houses to the bank.")
            print(f"\tPut {factor1} house(s) on North Carolina")
            return
        
    else :
        print(f"This purchase will cost${COST_HOTEL}")
        print("\tPurchase 1 hotel and 0 house(s).")
        print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
        
        

def main() :
    prompts = prompt_the_user()
    
    if decisions(prompts) == False :
        return
    
    else :
        purchases(prompts)

main()


