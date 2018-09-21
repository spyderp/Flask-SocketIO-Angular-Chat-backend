from flask import render_template
from app.errors import bp

@bp.route('/')
def main():
    return "Hello, World!"
    
@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('/error/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('/error/500.html'), 500