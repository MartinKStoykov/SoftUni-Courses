import re

file_text = str(input())
title = re.findall(r"<title>(.*?)</title>", file_text)
body = "".join(re.findall(r"<body>(.*?)</body>", file_text))
content = "".join(re.findall(r"<[^>]+>|([^<>]+)", body))
content = content.replace("\\n", "")
print("Title:", *title)
print("Content:", content)