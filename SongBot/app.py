from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bot")
def bot():
    return render_template("bot.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")
# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()