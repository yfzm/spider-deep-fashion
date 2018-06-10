# -*- coding:utf-8 -*-
import os

from urllib import request

# Define constants
PAGE_NUM = 50
OFFSET_PAGE = 0

OUTPUT_PATH = "../output"
REQUEST_URL = "https://www.deepfashion.cn/v1/blog/hot"

"https://www.deepfashion.cn/v1/blog/hot?q=&pageSize=30&boundaryId=15776995&start=30&decrease=0"


class Spider:
    def __init__(self, number=PAGE_NUM, offset=OFFSET_PAGE):

        self.num = number
        self.offset = offset

        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/59.0.3071.115 Safari/537.36 "
        self.headers = {"Accept-Language": "zh-CN,zh;q=0.8", 'User-Agent': self.user_agent}

        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)
            print(u"创建目录 {}".format(OUTPUT_PATH))

        if not os.path.exists(OUTPUT_PATH + "/json"):
            os.makedirs(OUTPUT_PATH + "/json")
            print(u"创建目录 {}".format(OUTPUT_PATH + "/json"))

    @staticmethod
    def decode_url_with_params(*, q="", pageSize=30, boundaryId="", start=0, decrease=0):
        return "{}?q={}&pageSize={}&boundaryId={}&start={}&decrease={}".format(REQUEST_URL, q, str(pageSize),
                                                                               str(boundaryId), str(start),
                                                                               str(decrease))

    def get_and_save_json(self, page_index):
        url = self.decode_url_with_params(start=page_index*30)
        my_request = request.Request(url, headers=self.headers)
        response = request.urlopen(my_request)
        page_dom = response.read().decode("utf-8")
        if not page_dom:
            print("NONE")
            return None

        # print(page_dom)

        with open("{}/json/{}.json".format(OUTPUT_PATH, page_index), 'w', encoding="utf-8") as f:
            f.write(page_dom)

    def start(self):
        print(u"正在爬取数据...")

        for page_num in range(self.offset, self.offset + self.num):
            self.get_and_save_json(page_num)
            print("{}.json saved.".format(page_num))


def main():
    spider = Spider(number=100, offset=200)
    spider.start()


if __name__ == "__main__":
    main()
