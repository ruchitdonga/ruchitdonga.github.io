import urllib.request
import re

url = "https://wallpapercave.com/w/wp12803870"
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode("utf-8")

# Find the main image URL
match = re.search(r'"([^"]*wp12803870\.jpg)"', html)
if match:
    img_url = match.group(1)
    if not img_url.startswith("http"):
        img_url = "https://wallpapercave.com" + img_url
    print("Downloading:", img_url)
    
    req2 = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0", "Referer": url})
    data = urllib.request.urlopen(req2).read()
    with open(r"c:\Users\ASUS\Desktop\portfolio\static\img\cs_red_bg.jpg", "wb") as f:
        f.write(data)
    print("Success")
else:
    print("Image URL not found in HTML.")
