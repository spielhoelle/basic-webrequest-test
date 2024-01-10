import requests
from bs4 import BeautifulSoup

resp = requests.get("https://tmy.io")

# if 'Heyy' in resp.text:
# 	print('Test passed')
# else:
# 	print('Test failed')




soup = BeautifulSoup(resp.text, "html.parser")

print(soup.prettify())

buttons = soup.find_all("button")
loginButton = soup.find(id="login-btn")

# BeautifulSoup + python assertion
if loginButton:
	print('Test passed')

