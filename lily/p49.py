nums=list(range(0,20,2))
nums[7]=60
# del nums[2]
nums.remove(10)
greeting=list("hellopython")
greeting.remove('h')
# greeting.pop()
# val=greeting.pop()
# for i in greeting:
#     print(greeting)
#     val=greeting.pop()
#     # print(val)
for i in range(10):
    greeting.insert(0,"0")
    greeting.pop(-1)
    print(greeting)