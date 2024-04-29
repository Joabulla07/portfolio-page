from flask import Blueprint, render_template, send_file

router = Blueprint('/', __name__)


@router.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@router.route('/download_resume', methods=['GET'])
def get_download():
    file_path = 'static/documents/CVJoannaBulla.pdf'

    return send_file(file_path, download_name="CVJoannaBulla.pdf", as_attachment=True)
