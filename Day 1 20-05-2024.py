#ps1
# from collections import Counter
# a,b = input(),input()
# d =  Counter(a)
# e = Counter(b)
# if d==e:
#     print("YES")
# else:
#     print("NO")
#ps2
# class stack:
#     def __init__(self,l):
#         self.l = l
#     def push(self,x):
#         self.l.append(x)
#     def pop(self):
#         self.l.pop()
#     def peek(self):
#         return self.l[-1]
# l = [1,2,4]
# st = stack(l)
# st.push(9)
# print(l)
# st.pop()  
# print(l)
# print(st.peek())  
#ps3
# s = "54367+-*+"
# st = []
# for i in s:
#     if i.isdigit():
#         st.append(i)
#     else:
#         a= int(st.pop())
#         b = int(st.pop())
#         if i=="+":
#             st.append(a+b)
#         elif i=="-":
#             st.append(a-b)
#         elif i=="*":
#             st.append(a*b)
#         elif i=="/":
#             st.append(a/b)
# print(st[-1])
s = [1,2,3,4,5,6,7,8,9,10,11,12]
n = 3
f = 0
while s:
    if f==0:
        for i in range(n):
            a = s.pop(0)
        f = 1
    else:
        for i in range(n):
            a = s.pop()
        f = 0
print(a)