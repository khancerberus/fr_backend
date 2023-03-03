from . import home_bp


@home_bp.route('/')
def index():
    return {'parametro': 'Hola mundo'}