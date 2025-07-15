"""
   JWT （JSON Web Token）是目前最流行的跨域身份验证解决方案，是一种基于 Token 的认证授权机制。
    JWT 本质上就是一组字串，通过（.）切分成三个为 Base64 编码的部分。
   JWT 通常是这样的：xxxxx.yyyyy.zzzzz

   到目前为止，jwt的签名算法有三种：

    HMAC【哈希消息验证码(对称)】：HS256/HS384/HS512
    RSASSA【RSA签名算法(非对称)】（RS256/RS384/RS512）
    ECDSA【椭圆曲线数据签名算法(非对称)】（ES256/ES384/ES512）
"""
from DrissionPage import SessionPage,SessionOptions
so = SessionOptions()
jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzMzMjU1MjkwLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsIm9yaWdfaWF0IjoxNzMzMjEyMDkwfQ.eINNdcE-n08DuM_UqX6zsyoYG4UNwLqWTdLX-iih_js'
so.set_headers({'Authorization': f'jwt {jwt}'})
page = SessionPage(session_or_options=so)
# page.post('https://login3.scrape.center/api/login',data={'username':'admin','password':'admin'})
# print(page.json)
# print(page.html)
page.get('https://login3.scrape.center/api/book?limit=18&offset=0')
print(page.html)
