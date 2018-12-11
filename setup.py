from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)
api = "https://api.imjad.cn/cloudmusic/"
"""
外部API引用 https://api.imjad.cn/cloudmusic.md
"""

h5_Element = "<div style=\"margin-top:20%;margin-left:35%;margin-right:35%\"><label text-align:center;>Song:{0}</label><br><label text-align:center;>Artist:{1}</label><br><label text-align:center;>Br:{2}</label><br><audio src=\"{3}\" controls=\"\" autoplay=\"\"></audio></div>"
# 辣鸡H5播放器...


@app.route('/')
def home():
    return "usage : "

@app.route("/s")
def search():
    word = request.args.get("search")
    url = api + "?type=search&s=" + word
    print(url)
    result_json = json.loads(requests.get(url).text)
    #song_name,song_id,ar,br = result_json["result"]["songs"][0]["name"],result_json["result"]["songs"][0]["id"],result_json["result"]["songs"][0]["ar"]["name"],result_json["result"]["songs"][0]["h"]["br"]
    song_name = result_json["result"]["songs"][0]["name"]
    song_id = result_json["result"]["songs"][0]["id"]
    ar = result_json["result"]["songs"][0]["ar"][0]["name"]
    br = result_json["result"]["songs"][0]["h"]["br"]
    # print(song_id)
    song_url = json.loads(requests.get(api + "?type=song&id=" + str(song_id)).text)["data"][0]["url"]
    print(song_url)
    return h5_Element.format(song_name,ar,br,song_url)

@app.route("/test")
def test():
    return r'<audio src="https://m8.music.126.net/20181211181046/461b23cd3c3d41fbc8a0d4ab5bfa6ac1/ymusic/5cd7/e95d/b6a6/ad061c9d4d0b0d14b16810691335a76a.mp3" controls="" autoplay="" style="width: 100%;"></audio>'


if __name__ == "__main__":
    requests.adapters.DEFAULT_RETRIES = 5
    app.run(host='0.0.0.0', port=5000)
