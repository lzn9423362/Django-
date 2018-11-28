import requests

url = 'https://fanyi.baidu.com/'


data = {'from': 'zh',
'to': 'en',
'query': '人生苦短我是真的为你哭了',
'transtype': 'translang',
'simple_means_flag': '3',
'sign': '822331.552714',
'token': 'cdaa4cf818092a2998fa7493de7c3902'}



headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# response = requests.post(url, data=query_string, headers=headers)

response = requests.post(url, data=data, headers=headers)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())

print(response)

print(response.content.decode())

