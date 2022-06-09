# coding:utf-8

import sys
import calendar
import requests
import base64
import json
import time
import uuid
import random
from datetime import datetime
from datetime import timedelta
from datetime import timezone

geo_dict = [
    'F%QDqpc',
    'F%L#VZj',
    'F%Pq-jD',
    "aL?Jp,q",
    "aL~M!6f",
    "aL:O:5-",
    "aL?,!D;",
    "aL;x^1J",
    "aL/j~j7",
    "aL;L4=%",
    "aL/j~j^",
    "aL(1)/s",
    "aL%*G5*",
    "aL)^Rd'",
    "aL;^eP3",
    "aL`BHoj",
    "aL~TP!%",
    "aL;u7u)",
    "F%A2-sv",
    "F%Or_qC",
    "F%K)2r`",
    "F%Ma4SQ"
]
url_13 = 'https://80648.activity-42.m.duiba.com.cn/seckw/v2/orderConfirm?appItemId=183234999342009&payType=3&actId=31620&vipFlag=false&Qhkey=null&strategyContent=&packId=&appSkuId=307289'
url_16 = 'https://80648.activity-42.m.duiba.com.cn/seckw/v2/orderConfirm?appItemId=176551240738479&payType=3&actId=31587&vipFlag=false&Qhkey=null&strategyContent=&packId=&appSkuId=272364'
url_19 = 'https://80648.activity-42.m.duiba.com.cn/seckw/v2/orderConfirm?appItemId=183235529916864&payType=3&actId=31588&vipFlag=false&Qhkey=null&strategyContent=&packId=&appSkuId=307292'

# 在容器里运行时时间为 UTC 时间，不是北京时间，需要进行调整
def beijing(sec, what):
    beijing_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    return beijing_time.timetuple()

SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)

