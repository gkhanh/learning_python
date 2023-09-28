import requests
import time

header = {"authorization": "NDEzNjY5MTUyMDI1NDc3MTIw.GJE71E.mD6LS48acruch7fkcM6430pT7sUSPlh6v_vBAg"}

message = {"content": "Hello!"}

request = requests.post("https://discord.com/api/v9/channels/1153831762468810763/messages?limit=50", data=message,
                        headers=header)
time.sleep(10)
