def create_sf():
    shared_file = open('Shared_file.txt', 'w')
    shared_file.close()
    f1 = open('1.txt', 'r', encoding='utf-8')
    f2 = open('2.txt', 'r', encoding='utf-8')
    f3 = open('3.txt', 'r', encoding='utf-8')
    file1_list = f1.readlines()
    file2_list = f2.readlines()
    file3_list = f3.readlines()
    f1.close()
    f2.close()
    f3.close()
    all_list = (file1_list, file2_list, file3_list)
    all_list = sorted(all_list, key=len)

    def file_number(file_list):
        if file_list == file1_list:
            return '1'
        elif file_list == file2_list:
            return '2'
        else:
            return '3'


    for file_list in all_list:
        for st_number, st in enumerate(file_list, start=1):
            shared_file = open('Shared_file.txt', 'r', encoding='utf-8')
            if st not in shared_file:
                shared_file = open('Shared_file.txt', 'a', encoding='utf-8')
                shared_file.write('Строка номер ' + str(st_number) + ' файла номер ' + file_number(file_list) + ' ' + st )
                shared_file.close()
            else:
                shared_file.close()





create_sf()
