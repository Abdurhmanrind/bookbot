def get_book_word_num(book_contents):
    list_words = book_contents.split()
    return len(list_words)
#---------------------------------------------------

def get_chara_num(book_contents):
    all_charac = {}
    all_lower_text = book_contents.lower()
    for character in all_lower_text:
        if character not in all_charac:
            all_charac[character] = 1
        else:
            all_charac[character] += 1
    return all_charac
#---------------------------------------------------

def sorting_list(unsorted_dic):
    sorted_list = []
    list_num = []
    for i in unsorted_dic:
        if i.isalpha():
            each_dic = {}
            each_dic["char"] = i
            each_dic["num"] = unsorted_dic[i]
            sorted_list.append(each_dic)
            list_num.append(unsorted_dic[i])

    return sorted_list , list_num