from bottle import request, response, get, post, run
from bottle import jinja2_template as template
import artistdb

@get('/')
def index():
    return template('index.tpl', [])

@post('/')
def hello():
    name = request.POST.get('name')
    alias = request.POST.get('alias')
    tag = request.POST.get('tag')

    db = artistdb.ArtistDB('localhost')
    artists = db.search(name=name, alias=alias, tag=tag)
    return template('index.tpl', artists)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
