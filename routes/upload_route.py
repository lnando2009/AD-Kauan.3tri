from flask import Blueprint
from controllers.upload_controller import UploadsController

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload', method=['POST'])
def upload_file():
    return UploadsController.upload_file()