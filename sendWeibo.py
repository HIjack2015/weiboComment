import  requests
def share_weibo(text):
    access_token = '2.00_M93AGFBpXtC43f6ecaf3aBAOitD'
    safe_domain = 'https://weibo.com'
    url_share = 'https://api.weibo.com/2/statuses/share.json'

    payload = {
        'access_token': access_token,
        'status': text + ' ' + safe_domain
    }


    res = requests.post(url_share, data=payload)
    return res