def get_jwt_token():
    try:
        time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
        sign = str(uuid.uuid1()).replace("-", "")
        headers = {
            'Host': 'api.369cx.cn',
            'accept': '*/*',
            'authorization': '',
            'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
            'date': time_369,
            'cityid': '2500',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7200 NetType/WIFI DarkMode/0 BlindMode/0',
            'geo': '',
            'sign': sign,
        }
        response = requests.post('https://api.369cx.cn/v2/Auth/LoginByTemp', headers=headers)
        print(response.json()["result"]["token"])
        return str(response.json()["result"]["token"])
    except Exception as err:
        print(err)
        jwt_dict = [
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1ESXpNalE1TmpJdE5URmhaUzAwTURFM0xXSmpOREl0TTJaaU5HVTNNMkk1T0dabCIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTEyNjQ5OTIyNjciLCJqdGkiOiJiOTNiNmE2Zi04ZTEzLTRhZTQtOTMyYy1jZDhjNjdhNGU3ZDYiLCJuYmYiOjE2NDc3NTQyMTUsImV4cCI6MTgwNTUyMDYxNSwiaWF0IjoxNjQ3NzU0MjE1LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.GZ-1YIfaikow-ijfZeM7tbZcL-QYZ5c621lBlvevcE5n5VzgNtCJt93S_0iemH29tTNMH2Bjqvo5unByEdixCFlkFC_LRgPBfPXhEelGwoSu5jLrldoXGNFF8mp6tJPsPaqqglkcq1KOBu-RjMmuyDgMmFAlAoKyijbEEKhJ9Pj_9SjqRBbkKgDj8qUeSRc-TGtFaEMgGRWYZX2EHRglE_aXOrWPm-6tNffuuDn234LJysVtoTlBDMbfIz2G_cVs5usSEVD7CXyZ8ZZ9j5845nrp7Z8wdg8mCj2-Z3xasPnfvi5v5XZmOJK7ShAebfK5IgIRRS_EUk5Oxhq6COP_Xw",
            'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlpETXhZVEZpWW1ZdFlUazVOUzAwTmpjMUxUaG1NelV0TVRjNFl6aGtaamhqWWpNMyIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE4Nzk4NDY3MTkiLCJqdGkiOiIxMGFlMmFkYi0wNGFlLTQ3MmMtYjgwMC1jMjliMzQwMTc3YzMiLCJuYmYiOjE2NDcxODI4MTMsImV4cCI6MTgwNDk0OTIxMywiaWF0IjoxNjQ3MTgyODEzLCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.EULawyV_Zd1phVU1xMQXDTM9MsemJi8NBe_wQJPhZnX_Vxb80GtDl-l5LhZkULaq9YtTF6COTt7z_-qvdWYit2OUS627rjUWitXA34DPFvoTpaQDpiC9YuLF9gxI7qcwz3Uij_pM4wIRWaiTqy1CCqkoyl4gGAcV5BHKectVM1n01n30aQJt529aaSwo1AfhJDjNqUCrfbnbNo5FFq06Z_M4-xyvjK22oXh8EzGDwsc324PP1l8oZmZnpFhLnOdzbgqaE9P1uoqdENFJP7q_tDIihpRboB4XmXnvWpTqCbJAtgX8u081-dQfZm_TslsN391bYzWbdxFZBIF8LEgiQg',
            'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlptTmxNMll3WkRjdFpXWTJNaTAwT1RRNExUZ3dZbVl0T0dZMFlXWTBaVE0yTkRJeSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE2MTA5MzUyODIiLCJqdGkiOiJlNjhiNWRiZS00ZTJlLTRhM2EtOWVlNi03MDE2NzFhNDk1MGIiLCJuYmYiOjE2NDcxMzc1MDksImV4cCI6MTgwNDkwMzkwOSwiaWF0IjoxNjQ3MTM3NTA5LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.PiR8LEjkcySPEpv2nJzHY2lp-_t0SeKWOMOw-Ag_tQl_Mis03jlvV-2Y01WfU-nvMtfrzXreUDH8Da06exjSoMdZ9Amy5GsQ-VxgxZHflloB04hp-MZ1zDFZPC3PfwYZTGDk2RHBzwcq62l7RLVWfq1XR84LH6wqcNeUDvUe89VivbH3kJ0QO4CRaqjCThbDq7GF9CDsTg-ajMd6bCu3ZhE5VXfH2NcmtFE_okM8feH7bLkSIgKJMrBS2pdNSTPmTSYwi4oEDxAQiBge4IhqI9JE_KPfqB5cKaW5C_9O-9yVpj7w-ItrhhQsaMAylm7buTJeyj72nmGRk1niGGUeCA',
            'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik4yTXlPR1F4WW1JdE1tUXpOaTAwTmpZeUxXSXhNalF0TmpRM09XRXpOVFF3TmpVeSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTEyNTQ0NzQ0NjEiLCJqdGkiOiIwNjEzMjFhZC1hN2U5LTQ2OTYtODliOS03YTA3ZTg5M2IwZjUiLCJuYmYiOjE2NDc3MDAxMTcsImV4cCI6MTgwNTQ2NjUxNywiaWF0IjoxNjQ3NzAwMTE3LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.FmlJ_IsLb3CP5uJ1ycqnAlpylO8bigsS7FkV3pNqMoUvr-6886_JYjdRD-W5anaXaJpuZmoLL7Mnwg5bjk8imbO5NUzjOH9mDwDKLlqMBQxUiWK-2gkAih2S3v9LKckDl28v09j4N5tGZx9Fwiz2OuARr-6cq15VshUZRDtwFbo9FTIg9FgP4517bqnKxc7IJOneN0x4iuISgnl3KVwFYDP6za8eCHMZgcoufACpwAjr44Wnh7Oj7TC4HWhlRtdCpTN8lAv27wboCHC9KmEiU8tJHIf9oJiKEeAi18NITWgJaNIdfW9EO_G8F_sTxVZ5S-2xuaKfZjvIFd9XXmYa_Q',
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik5UbGtNbVZrTnpVdFpEVmlPUzAwWVRsa0xUazFNalV0WVdOalpHRm1aVE5qTm1aaSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE3NzU0NTQyNjMiLCJqdGkiOiI5MGEzYzRmZi0wMjliLTQ3MTctOThmMS1lZDYzNDJhY2NhNjYiLCJuYmYiOjE2NDY5ODMyMzMsImV4cCI6MTgwNDc0OTYzMywiaWF0IjoxNjQ2OTgzMjMzLCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.ngXiGrBc44VE9nWGT_2Kmm8METc-aNugaLRzf3lBtQL2mmxSVKN0eMjgmfWuISj6nphdj8dUN6oDkBss2t5fV3W0Z3lITpSr32_m0m2K5l2RlL-lrWVzTWvZci6rmIB1WcxCVzNcOeaw4oAUO8jSmXXK5rxYfml8sd-Nzc07pvOZOw8qLX0tZyedDCeVPcc7GRuJzzu4e4Bjaurtrs-lunYwrilW7ZF-lzC3RDUj5bW8x3Bk-Am2ClIw8UvrA3QQvozD8dOFD_IT_Sot0vCVCe_WB6QBbGxFdowg9AOCJ6lvzTriPhPTbZY2WnZG4Buh_2AoMo8ztz8zlflDhXBygg",
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik9HSm1NVFpqWldVdE5qTTVOeTAwWVROaUxUZzBOakl0TURObE5qWXhNVEl3TmpneSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE3MDAwNjEwMCIsImp0aSI6ImE3MmYxNTUyLWUwMzUtNDYwOC05NDcyLTZmNmIwZTYzNjA3YSIsIm5iZiI6MTY0Nzc1NjE4MiwiZXhwIjoxODA1NTIyNTgyLCJpYXQiOjE2NDc3NTYxODIsImlzcyI6IndlYi4zNjljeC5jbiIsImF1ZCI6ImFwaS53ZWIuMzY5Y3guY24ifQ.LI-b11u8AiuJldQZki1gqHqqDyp2oKIsX3KwgexatllQObNFaeO3TrLZR1Xx_AkytXayyH2RaiBUbgoPMj1uJeF3nRs4DFEH3WU2KXPYHDan466lvoodoEko7ogkukD025_LdPKmL5AVWcPa-7iEBWJNyvZW3LyFjUz3czMUFPDNr0NQDNT2IyokSiB_TefuV_9UozZbiIuKEaF8AS_rtmWPETE5AkVy84TvjSpkG3RzE0smvIotxNfFnfq_inwr_iJpUm0AsZJtfbqEoe4QgcavJJrdzZThtXqYZQr8x3k3sjkYAIrHJvPerTLPe2omVuth098180s0_FSCaAg6uA",
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IllqUmhNMlJtWVdZdE9UQTVNQzAwWkRCakxUaGpORFV0TmpobU1tTm1OVFpqWmpsayIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTc4OTg3NTEyOCIsImp0aSI6IjI2MzA1MmFjLTZhNzktNDQ0Ni1iMGNiLTgxOWRkNDI3YmNhYSIsIm5iZiI6MTY0Nzc1NjI4OSwiZXhwIjoxODA1NTIyNjg5LCJpYXQiOjE2NDc3NTYyODksImlzcyI6IndlYi4zNjljeC5jbiIsImF1ZCI6ImFwaS53ZWIuMzY5Y3guY24ifQ.Eo714MKjyq9zMja4tYlcrZ5Mye9Nv1OaVS62SnYtMWEAjsjNIRrx1d0ZqW43EZAW4WhGD-TUc4o6R88Jrj_Hk9QjQ0ryyhITuzQE3TDDOlU6Ja3en-jWQGwbUhmanrOWJxKzjVU5H2jXHg6FfOGll2ZLK85ohKiiS9JpCtQN7hNeY0XroewtmR_CuCMCJEmpapI1SbGjgUKrW0CF-Je2GK1IiG7L5RJ-o-1U2bvQ4cot5lWE2BHLxvJZbqbBVctL7aJnN-euzPQ_AtYK3Qe2YuHV8Yj0AYf4r0slW8JqwRGzZysM8W7pW5p6iCruIxEJT9mTHoXhafh_mUbmWfkghQ",
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik5EUTJNalEzWldRdFpEY3haaTAwWm1FeUxUZzFNV1V0WkRZellXRXlPVFU0WW1KbCIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTk4NzYxNTUxMSIsImp0aSI6IjEwYThiNTZmLWUwOTgtNDUwNi05ZjI2LWJiODkwM2YyZjI5YSIsIm5iZiI6MTY0Nzc1NjU3NSwiZXhwIjoxODA1NTIyOTc1LCJpYXQiOjE2NDc3NTY1NzUsImlzcyI6IndlYi4zNjljeC5jbiIsImF1ZCI6ImFwaS53ZWIuMzY5Y3guY24ifQ.LCT4bENKbn_HqbivZxQoZ0_mrekZtsLcRwzj3gWvf_NvTgTYJQN4BvZItN0Peq1niQ6GgEwuVdBdZLb6rScXDqXNqs5uWwrOgBfeaZwuA01NKRs5R19vDVWCcrJ_clxUOUjPzKH8xV75x9_48GGll1UPXqvGL6tuw7aY2ahudgmnkui8dVNKDz199XaUMaXs0d1D8MZR6lNNd3QKV8A4C_Lm3AgGWld3kbfvc3q1NlRUEGuuUScJZhDm8NQXADhYHvW5eV0VgkWi9JseczbpmiMwGrRL4gadV6o1xkg-44wfw7PhHHjQC9p989dDIR3QmE52J_WQx8OwV-87E2_6OQ",
        ]
        return random.choice(jwt_dict)

