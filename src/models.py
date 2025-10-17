from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    post: Mapped["Post"] = db.relationship(back_populates="user")
    following: Mapped[int] = db.relationship(back_populates="following")
    follower: Mapped[int] = db.relationship(back_populates="follower")
    post_media: Mapped["Media"] = db.relationship(back_populates="post")
    Comment: Mapped["Comment"] = db.relationship(back_populates="user")
    # password: Mapped[str] = mapped_column(nullable=False)
    #  is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    author: Mapped["User"] = db.relationship(back_populates="post")

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Folower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    following_id:Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    following: Mapped[int] = db.relationship(back_populates="following")

    follower_id:Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    follower: Mapped[int] = db.relationship(back_populates="follower")

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(db.ForeignKey("post.id"))
    post: Mapped["Post"] = db.relationship(back_populates="media")
    type: Mapped[str] = mapped_column(String(20), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "url": self.url,
            "post_id": self.post_id,
            "type": self.type
            # do not serialize the password, its a security breach
        }

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    author_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(db.ForeignKey("post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
            # do not serialize the password, its a security breach
        }



