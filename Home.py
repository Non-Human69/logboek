from day_easy_viewer import get_data_logs_json
class HTML_page_gen():
    def __init__(self):
        self.html = ""
        self.head = ""
        self.body = ""

    def add_head(self, head):

        self.head = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Web Viewer</title>
            </head>
        """
    #def for making a body that steals the data from the day_easy_viwer.py function get_data_logs_json() returns dictionary with the data
    def add_body(self, days):
        self.body = "<body>"
        self.body += "<h1>Web Viewer</h1>"
        self.body += "</body>"

    def generate_html(self):
        self.html = self.head
        self.html += self.body
        self.html += "</html>\n"

    def write_html(self, filename):
        with open(filename, "w") as file:
            file.write(self.html)

    def __str__(self):
        return self.html

def main():
    days = get_data_logs_json()
    print(f"Available days:{len(days.keys())}")

    html = HTML_page_gen()
    html.add_head("Web Viewer")
    html.add_body(days)
    html.generate_html()
    html.write_html("web_viewer.html")


if __name__ == "__main__":
    main()