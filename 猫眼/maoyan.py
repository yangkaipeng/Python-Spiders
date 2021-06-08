# import requests
# from fontTools.ttLib import TTFont
# import re
# from lxml import etree

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
# }

# def get_response(url):
#     headers['Cookie'] = 'uuid_n_v=v1; uuid=FAD17120A69511EBAA337D02419931DB3657700772344CB6B601D4537FC3E138; _csrf=1136455110e99d0fc63f0271b35f07a4969136e560e025ee708f98130c1791ce; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=1790e6f9aa0c8-0151e38e670345-103c6054-13c680-1790e6f9aa0c8; _lxsdk=FAD17120A69511EBAA337D02419931DB3657700772344CB6B601D4537FC3E138; __mta=248479288.1619444866334.1619444866334.1619444866334.1; _lxsdk_s=1790e6f9aa1-940-fbc-74d%7C%7C3'
#     response = requests.get(url,headers=headers,verify=False)
#     # print(response.text)
#     return response

# def excute_response(response, font_name):
#     text = response.text
#     woff_url = re.findall(r'//vfile.meituan.net/colorstone/.*\.woff',text)[0]
#     woff_url = 'https:'+woff_url
#     headers['Referer'] = 'https://maoyan.com/'
#     response = requests.get(woff_url,headers=headers,verify=False)
#     with open(font_name,'wb') as f:
#         f.write(response.content)
#     print(woff_url)

# def convert_font(font_name):
#     # 此处可借助第三方工具或者在线平台识别出来 http://blog.luckly-mjw.cn/tool-show/iconfont-preview/index.html
#     num_list = [6,3,7,9,1,8,0,4,2,5]
#     # 建立字体文件对象
#     base_font = TTFont(font_name)
#     # 获取编码数据
#     cont_list = base_font.getGlyphOrder()[2:]
#     # 替换成html中的样式
#     new_cont_list = [i.replace('uni','').lower() for i in cont_list]
#     # 生成一个映射关系
#     num_map = dict(zip(new_cont_list, num_list))
#     print(num_map)
#     return num_map
#     # 转换成xml格式
#     # base_font.saveXML("maoyan_pf.xml")

# def excute_data(response,num_map):
#     # print(response.text)
#     html = etree.HTML(response.text)
#     # print(html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[2]/text()'))
#     dl = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
#     print(dl)
#     for dd in dl:
#         title = dd.xpath('div/div/div[1]/p[1]/a/text()')[0]
#         actors = dd.xpath('div/div/div[1]/p[2]/text()')[0].strip('主演：')
#         date = dd.xpath('div/div/div[1]/p[3]/text()')[0].strip('上映时间：')
#         add = dd.xpath('div/div/div[2]/p[1]/span/span/text()')[0].split(r'\u')
#         print('add',add)
#         total = dd.xpath('div/div/div[2]/p[2]/span/span/text()')[0].split(r'\u')
#         print('total',total)
#         data = {'电影名':title,'主演':actors,'上映时间':date,'新增想看':list_2_dict(add,num_map),'总共想看':list_2_dict(total,num_map)}
#         print(data)

# def list_2_dict(num_list, num_map):
#     return ''.join([num_list[i] for i in num_list if i in num_map.keys()])

# if __name__ == '__main__':
#     font_name = r'font_name.woff'
#     url = 'https://maoyan.com/board/6'
#     response = get_response(url)
#     excute_response(response, font_name)
#     num_map = convert_font(font_name)
#     excute_data(response,num_map)

import chardet
a = '\uf88a\ue5e2\ue343\ue7a1\uf848\ue5e2'

print(chardet.detect(a))