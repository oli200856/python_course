from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

## HTML tags
# print(soup.body.div)
# print(soup.find_all("div"))
# print(soup.find(id="first"))
# print(soup.find_all(class_="special"))
# print(soup.find_all(attrs={"data-example": "yes"}))

## CSS selectors
# print(soup.select("#first")[0])
# print(soup.select(".special"))
# print(soup.select("div"))
# print(soup.select("[data-example"))

## Accessing data
# for el in soup.select(".special"):
#     # print(el.get_text())
#     # print(el.name)
#     # print(el.attrs)
#     print(el.attrs["class"])
# print(soup.find('h3')["data-example"])

## Navigation via tags
# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.select(".super-special")[0].parent
# data = soup.select("#first")[0].find_next_sibling().find_next_sibling()
# data = soup.select("[data-example]")[1].find_previous_sibling()
# data = soup.select(".super-special")[0].find_next_sibling(class_="special")
data = soup.find("h3").find_parent()

print(data)