import requests
import re
from cgitb import text
from operator import truediv
from tkinter import E
import zmail

def query(roomid):
    udata=''
    data1='Yzm=123&RoomID='
    url='https://zywxhd02.gxust.edu.cn/Home/GetRoomInfo'
    h={
        "Host":"zywxhd02.gxust.edu.cn",
        "Origin":"https://zywxhd02.gxust.edu.cn",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"
    }

    res=requests.post(url,data=data1+roomid,headers=h)
    udata=res.text
    new_data=udata[-25:-19]
    find_a=re.compile("\d")
    find_x=find_a.findall(new_data)
    find_x.insert(-2,'.')

    data_1="".join(find_x)
    end_data=float(data_1)
    return end_data;



def send_email(remail, text1, text2):
    MAIL = {
        "from": '****@qq.com', #推送信息发送者的邮箱
        "pwd": '****' #推送邮箱的IMAP/SMTP服务授权码
    }
    receiver_list = [remail]

    MAIL_CONTENT = {
        'subject': "科大宿舍电费推送",
        'content_text': '您的宿舍' + text1 + text2,

    }

    try:
        # 登录邮箱
        server = zmail.server(MAIL['from'], MAIL['pwd'])
        # 发送邮件
        server.send_mail(receiver_list[0], MAIL_CONTENT)

        return 1;

    except Exception as e:
        return 0;


if __name__ == "__main__":
    input('请输入宿舍号')
    input('请输入宿舍id')
    input('请输入邮箱（仅支持qq邮箱）')
    a=query(aa)
    if a<=200:
        text2=str(a)
        send_email(remail, text1, text2)
    else:
        print(a)
