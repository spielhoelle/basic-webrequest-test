import requests

resp = requests.get("http://127.0.0.1:3000/")
# print("HTML RES:")
# print(resp.text)
# print("")
# if 'Heyy' in resp.text:
# 	print('Test passed')
# else:
# 	print('Test failed')


from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "html.parser")

buttons = soup.find_all("button")

print(len(buttons))
print(buttons)
