from app import db


class TestModel(db.Model):
    __tablename__ = 'test_model'

    id = db.Column(db.Integer, primary_key=True)
    campo_test = db.Column(db.String(20), nullable=True)

    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()
