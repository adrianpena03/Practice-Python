print("Imported My Module...")

test = "Test String"

# Find the index of a value in a list
def find_index(list_to_search, target):
    for index, value in enumerate(list_to_search):
        if value == target:
            return index

    return -1 # If the value does not exist in the list, return -1


def func1():
    print("Hello!")

def Lis2Str(lis):
    lis_str = [str(num) for num in lis]
    str_join = ",".join(lis_str)
    return str_join

def RemovePrime(lis):
    new_list = []
    for num in lis:
        if num <=3:
            continue
        else:
            for i in range(2, int(num**.05) + 1):
                if num % i == 0:
                    new_list.append(num)
                    break
                else:
                    continue
    return new_list

def PopulateDictionary(list_1, list_2):
    dict = {}
    for i in range(len(list_1)):
        key = list_1[i]
        value = list_2[i]
        dict[key] = value
    return dict

def nIndict(n):
    my_dict = {'name': 'John', 'expertise': 'Math'}
    if n in my_dict.values():
        return True
    else:
        return False
    
def LowestVal(dict):
    min_value = min(dict.values())
    for key, value in dict:
        if value == min_value:
            return key