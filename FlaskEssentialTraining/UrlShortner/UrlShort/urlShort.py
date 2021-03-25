from flask import Blueprint, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
from werkzeug.utils import secure_filename


bp = Blueprint('UrlShort', __name__)


# base url
@app.route('/')
def home():
    return render_template('home.html', codes=session.keys())
    # displaying the cookies on the homepage

# about page
# name of the route and the name of the function
# dont have to match
@app.route('/yourUrl', methods=['GET', 'POST'])
def yourUrl():
    if request.method == 'POST':
        urls = {}
        if os.path.exists('urls.json'):
            # print("EXISTS")
            with open('urls.json') as urlsFile:
                urls = json.load(urlsFile)

        # print(urls)
        if request.form['code'] in urls.keys():
            flash('THAT SHORT NAME HAS BEEN USED ALREADY! PLEASE SELECT/USE ANOTHER NAME')
            return redirect(url_for('urlShort.home'))

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            fullName = request.form['code'] + secure_filename(f.filename)
            f.save(f'E:/TCS/FlaskEssentialTraining/UrlShortner/UrlShort/static/userFiles/{fullName}')
            urls[request.form['code']] = {'file': fullName}

        with open('urls.json', 'w') as urlFile:
            json.dump(urls, urlFile)    # cookie
            session[request.form.get('code')] = True
    # get request
        # request.args is for get
        # request.form is for post
        return render_template('yourUrl.html', code=request.form.get('code'))
    else:
        return redirect(url_for('urlShort.home'))


@app.route('/<string:code>')
def redirectToURL(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urlsFile:
            urls = json.load(urlsFile)

        if code in urls:
            if 'url' in urls[code]:
                return redirect(urls[code]['url'])
            else:
                return redirect(url_for('static', filename='userFiles/' + urls[code]["file"]))
    return abort(404)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/api')
def sessionApi():
    return jsonify(list(session.keys()))
