from app import app 
from models import db, Team, Player, Manager
# import the classes after db above
from faker import Faker
from random import randint
import random

faker = Faker()

sport = ["baseball", "football", "soccer", "hockey", "basketball"]

with app.app_context():
    Player.query.delete()
    Team.query.delete()
    Manager.query.delete()

    teams = []
    for i in range(15):
        new_team = Team(
            name = faker.name(),
            city = faker.city(),
            sport = random.choice(sport),
            founding_year = random.randint(1900, 2023)
        )
        teams.append(new_team)
    db.session.add_all(teams)


    players = []
    for i in range(200):
        new_player = Player(
            name = faker.name(),
            salary = random.randint(0,10000000),
            team_id = randint(1,15),
            manager_id = randint(1,75)
        )
        players.append(new_player)
    db.session.add_all(players)


    managers = []
    for i in range(75):
        new_manager = Manager(
            name = faker.name(),
        )
        managers.append(new_manager)
    db.session.add_all(managers)
    db.session.commit()

# with app.app_context():
#     print("Deleting Customers")
#     Customer.query.delete()
#     print("Deleting Products")
#     Product.query.delete()
#     print("Deleting Orders")
#     Order.query.delete()
#     print("Seeding Customers")
#     customers = []
#     for i in range(50):
#         new_cust = Customer(name=faker.name())
#         customers.append(new_cust)
#     db.session.add_all(customers)

#     print("Seeding Teachers")
#     products = []
#     for i in range(50):
#         new_product = Product(name=faker.word())
#         products.append(new_product)
#     db.session.add_all(products)

#     print("Seeding Orders")
#     orders = []
#     for i in range(50):
#         new_schedule = Order(
#             name = ""
#             )
#     db.session.add_all(orders)
#     db.session.commit()