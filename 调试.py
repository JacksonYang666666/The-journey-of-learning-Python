# Jackson Yang的编程初体验
#银行输入密码的简易代码

#用for-in循环
for _ in range(3):
    pwd=input('请输入您的密码：')
    if pwd=='666666':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('您的密码输入次数已达上限')

#用while循环
a=0
while a<3:
    pwd=input('请输入您的密码：')
    if pwd=='666666':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1
else:
    print('您的密码输入次数已达上限')