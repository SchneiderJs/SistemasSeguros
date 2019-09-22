import os

from flask import Flask, redirect, request, send_file, abort, flash

app = Flask(__name__)
SERVER_FOLDER = 'server'

files = {
    "01": "file01",
    "02": "file02",
}


def get_dictionary(file_id):
    return files[file_id]


@app.route("/", methods=['GET'])
def get_file():
    file_name = request.args.get("file")

    if not file_name:
        abort(404)
    return send_file(os.path.join(SERVER_FOLDER, get_dictionary(file_name)))


@app.route("/", methods=['POST'])
def send_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    file_name = request.form['name']

    file.save(os.path.join(SERVER_FOLDER, get_dictionary(file_name)))
    return {'success': True}, 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)
