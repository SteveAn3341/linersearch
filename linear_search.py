array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
     for i in range(len(array_to_search_through)):
         if value_to_find ==array_to_search_through :
           print(i)
           return i


    

def linear_search_global(value_to_find, array_to_search_through):
    index = []
    for i in range(len(array_to_search_through)):
        if value_to_find ==array_to_search_through :
            index.append(i)
        return index
