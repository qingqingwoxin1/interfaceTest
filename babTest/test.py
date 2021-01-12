file ="./testFile/sqlFile/m_project_member"
f=open(file,"r")
# print(id(f))
# read_data=f.readlines()
# print(f.readline())
# print(f.readline())
# print("input"+f.read(2))
# print(id(f))
# print(f.readlines())
# print(id(f))
# print(read_data[0].replace("\n",""))
# print(read_data[1].replace("\n",""))
# print(f[1])
# print(f.readlines(0)[0].replace("\n",""))

# list = [1,2,3,4,5,6,7]
# # 第一种方式
# l = []
# for i in list:
#     if i%2==0:
#         l.append(i)
#
# print(l)
# print(list)
#
# # 列表推导式


# print('hellow world')
# str = "abcaabbccabc"
# str1 = str.replace('abc','123')
# print(str1)
# a = input("请输入数字: ")
# b=len(a)
# for i in range (b):
#     if(a[i]==a[b-i-1]):
#         c=1
#     else:
#         c=0
# if(c==1):
#     print("这是回文数")
# else:
#     print("这不是回文数")

def new_replace(raw, old, new, times=None):
    if times == None:
        times = raw.count(old)
    lists = list(raw)
    sub_index = []
    for i in range(len(lists)):
        if lists[i:i + len(old)] == list(old):
            sub_index.append(i)
    n = 0
    for j in sub_index:
        if times > 0:
            ffset = n * (len(new) - len(old))
            j = j + ffset
            lists[j:j + len(old)] = new
            n += 1
            times -= 1
    return "".join(lists)


ch = "abcabc1"
res = new_replace(ch, "c", "123",1)
print(res)