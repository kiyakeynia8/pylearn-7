my_list = [1,4,4,1]
my_list1 = [1,4,7,4,1]
my_list2 = [1,4,3,1]
status = []

def check(my_list,status):
    if len(my_list) % 2 == 0:
        for i in range(len(my_list)):
            a = len(my_list) - i-1

            if my_list[i] == my_list[a]:
                status.append("true")
            else:
                status.append("false")

        if "false" not in status:
            return True
        else:
            return False
    
    else:
        for i in range(int(len(my_list)// 2)):
            a = len(my_list) - i-1

            if my_list[i] == my_list[a]:
                status.append("true")
            else:
                status.append("false")

        if "false" not in status:
            return True
        else:
            return False

print(check(my_list2,status))