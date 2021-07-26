from flask import Flask, render_template, request, make_response
import requests

app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    return render_template("index.html")    

@app.route("/ssrf")
def ssrf():
    try:
        url = request.args.get("url")
        if url:
            response = requests.get(url)
            return make_response(
                response.content,
                response.status_code)
        else:
            return make_response(
                "bad request: should has request url(query string)",
                400)
    except Exception as error:
        print(error)
        return make_response(
            f"Internal server error: {error}",
            500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)