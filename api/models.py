from . import db


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_seller = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.ForeignKey('account.id'), nullable=False, index=True)
    nama = db.Column(db.String(128), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    remaining = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(256))

    account = db.relationship('Account', primaryjoin='Product.account_id == Account.id', backref='products')


class Session(db.Model):
    __tablename__ = 'session'

    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.ForeignKey('account.id'), nullable=False, index=True)
    key = db.Column(db.String(128), nullable=False, unique=True)
    creation = db.Column(db.Float, nullable=False)
    expired = db.Column(db.Float, nullable=False)
    is_expired = db.Column(db.String(45), nullable=False)

    account = db.relationship('Account', primaryjoin='Session.account_id == Account.id', backref='sessions')
