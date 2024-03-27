from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'kikostinky'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    '''Show home page with list of available pets'''
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    '''Display new pet form and handle form submission'''
    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {key: val for key, val in form.data.items() if key != "csrf_token"}
        new_pet = Pet(**data)
        
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)
    
@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet_details(id):
    '''Display pet details and handle pet editing'''
    
    pet = Pet.query.get_or_404(id)
    form= EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.add(pet)
        db.session.commit()
        
        return redirect(f'/{pet.id}')
    else:
        return render_template('pet_details.html', pet=pet, form=form)