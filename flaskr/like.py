from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('like', __name__)

def get_likes_for_post(post_id):
    db = get_db()
    likes = db.execute(
        "SELECT COUNT (1) FROM 'like' WHERE post_id = ?", (post_id ,)
    ).fetchone()[0]
    return likes


@login_required
@bp.route('/like/<int:id>', methods=["GET"])
def like(id):
    if request.method == "GET":
        db = get_db()
        db.execute(
            "INSERT INTO 'like' VALUES (?, ?)",
            (g.user['id'], id)
        )
        db.commit()

        return redirect(url_for("blog.post", id=id))