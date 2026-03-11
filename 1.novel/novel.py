#怎么发送请求：requests库
import requests
from lxml import etree
import time
import random

# 发送给谁：目标网站的URL
url = 'https://www.85xs.cc/book/douluodalu1/1.html'
# 创建session，会话对象可以保持cookie，避免重复发送请求
session = requests.Session()
while True:
    print(url)
    # 伪装自己
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
    }

    # 设置代理(以上网站我需要代理才能访问)
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }


    # 发送请求
    response = session.get(url, headers=headers, proxies=proxies, timeout=30)

    # 设置编码
    response.encoding = 'utf-8'

    # 打印响应内容
    # print(response.text)

    # 处理响应内容
    html = etree.HTML(response.text)
    # 如果显示的不是中文而是[<Element h1 at 0x186ebc78d80>]，说明xpath表达式没有匹配到元素
    # 可以尝试使用text()方法获取元素的文本内容
    content = html.xpath('//*[contains(@class, "entry-text")]//div[contains(@class, "m-post")]//p/text()')
    title = html.xpath('//h1[normalize-space(text())]/text()')[0]

    # print(content)
    print(title)
    # 提取下一页的URL
    try:
        url = 'https://www.85xs.cc' + html.xpath('//body/div[1]/div[2]/table[1]/tbody/tr/td[2]/a/@href')[0]
    except:
        print('没有下一页了')
        break
    


    # 保存内容
    # with open(f'斗罗大陆.txt', 'a', encoding='utf-8') as f:
    #     f.write(title + '\n\n')
    #     for p in content:
    #         f.write(p.strip() + '\n\n')

    # 关闭响应
    response.close()
    
    # 随机等待0.5-2秒，避免对目标网站造成过大压力
    time.sleep(random.uniform(0.5, 2))

session.close()
