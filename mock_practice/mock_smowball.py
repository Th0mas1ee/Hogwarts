import json
import sys

from mitmproxy import ctx, http
from mitmproxy.tools.main import mitmdump


class Counter:
    def __init__(self):
        self.num = 0
        # 用以记录股票的顺序
        self.count = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        # check_url_1 = 'https://stock.xueqiu.com/v5/stock/portfolio/stock'
        check_url_2 = 'https://stock.xueqiu.com/v5/stock/batch'
        if check_url_2 in flow.request.pretty_url: #or check_url_2 in flow.request.pretty_url:
            text = flow.response.text
            text_json = json.loads(text)
            # data = flow.response.data
            # print(f'data: {data}')
            # print(f'text type: {type(text)}')
            # print(f'text_json type: {type(text_json)}')
            # print(f'text: {text}')
            print(f'text_json: {text_json}')
            # with open('data.json', 'w', encoding='utf-8') as f:
            #     json.dump(text_json, fp=f, ensure_ascii=False)
            # count = 0
            flow.response.text = json.dumps(self.process_data(text_json))
            # with open("demo.json", encoding="utf-8") as f:
            #     data = json.load(f)
            # flow.response.text = json.dumps(data)

    def process_data(self, data):
        # print(f'before change: {data}')
        if isinstance(data, dict):
            # 遍历字典的数据
            # 当字典格式，递归value值
            for key, value in data.items():
                if key == 'name':
                    data[key] = self.change_name_by_number(data[key], self.count)
                    self.count += 1
                else:
                    data[key] = self.process_data(value)
        elif isinstance(data, list):
            # 当数据类型 为 list 的时候， 添加到结构内，并继续递归遍历，
            # 知道数据类型不为可迭代对象时
            data = [self.process_data(value) for value in data]
        else:
            data = data
        return data

    def change_name_by_number(self, name, number):
        # print('*************************************')
        # print(f'before name: {name}, {number}')
        if (number % 3) == 1:
            name *= 2
        elif (number % 3) == 2:
            name = ''
        # print(f'after name: {name}, {number}')
        # print('*************************************')
        return name


addons = [
    Counter()
]


if __name__ == '__main__':

    sys.argv = [__file__, "-s", __file__]
    #
    # 官方要求必须主线程
    mitmdump()