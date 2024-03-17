'''You are given list of integers (int). Your task in this mission is to duplicate
 all zeros (think about donuts ;-P) and return the result as any Iterable.'''

def double_donut(income_list):
    result_list = []
    for item in income_list:
        result_list.append(item)
        if item == 0:
            result_list.append(item)
    return result_list


print(double_donut([0,0,1,0]))