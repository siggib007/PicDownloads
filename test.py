from bs4 import BeautifulSoup
import requests
import json

iTimeOut = 30
strURL = "https://mikrotik.com/product/chateau_pro_ax#fndtn-gallery"
dictHeader = {}
dictHeader["Content-Type"] = "application/json"
dictHeader["Accept"] = "application/json"
dictHeader["Cache-Control"] = "no-cache"
dictHeader["Connection"] = "keep-alive"
dictHeader["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"

WebRequest = requests.get(strURL, timeout=iTimeOut, headers=dictHeader)
print ("call resulted in status code {}".format(WebRequest.status_code))
strHTML = WebRequest.text
objSoup = BeautifulSoup(strHTML,features="html.parser")
print("Fetched URL and parsed into a beautiful Soup, response length is {}".format(len(strHTML)))
for objLink in objSoup.findAll("img"):
  #print ("{}".format(objLink))
  strImg = objLink.get("src")
  if strImg[:4] == "http":
    print("Found an image: {}".format(strImg))