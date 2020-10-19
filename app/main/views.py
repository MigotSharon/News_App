from flask import render_template, request
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():
    sources = get_sources()
    print(sources)
    #print(sources)
    return render_template('index.html', sources=sources)


@main.route('/article/<id>')
def source_article(id):
    source_articles = get_articles(id)
    return render_template('articles_display.html', source_articles=source_articles)







