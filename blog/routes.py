from flask import render_template, request, session, flash, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
import functools


def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get('logged_in'):
            return view_func(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return check_permissions


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('You are now logged out.', 'success')
    return redirect(url_for('index'))


@app.route("/")
def index():
    all_posts = Entry.query.filter_by(
        is_published=True).order_by(Entry.pub_date.desc())

    return render_template("homepage.html", all_posts=all_posts)


@app.route("/drafts/", methods=['GET'])
@login_required
def list_drafts():
    drafts = Entry.query.filter_by(
        is_published=False).order_by(Entry.pub_date.desc())
    return render_template("drafts.html", drafts=drafts)


@app.route("/new-post/", methods=["GET", "POST"])
@login_required
def create_entry():
    return create_or_update()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    return create_or_update(entry)


@app.route("/delete-post/<int:entry_id>", methods=["POST"])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    flash(f'Usunięto wpis o tytule "{entry.title}"')
    return redirect(url_for('index'))


def create_or_update(entry=None):
    is_create = entry is None
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if is_create:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
                db.session.commit()
                flash(f'Dodano nowy wpis o tytule "{entry.title}"')
            else:
                form.populate_obj(entry)
                db.session.commit()
                flash(f'Zapisano wpis o tytule "{entry.title}"')
        else:
            errors = form.errors
    return render_template(
        "entry_form.html", form=form, errors=errors, is_create=is_create)
