import os

from flask import Flask, redirect, request, send_file, abort, flash

app = Flask(__name__)
SERVER_FOLDER = 'server'


@app.route("/", methods=['GET'])
def get_file():
    file_name = request.args.get("file")

    if not file_name:
        abort(404)
    return send_file(os.path.join(SERVER_FOLDER, file_name))


@app.route("/", methods=['POST'])
def send_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    dest_file = request.form['name']

    file.save(os.path.join(SERVER_FOLDER, dest_file))
    return {'success': True}, 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)
