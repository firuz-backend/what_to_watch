from datetime import datetime
from email import message
from random import randrange

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional

app = Flask(__name__, static_folder='static_dir')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'ItsPymido'
app.json.ensure_ascii = False
db = SQLAlchemy(app)


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class OpinionForm(FlaskForm):
    title = StringField(
        'Enter cinema name',
        validators=[
            DataRequired('Required field'),
            Length(1, 128, 'invalid name')
        ]
    )

    text = TextAreaField(
        'Enter your opinion about the film',
        validators=[DataRequired('Required field')]
    )

    source = URLField(
        'Please privide link - for looking more',
        validators=[Length(1, 256), Optional()]
    )

    submit = SubmitField('Add')


@app.route('/')
def index_view():
    quantity = Opinion.query.count()

    if not quantity:
        return 'В базе данных мнений о фильмах нет.'

    offset_value = randrange(quantity)
    opinion: Opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)


@app.route('/opinions/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()

    if form.validate_on_submit():
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )

        db.session.add(opinion)
        db.session.commit()

        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


if __name__ == '__main__':
    app.run()
