from os import getenv

from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from views.diary import diary_record_app
from models import db

from datetime import datetime

app = Flask(__name__)
app.register_blueprint(diary_record_app, url_prefix='/diary')

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

csft = CSRFProtect(app)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.template_filter('date_format')
def date_format(value, format='%d.%m.%Y'):
    return datetime.strftime(value, format)


PAGES = {
    1: {'name': 'Main page',
        'URL': '/',
        },
    2: {
        'name': 'Diary',
        'URL': '/diary/'
        },
    3: {
        'name': 'About page',
        'URL': '/about/'
        },
}


@app.route("/", endpoint="index_page")
def main_page():
    return render_template(
        "index.html",
        pages=PAGES,
    )


@app.route("/about/", endpoint="about_page")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=False)
