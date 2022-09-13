#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    rens = []
    for i in range(list_length):
        try:
            ren = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            ren = 0
        except IndexError:
            print("out of range")
            ren = 0
        except (ValueError, TypeError):
            print("wrong type")
            ren = 0
        finally:
            rens.append(ren)
    return rens
