#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            i += 1
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            pass
        except IndexError:
            print("out of range")
            result = 0
            pass
        finally:
            new_list.append(result)
    return new_list
