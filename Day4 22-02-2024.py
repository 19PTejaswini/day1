#ps1
# s = input()
# s = s.lower()
# s = s.replace(" ","")
# d = {}
# for i in s:
#     if i in "qwertyuiopasdfghjklzxcvbnm":
#         if i in d:
#             d[i] +=1
#         else:
#             d[i] = 1
# #print(d)
# if len(d)==26:
#     print("pangram")
# else:
#     print("not pangram")
# s = input()
# s = s.lower()
# s = s.replace(" ","")
# s = set(s)
# if len(s)==26:
#     print("pangram")
# else:
#     print("not pangram")

#ps2
# s = input()
# d = {}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i] = 1
# for i in s:
#     if d[i] >1:
#         print(i)
#         break
# else:
#     print(".")
#ps3
# d={}
# for i in range(n):
#     name, num= input().split()
#     d[name]=num
# while True:
#     s = input()
#     if s in d:
#         print(f"{s}={d[s]}")
#     else:
#         print("Not found")


#ps4
# a = int(input())
# d = {}
# for i in range(a):
#     s = input()
#     if s in d:
#         d[s] += 1
#     else:
#         d[s] = 1
# print(d)
# m = max(d.values())
# l = []
# for i in d:
#     if d[i] == m:
#         l.append(i)
# print(max(l) ,m)
#ps5
# for i in range(int(input())):
#     a,b = map(int,input().split())
#     d = {}
#     for _ in range(b):
#         k,l = input().split()
#         if l in d:
#             d[l].append(k)
#         else:
#             d[l] = [k]
#     for k in d:
#         if len(d[k])!=len(set(d[k])):
#             print(f"Scenario #{i+1}: impossible")
#             break
#     else:
#         print(f"Scenario #{i+1}: possible")
#ps6
d = {}
for _ in range(int(input())):
    a,b = input().split()
    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)
a = input("Enter required: ")
print(d.get(a,None))
#ps7
d = {}
for _ in range(int(input())):
    a,b,c = input().split()
    if a not in d:
        d[a]={b:c}
    else:
        d[a][b] =c
a = input("Enter required: ")
if a in d:
    m = min(d[a].values())
    for i in d[a]:
        if d[a][i] == m:
            print(i)
else:
    print(None)
