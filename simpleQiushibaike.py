import re
import urllib.error
import urllib.request


# start page i
def get_page(i):
    try:
        url = 'http://www.qiushibaike.com/hot/page/' + str(i)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        Headers = {'User-Agent': user_agent}
        request = urllib.request.Request(url, headers=Headers)
        response = urllib.request.urlopen(request).read().decode('utf-8')
        pattern = re.compile('<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, response)
        return items
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)


# deal with data
def get_msg(items):
    for item in items:
        if int(item[1]) > 3000:  # print the content which the num of praise is over 3000
            print(item[0])


# begin crawl
def start(i):
    if i == 1:
        date = get_page(i)
        get_msg(date)
        start(i + 1)
    else:
        print("如需继续浏览下一页，请输入Y并按回车！")  # if u want to crawl the next page,please enter Y then enter
        temp = input()
        if temp == "Y":
            date = get_page(i)
            get_msg(date)
            start(i + 1)
        else:
            print("end！")


start(1)
