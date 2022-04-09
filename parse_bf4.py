from bs4 import BeautifulSoup
import requests

def get_elements(url):
    response = requests.get(url)
    src = response.text
    soup = BeautifulSoup(src, "lxml")
    ul_tags = soup.find_all("ul", class_="vn-list--plain vn-list vn-accordion__content")

    headers_of_goods_ikea = []
    flag = 1

    for ul_tag in ul_tags:
        a_tags = ul_tag.find_all("a")
        for a_tag in a_tags:
            next_url = a_tag.get("href")
            # print(next_url)
            
            response = requests.get(next_url)
            src = response.text

            new_soup = BeautifulSoup(src, "lxml")
            div = new_soup.find("div", class_="catalog-product-list__total-count")# .split(" ")[-1])
            if div != None:
                div = int(div.text.split(" ")[-1])
                count = div // 24
                if div % 24 > 0:
                    count += 1
                next_url += "?page=" + str(count)
            
            response = requests.get(next_url)
            src = response.text
            new_soup = BeautifulSoup(src, "lxml")
            span_tags = new_soup.find_all("span", class_="pip-header-section__title--small notranslate")
            
            for span in span_tags:
                header = span.text
                # print(header)
                parts = header.split(" / ")
                # print(parts)

                for i in parts:
                    string = i.split(" ")
                    # print(str[1])
                    name = ""
                    for j in range(len(string) // 2, len(string)):
                        name += " " + string[j]
                    # print(name)
                    if headers_of_goods_ikea.count(name[1:]) == 0:
                        headers_of_goods_ikea.append(name[1:])
                        # print(headers_of_goods_ikea)
    
    headers_of_goods_ikea.sort()
    # print(headers_of_goods_ikea)
    # print(headers_of_goods_ikea.sort())
    return headers_of_goods_ikea


start_url = "https://www.ikea.com/ru/ru/cat/tovary-products/"
names = get_elements(start_url)
# print(type(names))


file = open("Names_of_ikea.txt", "w", encoding="utf-8")
for i in range(1, len(names) - 1):
    if ord(names[i][0]) >= ord("А") and ord(names[i][0]) <= ord("Я"):
        file.write(names[i] + "\n")
file.write(names[len(names) - 1])
file.close()