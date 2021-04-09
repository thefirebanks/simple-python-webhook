from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json)
    with open("test_webhook.json", "w") as f:
        json.dump(request.json, f)
    return Response(status=200)


@app.route("/index")
def index():
    with open("test_index.json", "w") as f:
        json.dump({"bro": "dis json"}, f)
    return "Index Hello World!"


@app.route("/")
def main():
    return "Hello World!"


if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,
            use_reloader=True)  # Launch built-in web server and run this Flask webapp
