import requests

from com_do import yaml_data1


class RE_data:
    def __init__(self,str,is_url):
        self.url_a = 'https://saas-test.ycb51.cn/ybt-supply/open/api/getRSA'
        self.data_a=str
        self.requ_a= requests.get(url=self.url_a, data=f'{self.data_a}')
        self.url=is_url

    def req(self):

        c=requests.post(url="https://saas-test.ycb51.cn"+yaml_data1()[self.url],data=f'{self.requ_a.json()["res"]}')
        d=c.text
        f=c.elapsed.total_seconds()
        data_re={"text":d,"date":f}
        return data_re
