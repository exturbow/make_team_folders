'''
Created on 2020/10/31

@author: turbow
'''

import requests
from bs4 import BeautifulSoup
import re
import os

#初期入力するところ
#イベントのアドレスを入力
event_url ='http://manbow.nothing.sh/event/event.cgi?action=List_def&event=133'

base_dir = "X:\\test\\"


# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get(event_url)

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.content, 'html.parser')

#team名を抽出。めんどかったので条件分岐ではなくタイトルとかをそぎ落とし（力技）
tag_items = soup.find_all('div', class_="fancy-title title-dotted-border title-center")
team_list = [t.get_text(strip=True) for t in tag_items]
team_list = team_list[2:]


#listからフォルダに使えない文字を削除
for i in range(len(team_list)):
    team_list[i]=re.sub(r'[\\/:*?"<>|]+','',team_list[i])

#フォルダ作成
for i in range(len(team_list)):
    new_dir = base_dir + team_list[i]
    os.mkdir(new_dir)

