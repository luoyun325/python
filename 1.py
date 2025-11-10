s=input("输入一个字符串:")
s1=s.lower()
s2=s1[::-1]
# 检查是否全部是字母
if not s.isalpha():
    print("No")
else:
    if s1==s2:
        print("Yes")
    else:
        print("No")
print("软工1班,2415304132,陆奕涵")