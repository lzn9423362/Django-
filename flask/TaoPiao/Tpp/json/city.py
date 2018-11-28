import json

import pymysql



# 获取json城市数据并加入数据库中
def city_data():
    #连接数据库
    db = pymysql.Connect(host='localhost', user='root', password='0000', database='tpp', charset='utf8')
    cursor = db.cursor()

    #获取json数据并插入数据库
    with open ('citys.json', 'r', encoding='GBK') as fp:
        #获取json文件中的字典数据
        content_dict = json.load(fp)
        print(content_dict)
        #所有城市的数据
        return_value = content_dict.get('returnValue')
        #获取所有城市字母
        city_letters = return_value.keys()
        #遍历所有城市字母
        # for city_letter in city_letters:

            # cursor.execute('insert into city_letter(letter) VALUES ("%s")' % city_letter)

        db.commit()

    #关闭数据库连接
    cursor.close()
    db.close()

def city():
    #连接数据库
    db = pymysql.Connect(host='localhost', user='root', password='0000', database='tpp', charset='utf8')
    cursor = db.cursor()

    #获取json数据并插入数据库
    with open ('citys.json', 'r', encoding='GBK') as fp:
        #获取json文件中的字典数据
        content_dict = json.load(fp)
        #所有城市的数据
        return_value = content_dict.get('returnValue')
        #获取所有城市字母
        city_letters = return_value.keys()
        #遍历所有城市字母
        for city_letter in city_letters:

            citys = return_value.get(city_letter)

            for city in citys:
                id = city.get('id')
                parentId = city.get('parentId')
                regionName = city.get('regionName')
                cityCode = city.get('cityCode')
                pinYin = city.get('pinYin')

                #获取字母数据对应的id
                cursor.execute('select id from city_letter where letter= "%s"'% city_letter)
                res = cursor.fetchone()
                letter_id = res[0]
                #插入城市数据
                cursor.execute('insert into city(id,parentId,regionName,cityCode,pinYin,letter_id)'
                               'values(%d, %d,"%s", %d, "%s", %d)'
                               ''%(id,parentId,regionName,cityCode,pinYin,letter_id))
        db.commit()

    #关闭数据库连接
    cursor.close()
    db.close()

if __name__ == '__main__':

    city_data()
