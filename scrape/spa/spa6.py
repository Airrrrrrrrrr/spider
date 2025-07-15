import subprocess
from DrissionPage import SessionPage, SessionOptions
import fake_useragent
result = subprocess.run(['node', 'js/spa6_webpack.js'], stdout=subprocess.PIPE).stdout.decode().replace('\n', '')
so = SessionOptions()
ua = fake_useragent.UserAgent()
so.user_agent = ua.random
page = SessionPage(session_or_options=so)
base_url = f'https://spa6.scrape.center/api/movie/?limit=10&offset=0&token={result}'
page.get(base_url)
print(page.json)
