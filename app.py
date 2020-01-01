from chalice import Chalice

app = Chalice(app_name='cedd')


@app.route('/')
def index():
    return {'hello': 'world'}

