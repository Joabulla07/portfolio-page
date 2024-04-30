from flask import Blueprint, render_template, send_file, Request, request
from pytube import YouTube


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


@router.route('/project/video_downloader', methods=['GET'])
def get_video_download():
    return render_template('video_downloader.html')


@router.route('/project/video_downloader/download', methods=['GET'])
def get_url_for_video_download():
    data = request.args.get("url")

    yt = YouTube(data)
    path_file = yt.streams.get_highest_resolution().download()

    return send_file(path_file, as_attachment=True)
