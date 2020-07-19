import webbrowser

DURL = "http://localhost:8080"

url = input("取得先URL:")
if url == "":
  url = DURL

webbrowser.open(url)
