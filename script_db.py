from website import create_app, db
from website.models import User  # Import your models

app = create_app()

with app.app_context():
    #db.create_all()   This will create the database tables in `site.db`
    #user = User.query.all()
    #new_user = User(email='andredsouza256@gmail.com', password='Welcomegaga@238')
    #db.session.add(new_user)
    #db.session.commit()
    print(User.query.all())
