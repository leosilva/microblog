from app import db
import sqlalchemy as sa


followers = sa.Table('followers',
                     db.metadata,
                     sa.Column('follower_id', db.Integer, db.ForeignKey('user.id'),
                               primary_key=True),
                     sa.Column('followed_id', db.Integer, db.ForeignKey('user.id'),
                               primary_key=True),
                    )