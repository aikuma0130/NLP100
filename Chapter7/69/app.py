from bottle import request, response, get, post, template, run

@get('/')
def helow():
    return "Hello World"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
