title = str(input())
article_content = str(input())
print(f"<h1>\n {title}\n</h1>")
print(f"<article>\n {article_content}\n</article>")
while True:
    content = str(input())
    if content == "end of comments":
        break
    print(f"<div>\n {content}\n</div>")