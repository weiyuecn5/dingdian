from spider import info_list
from getcontens import get_allzj_title


def book_number(search_name):
    data = {}
    info = []
    for item in info_list.find():
        if search_name in item:
            info = item[search_name]
        bookname = [i[1] for i in info]
        for i, e in enumerate(bookname):
            data[i] = e
    # print(data)
    return data
    # for k,v in data.items():
    #     print(k)

def contents_number(list):
    data = {}
    for i, e in enumerate(list):
        data[i] = e
    # print(data)
    return data



# search_name = '诛仙'
#
# list = get_allzj_title(search_name)
# # print(list)
# contents_number(list)
#
# book_number(search_name)