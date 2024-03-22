import requests

requests.get(
    "http://127.0.0.1:5000/increaseViews",
    headers={
        "Referer": "https://animedex.pages.dev/embed?url=https://www080.vipanicdn.net/streamhls/6799e5ffd902f036bf34ccd655f6755c/ep.11.1709061047.m3u8&episode_id=black-lagoon-the-second-barrage-dub-episode-11"
    },
)
