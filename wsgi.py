from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()