import requests
import urllib3
urllib3.disable_warnings()


url = "https://mp.weixin.qq.com/s/sqJgd_L_SmWX9bty8rerBw"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Cookie":"ua_id=Dgze8bRpgFpWf8joAAAAALbpAylEzeph7jeekwMYAKQ=; pgv_pvi=2134864896; pgv_pvid=9824098532; mm_lang=zh_CN; pgv_info=ssid=s1072156240; tvfe_boss_uuid=a9290f958038a605; RK=1JJRSJtvWO; ptcz=83c53b2012b584359a80bdb700025d48bc5fea7e5cc4a3688877715e7a13378d; uin=o0503998088; wxuin=15298846078394; uuid=e9c1e1e24ecc926b69a865fff5c63db3; ticket=e915d8482663094246029ac7d443a89f964edad8; ticket_id=gh_a93bc920dfec; cert=a2sq0vxJjbRWOmKh2aLcKhSjEiDdTVKb; xid=6239dc243cda6da380764058e2eb6a0a; openid2ticket_orqUt55KKVdSfpF4fdMeiNIUsrWg=TmWirjAQBI5GOhVJWYtl19SOZqyxL/A7sAwdc/4wn6k=; skey=@AcZYQbYqb; rewardsn=; wxtokenkey=777"}

response = requests.get(url,headers=headers)

print(response)