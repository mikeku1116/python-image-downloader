from bs4 import BeautifulSoup
import requests
import os

input_image = input("請輸入要下載的圖片：")

response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all("img", {"class": "_2VWD4 _2zEKz"}, limit=5)

image_links = [result.get("src") for result in results]  # 取得圖片來源連結

for index, link in enumerate(image_links):

    if not os.path.exists("images"):
        os.mkdir("images")  # 建立資料夾

    img = requests.get(link)  # 下載圖片

    with open("images\\" + input_image + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)  # 寫入圖片的二進位碼
