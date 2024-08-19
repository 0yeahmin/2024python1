# nums=list(range(1,10,2))
# print(nums)
# print(type(nums))
# for i in range(2,11,2):
#     print(i)
# nums=(3,5,2,8,9)
# print(type(nums))
# for i in nums:
#     print(i)

def p(space, space_num,*args):
    str=""
    for i in args:
        str=str+(space*space_num)+i
    print(str)
p("a",3,"s","d")
p("a",3,"s","d","f","g")