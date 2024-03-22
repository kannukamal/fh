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

print("Python file execution started")
generate_url("https://www.adidas.com.sg/women-shoes-new_arrivals")
print(generate_url("https://www.adidas.com.sg/women-shoes-new_arrivals"))


print("Hello World")
