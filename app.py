from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/aboutme')
def aboutMe():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()