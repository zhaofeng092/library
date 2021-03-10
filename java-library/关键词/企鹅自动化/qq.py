# -*- coding: utf-8 -*-
# @Time : 2021/3/9 9:46
# @公众号 : Python图书馆
# @File : qq.py
# @Software: PyCharm


from appium import webdriver
import time

desired_caps={
    'platformName':'Android',
    'platformVersion':'8.1',
    'deviceName':'xxx',
    'appPackage':'com.tencent.qqlite',  # 自动化应用
    'appActivity':'com.tencent.mobileqq.activity.SplashActivity',
    #'unicodeKeyboard':True,
    #'resetKeyboard':True,
    'noReset':True,
    'newCommandTimeout':6000,
    'automationName':'UiAutomator2'
}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.implicitly_wait(10)

driver2=driver.find_element_by_id('recent_chat_list')

list2=driver2.find_elements_by_class_name('android.widget.LinearLayout')
print('当前QQ消息为%d个'%(len(list2)))

time.sleep(2)
list2[0].click()


def send_Message(text2:str):   # 发消息
    driver4=driver.find_element_by_id('inputBar')
    driver4.find_element_by_id('input').send_keys(text2)
    driver4.find_element_by_id('fun_btn').click()
    time.sleep(2)
    print("发送消息:%s"%(text2))

list4=[
"刘邦，字季，沛郡丰邑（今江苏省丰县）人。中国历史上杰出的政治家、战略家和军事指挥家，汉朝开国皇帝，汉民族和汉文化的伟大奠基者和开拓者，对汉族的发展以及中国的统一有突出贡献。",
"还没",
"湖南省，简称“湘”，是中华人民共和国省级行政区，省会长沙，界于北纬24°38′～30°08′，东经108°47′～114°15′之间，东临江西，西接重庆、贵州，南毗广东、广西，北连湖北，总面积21.18万平方千米。"
]

while True:
    try:
        driver3=driver.find_element_by_id('listView1')
        list3=driver3.find_elements_by_class_name('android.widget.RelativeLayout')
        text=list3[-1].find_element_by_id('chat_item_content_layout').text
        print('收到消息:%s'%(text))      # 接收消息

        time.sleep(5)
        if(text=='你好，请帮我查阅一下刘邦的简介'):
            send_Message(list4[0])
        elif(text=="你吃中饭了没"):
            send_Message(list4[1])
        elif(text=="介绍一下湖南呗！"):
            send_Message(list4[2])

    except Exception as e:
        pass