def getAuth(UserName, Password):
    try:
        time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
        sign = str(uuid.uuid1()).replace("-", "")
        headers = {
            'Host': 'api.369cx.cn',
            'accept': '*/*',
            'authorization': get_jwt_token(),
            'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
            'date': time_369,
            'cityid': '2500',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7200 NetType/WIFI DarkMode/1 BlindMode/0',
            'geo': random.choice(geo_dict),
            'sign': sign,
        }

        json_data = {
            'UserName': UserName,
            'Password': Password,
        }

        response = requests.post('https://api.369cx.cn/v2/Auth/LoginByPassword', headers=headers, json=json_data)
        rsp = response.json()
        print(rsp["result"]["token"])
        return str(rsp["result"]["token"])

    except Exception as err:
        print(err)
        pass

def getPreUrl(token):
    try:
        headers = {
            'Host': 'zzczsm.sdzhx.com.cn',
            'content-type': 'application/json',
            'accept': 'application/json',
            'authorization': 'Bearer ' + token,
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': 'zh-cn',
            'origin': 'https://jngj.369cx.cn',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7200 NetType/WIFI DarkMode/1 BlindMode/0 Webview/1',
            'referer': 'https://jngj.369cx.cn/',
            'x-access-token': token
        }
        response = requests.get('https://zzczsm.sdzhx.com.cn/duiba/api/login', headers=headers)
        print(response.json()['result'])
        return response.json()['result']
    except Exception as err:
        print(err)
        pass

