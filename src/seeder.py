 
from app import app, db
from models import Users, People, Planets, Vehicles, Favorites
from utils import APIException, generate_sitemap
with app.app_context():
    db.session.query(Favorites).delete()
    db.session.query(People).delete()
    db.session.query(Planets).delete()
    db.session.query(Vehicles).delete()
    db.session.query(Users).delete()
    db.session.commit()

with app.app_context():
    # Validate
    user = Users.query.filter_by(email="test1@example.com").first()
    if not user:
        user = Users(email="test1@example.com", password="tUpassword", is_active=True)
        db.session.add(user)
        db.session.commit()

    # Create a person
    person = People.query.filter_by(name="Luke Skywalker").first()
    if not person:
        person = People(name="Luke Skywalker", description="A Jedi Knight.", user_id=user.id)
        db.session.add(person)
        db.session.commit()

    # Create a planet
    planet = Planets.query.filter_by(name="Tatooine").first()
    if not planet:
        planet = Planets(name="Tatooine", description="A desert planet.", user_id=user.id)
        db.session.add(planet)
        db.session.commit()

    # Create a vehicle
    vehicle = Vehicles.query.filter_by(name="X-Wing").first()
    if not vehicle:
        vehicle = Vehicles(name="X-Wing", description="A starfighter.", user_id=user.id)
        db.session.add(vehicle)
        db.session.commit()

    # Create an favorite
    favorite = Favorites.query.filter_by(user_id=user.id, people_id=person.id).first()
    if not favorite:
        favorite = Favorites(user_id=user.id, people_id=person.id)
        db.session.add(favorite)
        db.session.commit()

    # print data
    print("Usuarios:", Users.query.all())
    print("Personas:", People.query.all())
    print("Planetas:", Planets.query.all())
    print("Vehículos:", Vehicles.query.all())
    print("Favoritos:", Favorites.query.all())