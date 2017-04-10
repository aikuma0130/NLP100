from bottle import request, response, get, post, run
from bottle import jinja2_template as template
import artistdb

@get('/')
def index():
    return template('index.tpl', artists=[])

@post('/')
def hello():
    name = request.POST.get('name', None)
    alias = request.POST.get('alias', None)
    tag = request.POST.get('tag', None)

    db = artistdb.ArtistDB('localhost')
    artists = db.search(name=name, alias=alias, tag=tag)
    return template('index.tpl', artists=artists)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
