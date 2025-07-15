'''
time: 2024/12/26

数据通过api接口获取
'''
from DrissionPage import SessionPage, SessionOptions
from fake_useragent import UserAgent
ua = UserAgent()
so = SessionOptions()
so.set_headers({'User-Agent': ua.random})
so.set_cookies('Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1735049062,1735050301,1735175095,1735177710; qpfccr=true; no-alert3=true; tk=5575573561269534795; sessionid=gkhbus44tz7g78g8xnduvkbwopaptyuw; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1735049062,1735050301,1735175095,1735177748; m=6a6473a3b62ffe478c854a4eb4618cf5|1735177878000; Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1735049067,1735177953; HMACCOUNT=FF4A8E605671A938; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1735177959; yuanrenxue_cookie=1735178109|07cUcLNUU7JUxsYRXPFbTEOrsF82tikNhE1otXVNqMlU44befmBuef4zkbbRFLnMJA5kN2Kle0yHRCcSa9X5hBRkJXEoNPUKkVDA95U6LlCqbGy7Obp8Uo1kTX30yMbW2mN6qiMFFx3pCeLM61oo3jIFZxL; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1735178209; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1735178389')
page = SessionPage(session_or_options=so)
page.get('https://match.yuanrenxue.cn/api/match/19?page=2')
print(page.html)
print(page.json)
