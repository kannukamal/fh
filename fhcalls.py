from urllib.parse import urlparse
def generate_url(url_m):
    print("PLP URL entered :", url_m)
    if "staging" not in url_m:
        hashlist = list(url_m)
        hashlist.insert(12, 'staging.')

        str2 = ''
        for ele in hashlist:
            str2 += ele

        url_m2 = str2 + '&debug=true'
        print(url_m2)
        str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?&query=" + urlparse(url_m2).path.replace('/', '', 1)

        print("URL where we can get more details related to PLP like Facets, Sortings, etc. : ", str1)
print("Python file execution started")
generate_url("https://www.adidas.com.sg/women-shoes-new_arrivals")
print(generate_url("https://www.adidas.com.sg/women-shoes-new_arrivals"))


print("Hello World")
