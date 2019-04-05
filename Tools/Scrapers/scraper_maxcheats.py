import urllib.request
import re
import os

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }

for i in range(600, 900):
    req = urllib.request.Request('https://www.max-cheats.com/view.php?ItemID=' + str(i), None, headers)
    response = urllib.request.urlopen(req)
    page = response.read().decode('utf-8')
    response.close()

    try:
        titleIDStr = re.search(r"(Title ID:<\/b>&nbsp;[a-fA-F0-9]{16})", page).group(0)[19:].upper()
        buildIDStr = re.search(r"(Build ID:<\/b>&nbsp;[a-fA-F0-9]{16})", page).group(0)[19:].lower()
        cheats = re.findall(r"(\[.{1,40}\])<br />\r\n((([0-9A-Fa-f]{8} ?){1,3})(<br />|</td>)\r\n){1,}", page, re.MULTILINE)
    except:
        continue

    try:
        os.makedirs(f"Scrapes/MaxCheats/Cheats/{titleIDStr}/cheats/")
    except:
        pass
    file = open(f"Scrapes/MaxCheats/Cheats/{titleIDStr}/cheats/{buildIDStr}.txt", "w")

    for cheat in cheats:
        file.write(cheat[0] + "\n")
        file.write(cheat[2].replace(" ", "\n") + "\n")
    
    file.close()