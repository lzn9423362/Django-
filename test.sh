your_name='qinjx'
str="Hello, I know you are \"$your_name\"! \n"
echo $str
#拼接字符串
your_name="qinjx"
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1
string="1000phone is a great site"
echo ${string:1:4}       #包头包尾
string="1000phone is a great company"
echo `expr index "$string" is`
arr1=(10 20 30 40)
echo $arr1
arr2=(
10
20
30
40
)
echo $arr2

#数组的使用
#读取数组中的元素
echo ${arr1[2]}
#如果要读取数组中的全部元素
echo ${arr2[@]}

# 取得数组元素的个数
length=${#arr1[@]}
echo $length
# 或者
length=${#arr1[*]}
echo $length
# 取得数组单个元素的长度
lengthn=${#arr1[3]}
echo $lengthn


if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi

for str in 'This is a string'
do
    echo $str
done
