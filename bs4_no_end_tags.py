#!/usr/bin/env python3

from bs4 import BeautifulSoup

def main():
	# also try with html.parser
	soup = BeautifulSoup("""
		<ul>
			<li>a
			<li>b
			<li>c
		</ul>
	""", 'lxml')
	print(soup.find_all('li'))

if __name__ == '__main__':
	main()
