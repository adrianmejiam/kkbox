from flask import Flask
from app import create_app
from model import test

app = create_app("development")


@app.route('/search')
def predictInput():
    test.get_charts()
    res = {}
    n=1
    for i, item in enumerate(test.search()):
        res[i+1] = item["name"]+", " +item["url"]
    return res

@app.route("/")
def index_page():
    user = "Cat"
    return render_template("index.html", user=user)


if __name__ == '__main__':
    app.config["SECRET_KEY"] = "rc498mt6848"
    app.run(host='0.0.0.0', port=3000, debug=True)

