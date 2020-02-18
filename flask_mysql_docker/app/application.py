import csv
from flask import Flask, Response, render_template, request
from wtforms import TextField, Form, SubmitField
from wtforms.validators import DataRequired
from flask import jsonify
import mysql.connector
from mysql.connector import Error
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import sqlalchemy
import MySQLdb


app = Flask(__name__)
fa = FontAwesome(app)


db_uri = 'mysql://root:docker@localhost:3360/dockerdb'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(50), unique=False, nullable=True)
    city_ascii = db.Column(db.String(50), unique=False, nullable=True)
    lat = db.Column(db.String(20), unique=False, nullable=True)
    lng = db.Column(db.String(20), unique=False, nullable=True)
    country = db.Column(db.String(50), unique=False, nullable=True)
    iso3 = db.Column(db.String(5), unique=False, nullable=True)
    admin_name = db.Column(db.String(100), unique=False, nullable=True)
    population = db.Column(db.String(50), unique=False, nullable=True)


db.create_all()


def db_insert():
    try:

        info = csv.DictReader(open(
            "static\worldcities.csv", "r", errors='ignore'))

        for data in info:
            row = dict(data)
            city_info = City(city=row['city'], city_ascii=row["city_ascii"], lat=row["lat"], lng=row["lng"],
                             country=row["country"], iso3=row["iso3"], admin_name=row["admin_name"], population=row["population"])

            db.session.add(city_info)
            
        db.session.commit()
        print("Data from csv file inserted into database successfully")

    except Error as e:
        print("Can't insert data into database: {}".format(e))

if City.query.get(1) == None:
    db_insert()


def get_details(res):
    try:

        values = []
        for item in res:
            val = item

            result = City.query.filter_by(city=val).first()
            values.append(result)

        return values

    except Error as e:
        print(e)


def get_cities():
    try:

        results = [city_name.city for city_name in City.query.all()]

        return results

    except Error as e:
        print(e)


results = get_cities()


class GetForm(Form):
    search_box = TextField('', id='autocomplete', validators=[DataRequired()])
    search_button = SubmitField('', id='search_button')


@app.route('/place', methods=['GET'])
def place():
    return jsonify(json=results)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        res = request.get_json().get('locations')
        values = get_details(res)

        return render_template("index.html", res=values)

    return render_template("index.html")


@app.route('/locations', methods=['GET', 'POST'])
def locations():
    form = GetForm(request.form)
    if request.method == 'POST':
        res = form.search_box.data

        result = City.query.filter_by(city=res).first()
        return render_template("locations.html", form=form, res=result)

    return render_template("locations.html", form=form, res=None)


if __name__ == '__main__':
    app.run(debug=True)
