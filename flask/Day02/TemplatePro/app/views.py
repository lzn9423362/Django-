from flask import Blueprint, render_template

blue = Blueprint('blue',__name__)


@blue.route('/')
def index():

    return  render_template('index.html')

@blue.route('/1/')
def exts():

    return render_template('exts.html')


lis = [0, 1, 3, 4, 5, 6, 7, 9, 10, 11,12,16,17]

def two_find(x, lis, start=0, end=None):
    if end == None:
        end = len(lis) - 1
    num = (end - start) // 2 + start
    if end > start:
        if lis[num] > x:
            return two_find(x, lis, start=start, end=num)
        elif lis[num] < x:
            return two_find(x, lis, start=num + 1, end=end)
        elif lis[num] == x:
            return num
    elif lis[end] == x:
        return end
    else:
        return None

print(two_find(12, lis))

