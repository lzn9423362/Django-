# json解析: json字符串　=>　json对象　json.load(fp) , json.loads(string)
# json序列化： json对象　=>　json字符串　json.dump(fp) json.dumps(string)

import json

#JSON字符串
# "hello" 是JSON字符串　'hello'不是
#'[]': 是
#'{}': 是
#'{"like":['code', 'movie']}' :　是
# "{'name': 'lisi'}" : 不是
# '{"name":' 不是

#json解析: json字符串 => json对象(python字典, 列表) json.load(fp), json.loads(string)
json_str = '{"name": "lisi", "likes": ["movie", "code"]}'
json_obj = json.loads(json_str)
print(json_obj)
print(type(json_obj))


json_obj = {'name:': 'lisi', 'likes': ['movie', 'code']}

json_str = json.dumps(json_obj)
print(json_str)
print(type(json_str))