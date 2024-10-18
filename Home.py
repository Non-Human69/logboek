import json
from day_easy_viewer import get_data_logs_json

class HTMLPageGen:
    def __init__(self):
        self.html = ""
        self.head = ""
        self.body = ""

    def add_head(self):
        self.head = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Web Viewer</title>
</head>
        """

    def add_body(self, days, keys):
        self.body = "<body>\n"
        self.body += "<h1>Web Viewer</h1>\n"
        self.body += "<div></div>\n"
        for key in keys:
            self.body += f"<button onclick='data_get(\"{key}\")'>{key}</button>\n"
        self.body += "<div id='data'></div>\n"
        self.body += "<script>\n"
        self.body += "var days = " + json.dumps(days) + ";\n"
        self.body += """
function data_get(key) {
    var data = days[key];
    var data_div = document.getElementById('data');
    data_div.innerHTML = '';
    for (var time in data['times']) {
        var p = document.createElement('p');
        p.innerHTML = time + ' - ' + data['times'][time];
        data_div.appendChild(p);
    }
}
        """
        self.body += "</script>\n"
        self.body += "</body>\n"

    def generate_html(self):
        self.html = self.head + self.body + "</html>\n"
        print("Generated HTML")

    def write_html(self, filename):
        with open(filename, "w") as file:
            file.write(self.html)
        print(f"Written HTML to {filename}")

def main():
    days = get_data_logs_json()
    keys = days.keys()
    print(f"Available days: {len(days.keys())}")

    html_gen = HTMLPageGen()
    html_gen.add_head()
    html_gen.add_body(days, keys)
    html_gen.generate_html()
    html_gen.write_html("web_viewer.html")

if __name__ == "__main__":
    main()