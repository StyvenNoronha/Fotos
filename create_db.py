from core import db, app
from core.models import Usuario, Fotos
with app.app_context():
    db.create_all()