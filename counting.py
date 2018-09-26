import os


def print_counting(input_list):
    d = {}
    for i in input_list:
        name = os.path.basename(i)
        d[name] = d.get(name, 0) + 1

    for item in sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]:
        print('{} {}'.format(*item))


if __name__ == '__main__':
    input_list = [
        'http://www.google.com/a.txt',
        'http://www.google.com.tw/a.txt',
        'http://www.google.com/download/c.jpg',
        'http://www.google.co.jp/a.txt',
        'http://www.google.com/b.txt',
        'https://facebook.com/movie/b.txt',
        'http://yahoo.com/123/000/c.jpg',
        'http://gilacloud.com/haha.png'
    ]
    print_counting(input_list)
