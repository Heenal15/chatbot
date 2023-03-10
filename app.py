# Credit: Followed online tutorial link: https://studygyaan.com/python/create-web-based-chatbot-in-python-django-flask
# Link to tutorial GitHub repository: https://github.com/huzaifsayed/coronabot-chatterbot/blob/master/app.py

from chat import get_response, bot_name

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))


if __name__ == "__main__":
    # app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)