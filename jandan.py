#! usr/bin/env python
# coding:utf-8

import base64
import requests
import re
import os
from multiprocessing import Pool
import random
import time
import multiprocessing


def get_page_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        print(e)


def get_real_img(html):
    pattern = re.compile('<span class="img-hash">(.*?)</span>')
    imgs_hash = re.findall(pattern, html)
    for img_hash in imgs_hash:
        yield base64_decode(img_hash)


def base64_decode(img_hash):
    img_hash = base64.b64decode(img_hash)
    return img_hash


def get_img_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_img(url, response.content)
        return None
    except Exception as e:
        print(e)


def save_img(url, content):
    root = 'E://jandan/'
    path = root + url.split('/')[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            print('Save successful', url)


def main(i):
    start_url = 'http://jandan.net/ooxx/page-{}#comments'.format(i)
    time.sleep(random.random() * random.randint(1, 10))
    html = get_page_html(start_url)
    for result in get_real_img(html):
        url_split = result.decode('utf-8').split('/')
        real_img_url = 'http://{}/{}/{}'.format(url_split[-3], 'large', url_split[-1])
        get_img_content(real_img_url)


if __name__ == '__main__':
    # On Windows calling this function is necessary
    multiprocessing.freeze_support()
    start_page = 1
    end_page = 47
    pool = Pool()
    pool.map(main, [i for i in range(start_page, end_page + 1)])
