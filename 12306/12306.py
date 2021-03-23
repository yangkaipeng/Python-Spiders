import time
from chaojiying import Chaojiying_Client
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
options = Options()
# 设置无头浏览器
# options.headless = True
# 防反爬
options.add_experimental_option('excludeSwitches',['enable-automation'])

def login(url):
    # 实例化一个driver
    with webdriver.Chrome(options=options) as driver:
        driver.get(url)   # 发送请求
        driver.find_element_by_class_name('login-hd-account').click()   # 切换到账号登录
        driver.fullscreen_window()                               # 全屏显示
        loginImg = WebDriverWait(driver,5,0.2).until(            # 显示等待5秒，直到验证码加载出来
            EC.presence_of_element_located((By.ID,'J-loginImg'))
            )
        ImgSize = loginImg.rect             # 获取验证码的尺寸和位置
        driver.save_screenshot('12306.png')       # 将整个页面截屏保存
        rangle = (ImgSize['x'],ImgSize['y'],ImgSize['x']+ImgSize['width'],ImgSize['y']+ImgSize['height'])
        frame = Image.open('12306.png').crop(rangle)   # 通过验证码的左上角和右下角坐标，截屏验证码图片
        frame.save('code.png')               # 保存验证码图片
        # 使用超级鹰识别出验证码中待点击个图的位置
        cjy = Chaojiying_Client('超级鹰账户', '超级鹰密码', '913533')	    
        im = open('code.png', 'rb').read()
        result = cjy.PostPic(im, 9004)['pic_str']  # ‘96,23|67,11’
        points = process_site(result)  # 处理成[[‘96‘,‘23’],[‘67’,‘11’]]
        print(points)   
        driver.find_element_by_id('J-userName').send_keys('账户')  # 输入账户
        time.sleep(1)
        driver.find_element_by_id('J-password').send_keys('密码')   # 输入密码
        time.sleep(1)
        # 依次找到识别物并点击
        for l in points:
            x = int(l[0])
            y = int(l[1])
            ActionChains(driver).move_to_element_with_offset(loginImg,x,y).click().perform()  
            time.sleep(1)
        driver.find_element_by_id('J-login').click()   # 点击登录按钮
        time.sleep(3)
        # 最后可能会因弹出滑块验证码而失败

def process_site(result):
    points = []
    if '|' in result:
        for xys in result.split('|'):
            points.append((xys.split(',')))
    else:
        points.append(result.split(','))
    return points


url = 'https://kyfw.12306.cn/otn/resources/login.html'
login(url)