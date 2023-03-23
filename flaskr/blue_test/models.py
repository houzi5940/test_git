from flaskr import db

class BaseModel(db.Model):
    __abstract__=True
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        session=db.session()
        session.add(self)
        session.commit()

    def update(self):
        session = db.session()
        session.commit()

    def delete(self):
        session = db.session()
        session.delete(self)
        session.commit()

class Person(BaseModel):
    username=db.Column(db.String(32))

    def __repr__(self) -> str:
        return "<Person %r>" % self.username
