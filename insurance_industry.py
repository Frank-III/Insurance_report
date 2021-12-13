import requests
import re


headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/xml, text/xml, */*; q=0.01',
    'Origin': 'http://www.iachina.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://www.iachina.cn/col/col41/index.html?uid=1508&pageNum=7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,zh-TW;q=0.6,ru;q=0.5',
}
params = (
    ('startrecord', '1'), ('endrecord', '107'), ('perpage', '40'), )
data = {
    'col': '1',
    'appid': '1',
    'webid': '1',
    'path': '/',
    'columnid': '41',
    'sourceContentType': '8',
    'unitid': '1508',
    'webname': '中国保险行业协会',
    'permissiontype': '0'
}
response = requests.post('http://www.iachina.cn/module/web/jpage/dataproxy.jsp', headers = headers, params = params, data = data, verify = False)

links=re.findall('<a href="(.*?)">',response.text)
titles=re.findall('html">(.*?)</a>',response.text)
print(len(links))
for link,title in zip(links,titles):
    print(title,'http://www.iachina.cn/'+link)
    with open('web_data.csv','a',encoding='utf-8-sig') as csv:
        csv.write(f'{title},http://www.iachina.cn{link}\n')

