import json

from flask import Flask, make_response, jsonify, Response, request, redirect

app = Flask(__name__)


@app.route("/html1")  # $routeSetup="/html1"
def html1():  # $requestHandler
    return "<h1>hello</h1>"  # $HttpResponse mimetype=text/html responseBody="<h1>hello</h1>"


@app.route("/html2")  # $routeSetup="/html2"
def html2():  # $requestHandler
    return make_response("<h1>hello</h1>")


@app.route("/html3")  # $routeSetup="/html3"
def html3():  # $requestHandler
    return app.make_response("<h1>hello</h1>")


# TODO: Create test-cases for the many ways that `make_response` can be used
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.make_response


@app.route("/html4")  # $routeSetup="/html4"
def html4():  # $requestHandler
    return Response("<h1>hello</h1>")


@app.route("/html5")  # $routeSetup="/html5"
def html5():  # $requestHandler
    return Flask.response_class("<h1>hello</h1>")


@app.route("/html6")  # $routeSetup="/html6"
def html6():  # $requestHandler
    return app.response_class("<h1>hello</h1>")


@app.route("/html7")  # $routeSetup="/html7"
def html7():  # $requestHandler
    resp = make_response()  # $HttpResponse mimetype=text/html
    resp.set_data("<h1>hello</h1>")  # $ MISSING: responseBody="<h1>hello</h1>"
    return resp  # $ SPURIOUS: HttpResponse mimetype=text/html responseBody=resp


@app.route("/jsonify")  # $routeSetup="/jsonify"
def jsonify_route():  # $requestHandler
    data = {"foo": "bar"}
    return jsonify(data)

################################################################################
# Tricky return handling
################################################################################

@app.route("/tricky-return1")  # $routeSetup="/tricky-return1"
def tricky_return1():  # $requestHandler
    return (
        "<h1>hellu</h1>"
        if "raw" in request.args
        else make_response("<h1>hello</h1>")
    )

def helper():
    if "raw" in request.args:
        return "<h1>hellu</h1>"
    else:
        return make_response("<h1>hello</h1>")  # $HttpResponse mimetype=text/html responseBody="<h1>hello</h1>"

@app.route("/tricky-return2")  # $routeSetup="/tricky-return2"
def tricky_return2():  # $requestHandler
    return helper()


################################################################################
# Setting content-type manually
################################################################################


@app.route("/content-type/response-modification1")  # $routeSetup="/content-type/response-modification1"
def response_modification1():  # $requestHandler
    resp = make_response("<h1>hello</h1>")  # $HttpResponse mimetype=text/html responseBody="<h1>hello</h1>"
    resp.content_type = "text/plain"  # $ MISSING: HttpResponse mimetype=text/plain
    return resp  # $ SPURIOUS: HttpResponse mimetype=text/html responseBody=resp


@app.route("/content-type/response-modification2")  # $routeSetup="/content-type/response-modification2"
def response_modification2():  # $requestHandler
    resp = make_response("<h1>hello</h1>")  # $HttpResponse mimetype=text/html responseBody="<h1>hello</h1>"
    resp.headers["content-type"] = "text/plain"  # $ MISSING: HttpResponse mimetype=text/plain
    return resp  # $ SPURIOUS: HttpResponse mimetype=text/html responseBody=resp


# Exploration of mimetype/content_type/headers arguments to `app.response_class` -- things can get tricky
# see https://werkzeug.palletsprojects.com/en/1.0.x/wrappers/#werkzeug.wrappers.Response


@app.route("/content-type/Response1")  # $routeSetup="/content-type/Response1"
def Response1():  # $requestHandler
    return Response("<h1>hello</h1>", mimetype="text/plain")


@app.route("/content-type/Response2")  # $routeSetup="/content-type/Response2"
def Response2():  # $requestHandler
    return Response("<h1>hello</h1>", content_type="text/plain; charset=utf-8")


@app.route("/content-type/Response3")  # $routeSetup="/content-type/Response3"
def Response3():  # $requestHandler
    return Response(
        "<h1>hello</h1>",
        content_type="text/plain; charset=utf-8",
        mimetype="text/html",
    )


@app.route("/content-type/Response4")  # $routeSetup="/content-type/Response4"
def Response4():  # $requestHandler
    return Response("<h1>hello</h1>", headers={"Content-TYPE": "text/plain"})


@app.route("/content-type/Response5")  # $routeSetup="/content-type/Response5"
def Response5():  # $requestHandler
    return Response(
        "<h1>hello</h1>",
        headers={"Content-TYPE": "text/html"},
        content_type="text/plain; charset=utf-8",
    )


@app.route("/content-type/Response6")  # $routeSetup="/content-type/Response6"
def Response6():  # $requestHandler
    return Response(
        "<h1>hello</h1>",
        headers={"Content-TYPE": "text/html"},
        mimetype="text/plain",
    )


@app.route("/content-type/Flask-response-class")  # $routeSetup="/content-type/Flask-response-class"
def Flask_response_class():  # $requestHandler
    return Flask.response_class("<h1>hello</h1>", mimetype="text/plain")


@app.route("/content-type/app-response-class")  # $routeSetup="/content-type/app-response-class"
def app_response_class():  # $requestHandler
    return app.response_class("<h1>hello</h1>", mimetype="text/plain")


# TODO: add tests for setting status code
# TODO: add test that manually creates a redirect by setting status code and suitable header.

################################################################################
# Redirect
################################################################################


@app.route("/redirect-simple")  # $routeSetup="/redirect-simple"
def redirect_simple():  # $requestHandler
    next = request.args['next']
    return redirect(next)


################################################################################
# Cookies
################################################################################

@app.route("/setting_cookie")  # $routeSetup="/setting_cookie"
def setting_cookie():  # $requestHandler
    resp = make_response() # $ HttpResponse mimetype=text/html
    resp.set_cookie("key", "value") # $ CookieWrite CookieName="key" CookieValue="value"
    resp.set_cookie(key="key", value="value") # $ CookieWrite CookieName="key" CookieValue="value"
    resp.headers.add("Set-Cookie", "key2=value2") # $ MISSING: CookieWrite CookieRawHeader="key2=value2"
    resp.delete_cookie("key3") # $ CookieWrite CookieName="key3"
    resp.delete_cookie(key="key3") # $ CookieWrite CookieName="key3"
    return resp  # $ SPURIOUS: HttpResponse mimetype=text/html responseBody=resp

################################################################################


if __name__ == "__main__":
    app.run(debug=True)
