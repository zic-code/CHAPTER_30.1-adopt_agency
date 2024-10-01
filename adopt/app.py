from flask import Flask,render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from model import db,connect_db, Pet
from forms import AddPetForm,EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "jisoo_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

db.init_app(app)

@app.route('/', methods=['GET'])
def home():
    pets = Pet.query.all()
    
    return render_template('home.html', pets= pets)

@app.route('/add', methods= ['GET','POST'])
def add_pets():
    form =  AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('home'))
    else:

        return render_template('add_pets.html', form = form)

@app.route('/<int:pet_id>', methods=['GET','POST'])
def show_Pet (pet_id):

    pet = Pet.query.get_or_404(pet_id)
    
    return render_template('pet_detail.html',pet= pet)


@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('home'))

    else:
        # failed; re-presensjt form for editing
        return render_template("edit.html", form=form, pet=pet)

@app.route("/<int:pet_id>/delete,methods=['POST']")
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    db.session.delete(pet)
    db.session.commit()
    flash(f"{pet.name}has been deleted.", "success")

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()