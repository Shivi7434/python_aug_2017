# # # input
# # word_list = ['mississippi','miss','lake','que']
# # char = 'o'
# output



def find_char(arr, str):
    myList = []
    for word in arr:
        if str in word:
            myList.append(word)
    return myList

myList = ['hello','world','my','name','is','Anna']
char = 'o'
print find_char(myList,char)

    

# # letter = 'o'
# # new_list = []
# # for letter in wordlist:
# #     if str.contain(letter):
# #         newlist.append(str)
# # print new_list       

# n = "o"  # you can set this too, but this is optional
# def find_letter(lst):
#     # do not set a value to lst in here

#     if not lst:          
#         return 0

#     elif lst[0] == n:  # You checked first element in here
#         return True

#     elif find_letter(lst[1:]):  # since you checked the first element, skip it and return the orher elements of the list
#         return True

#     else: 
#         return False

# lst = ['o','hello', 1]
# print find_letter(lst)

