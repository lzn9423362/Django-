from random import randint

# import  PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#验证码
class VerifyCode:
    def __init__(self,width=100,height=60,len=4):
        """

        :param width: 验证码宽度
        :param height: 高度
        :param len: 字符个数
        """
        self.width = 100 if width < 0 else width
        self.height = 60 if height < 0 else height
        self.len = 4 if len < 0 or len > 5 else len
        self.pen = None  #画笔
        self.__code = None  #验证码字符串

    @property
    def code(self):
        return self.__code

    def generate_code(self):
        """
        生成验证码
        :return:
        """
        #1.生成画布
        im = Image.new("RGB",(self.width,self.height),self.__rand_color(160,250))

        #2.生成画笔
        self.pen = ImageDraw.Draw(im)

        #3.生成验证码字符串
        self.__code = self.__rand_string()

        #4.画验证码
        self.__draw_code()
        self.__draw_line()

        #5.画干扰项
        self.__disturb_point()

        #6.保存图片
        im.show()
        im.save('vc.png','PNG')
    def __draw_line(self):
        for i in range(5):
            x1 = randint(1,self.width-1)
            x2 = randint(1,self.width-1)
            y1 = randint(1,self.height-1)
            y2 = randint(1,self.height-1)
            self.pen.line([(x1,y1),(x2,y2)],fill=self.__rand_color(120,160))
    def __disturb_point(self):
        for i in range(500):
            x = randint(1,self.width-1)
            y = randint(1,self.height-1)
            self.pen.point([(x,y)],fill=self.__rand_color(120,160))
    def __rand_color(self,low,hight):
        """
        随机颜色
        :param low:
        :param hight:
        :return:
        """
        return randint(low,hight),randint(low,hight),randint(low,hight)

    def __rand_string(self):
        """
        纯数字验证码
        :return:
        """
        string = ''
        for i in range(self.len):
            string += str(randint(0,9))
        return string

    def __draw_code(self):
        """
        画验证码字符串
        :return:
        """
        for i in range(len(self.__code)):
            x = 10 + i * (self.width - 20) / self.len  #x坐标
            y = randint(10,25)
            font = ImageFont.truetype('simhei.ttf',size=25,encoding='utf-8')
            self.pen.text((x,y),self.__code[i],self.__rand_color(0,90),font=font)
#
vc = VerifyCode()
vc.generate_code()