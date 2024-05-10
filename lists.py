def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
    if len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
    if len(list_to_remove_elements) >=1:
        del list_to_remove_elements[0]
    return list_to_remove_elements


print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))





def add_elements(list_to_add_elements):
    ultimo_numero = len(list_to_add_elements)+1
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.insert(ultimo_numero, "Yellow")

    return list_to_add_elements

print(add_elements(['Red', 'Green', 'White', 'Black']))


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

print(is_empty(""))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'], ['Red', 'Green']))


def list_of_lists(list_of_lists_to_modify):
    a = list_of_lists_to_modify[0][0:2]
    b = list_of_lists_to_modify[1][1:4]
    c = list_of_lists_to_modify[2][-2:]
    list_of_lists_to_modify = [a, b, c]
    return list_of_lists_to_modify

print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
    
