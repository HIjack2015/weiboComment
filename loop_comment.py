import webbrowser
from time import sleep

import textrank4zh
from textrank4zh import TextRank4Keyword, TextRank4Sentence

import sinaweibopy3
from BaiJiaHaoGen import  获取一堆评论

APP_KEY = '2653025079'
APP_SECRET = 'secret'
REDIRECT_URL = 'https://www.weibo.com/'

# step 2 : get authorize url and code范德萨
client = sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
def get_weibo_list():

    client.set_access_token('your_token', expires_in=4)
    res = client.home_timeline()
    return res.statuses

def comment_weibo(weibo,):
    weibo_id=weibo.id
    weibo_text=weibo.text
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=weibo_text, lower=True, window=2)

    for comment in 获取一堆评论(get_key_word(weibo_text),weibo_text,5):
        sleep(3)
        client.comment(weibo_id,comment)

def should_comment(weibo):
    user_id_list=[5502148603]
    commented_id_list=[]
    should_comment_this_user=  weibo.user.id in user_id_list
    already_commented=weibo.id in commented_id_list
    if should_comment_this_user and not already_commented:
        return True
    else:
        return False
def get_key_word(text):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=2)
    phrases = tr4w.get_keyphrases(keywords_num=2, min_occur_num=0)
    if len(phrases)!=0:
        return phrases[0]
    keywords=""
    for item in tr4w.get_keywords(2, word_min_len=1):
        keywords+=str(item.word)

    return keywords

while True:
    sleep(10)
    weibo_list=get_weibo_list()
    for weibo in weibo_list:
        if should_comment(weibo):
            comment_weibo(weibo)






