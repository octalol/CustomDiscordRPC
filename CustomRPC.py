from pypresence import Presence
import time

rpc= Presence("ApplicationClientID")
rpc.connect()
rpc.update(state="StateText", 
    details="DetailsText",
    large_image="ImageOrGifLink", # For images I use imgur.com and for gifs tenor.com
    small_image="ImageOrGifLink",
    buttons=[{"label": "ButtonText", "url": "URL"}, {"label": "ButtonText", "url": "URL"}], # 2 Buttons
    start=time.time()) # Timer

print("Custom Discord RPC")
print("Status: ON")
print("Made by octa")
while True:
    time.sleep(15)