from flask import Blueprint, render_template, send_file

router = Blueprint('/project', __name__)


@router.route('/project/calculator', methods=['GET'])
def get_calculator():
    return render_template('calculator.html')


@router.route('/project/exam_generator', methods=['GET'])
def get_exam_generator():
    return render_template('exam_generator.html')


@router.route('/project/exam_generator/file', methods=['GET'])
def get_excel_for_exam():
    file_path = 'static/documents/kinesiologia.xlsx'

    return send_file(file_path, download_name="fake_file.xlsx", as_attachment=True)