def sendSeverJ(sendKey, title, content):
    api = "https://sctapi.ftqq.com/" + sendKey + ".send"
    data = {
       "text":title,
       "desp":content
    }
    req = requests.post(api, data = data)

def main(rst, sendKey, user, pwd, targetTime):
    rst += "----pre----" + '\n\r\n'
    auth = getAuth(user, pwd)
    token = str(auth).replace('Bearer ', "")

    url = getPreUrl(token)
#     print(url)
    rst += url + '\n\r\n'
    
    if (targetTime == "13:00:00") :
        rst += url_13 + '\n\r\n'
    if (targetTime == "16:00:00") :
        rst += url_16 + '\n\r\n'
    if (targetTime == "19:00:00") :
        rst += url_19 + '\n\r\n'
        
    title = u"369抢兑"
    content = rst
    sendSeverJ(sendKey, title, content)
    
def judge():
    # 协调世界时
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)
    currentdate = beijing_now.today()

    year= currentdate.year
    month = currentdate.month
    day = currentdate.day

    currentday =calendar.weekday(year,month,day)

    print("今天是周" + str(currentday + 1) + "！")
    if currentday >= 5:
        exit(0)
    if currentday < 5:
        return beijing_now

if __name__ == '__main__':

    beijing_now = judge()
    print(beijing_now, beijing_now.tzname())
    print(beijing_now.strftime('%Y-%m-%d %H:%M:%S.%f'))
    rst = beijing_now.strftime('%Y-%m-%d %H:%M:%S.%f')
    rst += '\n\r\n'

    targetTime = sys.argv[1]
    user = sys.argv[2]
    user1 = sys.argv[3]
    pwd = sys.argv[4]
    key = sys.argv[5]
    key1 = sys.argv[6]

    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M:%S")
    while True:
        tar = datetime.strptime(targetTime, "%H:%M:%S")
        now = datetime.strptime(str(beijing_now), "%H:%M:%S")
        if abs(now - tar) <= timedelta(seconds=179):
            main(rst, key, user, pwd, targetTime)
            main(rst, key1, user1, pwd, targetTime)
            break
        time.sleep(10)
        utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
        beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M:%S")
