import requests

webhook_url = "https://discord.com/api/webhooks/1409698735713419264/XnRiwOydqQbs0J3Kzo6L3poOB-90UDGZHYiOtO3099YCCCSzghMi-vKrHFdD-GPMHOKV"

data = {
    "embeds": [
        {
            "title": "a",
            "description": "you gay asf nigga",  # <-- change this
            "color": 0x00ff00
        }
    ]
}

requests.post(webhook_url, json=data)
