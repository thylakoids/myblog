from flask import Flask, render_template


app = Flask(__name__, template_folder='./', static_folder='./')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return render_template(path + 'index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4500, threaded=True)
