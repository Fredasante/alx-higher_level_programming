#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = 0
    for idx in range(list_length):
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
