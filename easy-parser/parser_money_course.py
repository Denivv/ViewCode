import requests
from bs4 import BeautifulSoup
import time



class Currency:
	DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
	EURO_RUB = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&oq=tdhj+he%2Ckn&aqs=chrome.1.69i57j0i1i10.5863j1j7&sourceid=chrome&ie=UTF-8'
	GBP_RUB = 'https://www.google.com/search?q=gbp&sxsrf=APq-WBsepT3AC9-Ha6Vd8t76lw9htIQcAg%3A1645043282736&ei=Ul4NYoy6LMXLrgTM-qv4Cw&ved=0ahUKEwiMq4fkh4X2AhXFpYsKHUz9Cr8Q4dUDCA4&uact=5&oq=gbp&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCwgAEIAEELEDEIMBMgoIABCABBCHAhAUMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoECCMQJzoRCC4QgAQQsQMQgwEQxwEQ0QM6CAgAEAoQARBDOgkIABCABBAKEAFKBAhBGABKBAhGGABQgRFYihVglRpoAXABeACAAXKIAZkCkgEDMi4xmAEAoAEByAEIwAEB&sclient=gws-wiz'
	CNY_RUB = 'https://www.google.com/search?q=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0&sxsrf=APq-WBsZeCOPonW2tFIO1LD-JKMxPcTRWg%3A1645043445514&ei=9V4NYo-AH4T8rgT0oqT4Bg&oq=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9%D1%81&gs_lcp=Cgdnd3Mtd2l6EAMYADIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIFCAAQsQMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyCAguEIAEELEDMggIABCABBCxAzILCC4QgAQQxwEQrwE6BwgjELADECc6BwgAEEcQsAM6EgguEMcBEKMCEMgDELADEEMYADoPCC4Q1AIQyAMQsAMQQxgAOgQIIxAnOgQIABBDOgkIABCABBAKEAE6CggAEIAEEIcCEBQ6CgguEMcBEKMCEEM6CAgAEAoQARBDOgsIABCABBCxAxCDAToHCCMQ6gIQJzoLCC4QgAQQxwEQowI6DgguEIAEELEDEMcBEKMCOhEILhCABBCxAxCDARDHARCjAjoOCC4QgAQQsQMQgwEQ1AI6CgguEMcBEK8BEEM6BwgAELEDEAo6CQguEIAEEAoQAToKCAAQsQMQgwEQCjoECAAQCjoLCAAQgAQQChABECo6EAgAEIAEEAoQARAqEEYQgQI6DAguEIAEENQCEAoQAToHCAAQgAQQCjoQCAAQgAQQhwIQsQMQgwEQFDoKCC4QxwEQowIQJzoLCC4QsQMQgwEQ1AJKBAhBGABKBAhGGABQvAhYpGpg2XNoCnABeACAAWCIAYQKkgECMTaYAQCgAQGwAQrIAQvAAQHaAQQIABgI&sclient=gws-wiz'
	JPY_RUB = 'https://www.google.com/search?sxsrf=APq-WBv0m3Ol7Lbf5054iBmi6GQVg2E7kg:1645044169979&q=JPY+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&spell=1&sa=X&ved=2ahUKEwiLrJCLi4X2AhWUuosKHehnDNwQBSgAegQIARA3&biw=1920&bih=881&dpr=1'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
	current_converted_price = 0

	def __init__(self):
		self.current_converted_price = float(self.get_dollar_price().replace(",", "."))


	def get_dollar_price(self):
		full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text


	def get_euro_price(self):
		full_page = requests.get(self.EURO_RUB, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text


	def get_gbp_price(self):
		full_page = requests.get(self.GBP_RUB, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text


	def get_cny_price(self):
		full_page = requests.get(self.CNY_RUB, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text


	def get_jpy_price(self):
		full_page = requests.get(self.JPY_RUB, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text


	def check_currency(self):
		dollar = float(self.get_dollar_price().replace(",", "."))
		euro = float(self.get_euro_price().replace(",", "."))
		gbp = float(self.get_gbp_price().replace(",", "."))
		cny = float(self.get_cny_price().replace(",", "."))
		jpy = float(self.get_jpy_price().replace(",", "."))
		print(f"$ = {str(dollar)} рублей")
		print(f"€ = {str(euro)} рублей")
		print(f"£ = {str(gbp)} рублей")
		print(f"Ұ(cn) = {str(cny)} рублей")
		print(f"¥(jp) = {str(jpy)} рублей")
		time.sleep(3)
		self.check_currency()


currency = Currency()
currency.check_currency()