from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов.
    """

    # @property
    @staticmethod
    def get_content():
        """Метод, возвращающий html-код страницы."""
        with open("index.html", "r", encoding="utf-8") as f:
            html_file = f.read()
            return html_file

    def do_GET(self):
        """Метод для обработки входящих GET-запросов."""
        page_content = self.get_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
