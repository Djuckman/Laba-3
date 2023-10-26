# TODO Напишите функцию find_common_participants
def find_common_participants(surnames1, surnames2, delim=','):
    common_list = list(set(surnames1.split(delim)).intersection(set(surnames2.split(delim))))
    common_list.sort()
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))