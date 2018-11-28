import requests

url = 'https://www.baidu.com'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

response = requests.get(url, headers=headers)



# response.encoding = 'utf-8'


# print(response.text)#获取网页的字符串

print(response.content.decode())