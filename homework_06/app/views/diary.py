from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    url_for,
    redirect,
)
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from views.forms.diary import DiaryForm
from models import db, Diary


diary_record_app = Blueprint(
    "diary_record_app",
    __name__,
    url_prefix="/diary",
)


@diary_record_app.route("/", endpoint="diary_list")
def diary_records_list():
    diary_records = Diary.query.all()
    return render_template(
        "diary/list.html",
        records=diary_records,
    )


@diary_record_app.route("/<int:record_id>/", endpoint="details")
def get_diary_record_by_id(record_id: int):
    diary_record = Diary.query.get_or_404(
        record_id,
        description=f"Record #{record_id} not found!",
    )

    return render_template(
        "diary/record.html",
        record=diary_record,
    )


@diary_record_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_product():
    form = DiaryForm()

    if request.method == "GET":
        return render_template("diary/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("diary/add.html", form=form), 400

    record_date = form.date.data
    record_title = form.title.data
    record_text = form.text.data
    diary_record = Diary(date=record_date, title=record_title, text=record_text)
    db.session.add(diary_record)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create diary record {record_title!r},"
                         f" probably such record already exists.")

    flash(f"Successfully added product {record_title}!")
    url = url_for("diary_record_app.details", record_id=diary_record.id)
    return redirect(url)
