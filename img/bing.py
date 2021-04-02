# coding = utf8

import requests
import json

def bing_daily_wallpaper():
    fileName = 'bing.jpg'
    bingURL = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Chrome/52.0.2743.116 '
    }
    wallJson = requests.get(bingURL, headers).text
    wallURL = json.loads(wallJson)['images'][0]['url']
    wallFullURL = 'http://cn.bing.com' + wallURL
    response = requests.get(wallFullURL)
    with open(fileName, 'wb') as f:
        f.write(response.content)
        
        
if __name__ == '__main__':
    bing_daily_wallpaper()
    
