from random import choice

myDict = {"fruit" : ["apple", "blueberry", "pineapple"], "vegetable" : ["broccoli", "potato", "tomato"]}

a = ["maya", "apple", "potato", "blueberry", "laptop", "icecream", "tomato", "candy"]

vegetables = myDict['vegetable']
fruits =  myDict['fruit']

def exchange(fruits:list = fruits, vegetables:list = vegetables) -> list:

    copy_list = a[:]

    for item in a:

        item_index = a.index(item)
        random_fruit = choice(fruits)
        random_vegetable = choice(vegetables)

        if item in fruits:
            
            while random_fruit == item: 

                random_fruit = choice(fruits)

            copy_list.pop(item_index)
            copy_list.insert(item_index, random_fruit)
            

        elif item in vegetables:

            
            while random_vegetable == item:

                random_vegetable = choice(vegetables)
                
            copy_list.pop(item_index)
            copy_list.insert(item_index, random_vegetable)
            
           
    return copy_list

a = exchange()
print(a)