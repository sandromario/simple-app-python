from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
    response = make_response("Hello Tekton from Python!\n", 200)
    response.mimetype = "text/plain"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
