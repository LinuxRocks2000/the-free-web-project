## Add index-section to an HTML file.
import bs4


retnr = "<section id = \"index\">\n    <h2>Index</h2>"

with open("rawindex.html") as file:
    c = file.read()
    data = bs4.BeautifulSoup(c, "lxml")
    curLvl = 0
    for x in data.find_all("section"):
        pos = 0
        for i in x["id"]:
            if i == '.':
                pos += 1
        retnr += "    <a style = \"margin-left: " + str(pos * 20) + "px\" href = \"#" + x["id"] + "\">" + x["id"] + ". " + x.find("h2").contents[0] + "</a><br \>\n"
    retnr += "</section>"
    open("index.html", "w+").write(c.replace("<!AUTO_INDEX>", retnr))
print(retnr)
