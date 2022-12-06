from bet_stats import db


def save_data(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def save_list_data(data):
    try:
        if data:
            for obj in data:
                db.session.add(obj)
            db.session.commit()
    except:
        db.session.rollback()
        raise


def delete_data(data):
    try:
        db.session.delete(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def flush_and_commit_changes():
    try:
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        raise
