from urllib.parse import urlparse
import requests

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
        if "/us/" in url_m2:
            str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?" + "sitePath=us&query=" + urlparse(url_m2).path.replace('/us/', '')
        elif "/en/" in url_m2:
            str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?" + "sitePath=en&query=" + urlparse(url_m2).path.replace('/en/', '')
        elif "/th/" in url_m2:
            str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?" + "sitePath=th&query=" + urlparse(url_m2).path.replace('/th/', '')
        elif "/nl/" in url_m2:
            str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?" + "sitePath=nl&query=" + urlparse(url_m2).path.replace('/nl/', '')
        elif "/tr/" in url_m2:
            str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?" + "sitePath=tr&query=" + urlparse(url_m2).path.replace('/tr/', '')
        else:
            str1 = urlparse(url_m2).scheme + "://" + urlparse(url_m2).netloc + "/api/plp/content-engine?&query=" + urlparse(url_m2).path.replace('/', '', 1)

        print("URL where we can get more details related to PLP like Facets, Sortings, etc. : ", str1)

        print("str1 : ", str1)
        fh_url_to_be_changed = get_api_response(str1)
        print("fh_url_to_be_changed : ", fh_url_to_be_changed)
        print("-------------------------------STAGING OUTPUT------------------------------------")
        fh_preview_url_stg = fh_url_to_be_changed.replace("fredhopper/query", "preview")
        print("Fredhopper Business Manager Link with all Modifications for STG : ", fh_preview_url_stg)

        fh_preview_url_wm_stg = fh_preview_url_stg + "&fh_suppress=modifications:all"
        print("Fredhopper Business Manager Link without Modifications for STG : ", fh_preview_url_wm_stg)

        print("-------------------------------PRODUCTION OUTPUT------------------------------------------")

        fh_preview_url_prod = fh_preview_url_stg.replace(".prepublished", ".published")
        print("Fredhopper Business Manager Link with all Modifications for PROD : ", fh_preview_url_prod)

        fh_preview_url_wm_prod = fh_preview_url_wm_stg.replace(".prepublished", ".published")
        print("Fredhopper Business Manager Link without Modifications for PROD : ", fh_preview_url_wm_prod)
        print("-------------------------------------------------------------------------")
def get_api_response(api_url):
    try:
        response = requests.get(api_url, verify=False)
        response.raise_for_status()
        # Other code
    except requests.ConnectionError as e:
        print(f"Connection error occurred: {e}")
        # Handle the error gracefully
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        # Handle HTTP errors
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle other exceptions

print("Python file execution started")
generate_url("https://www.adidas.com.sg/women-shoes-new_arrivals")
print(generate_url("https://www.adidas.com.sg/women-shoes-new_arrivals"))


print("Hello World")
