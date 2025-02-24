from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def main(title):
    return render_template('content.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('content.html', prof=prof.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')