from flask import Blueprint
from app.controllers.LogoutController import logout

logout_bp = Blueprint('logout_bp', __name__)

logout_bp.route('/', methods=["GET", "POST"]) (logout)