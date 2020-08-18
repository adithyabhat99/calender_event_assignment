from app import *
from database import db_session
from models import User, Event
import datetime


@app.route("/api/event", methods=["POST"])
@token_required
def create_event(userid):
    data = request.get_json()
    if data is None or "title" not in data or "start_date" not in data or "end_date" not in data:
        return jsonify({"success": False, "message": "send title,start_date,end_date and description(optional)"}), 400
    try:
        description = None
        title = data["title"]
        start_date = datetime.datetime.strptime(
            data["start_date"], "%Y-%m-%d %H:%M:%S")
        end_date = datetime.datetime.strptime(
            data["end_date"], "%Y-%m-%d %H:%M:%S")
        if "description" in data:
            description = data["description"]
        event = Event(title, start_date, end_date, userid, description)
        db_session.add(event)
        db_session.commit()
        return jsonify({"success": True, "message": "Event created", "data": {"id": event.id, "title": event.title, "start_date": event.start_date.strftime("%Y-%m-%d %H:%M:%S"), "end_date": event.end_date.strftime("%Y-%m-%d %H:%M:%S")}}), 200
    except:
        return jsonify({"success": False, "message": "error occured"}), 500


@app.route("/api/event/<id>")
@token_required
def get_event_by_id(userid, id):
    try:
        event = Event.query.filter_by(id=id, user_id=userid).first()
        if event is not None:
            data = {}
            data["id"] = event.id
            data["title"] = event.title
            data["description"] = event.description
            data["start_date"] = event.start_date.strftime(
                "%Y-%m-%d %H:%M:%S")
            data["end_date"] = event.end_date.strftime(
                "%Y-%m-%d %H:%M:%S")
            return jsonify({"success": True, "message": "event exists", "data": data}), 200
        else:
            return jsonify({"success": False, "message": "event does not exist", "data": []}), 400
    except:
        return jsonify({"success": False, "message": "error occured"}), 500


@app.route("/api/event/<id>", methods=["DELETE"])
@token_required
def delete_event_by_id(userid, id):
    try:
        event = Event.query.filter_by(id=id, user_id=userid).first()
        if event is not None:
            db_session.delete(event)
            db_session.commit()
            return jsonify({"success": True, "message": "event deleted"}), 200
        else:
            return jsonify({"success": False, "message": "event does not exist"}), 400
    except:
        return jsonify({"success": False, "message": "error occured"}), 500


@app.route("/api/event")
@token_required
def get_events_by_user(userid):
    try:
        events = Event.query.filter_by(
            user_id=userid).order_by(Event.start_date).all()
        if events is not None:
            data = []
            for event in events:
                edata = {}
                edata["id"] = event.id
                edata["title"] = event.title
                edata["description"] = event.description
                edata["start_date"] = event.start_date.strftime(
                    "%Y-%m-%d %H:%M:%S")
                edata["end_date"] = event.end_date.strftime(
                    "%Y-%m-%d %H:%M:%S")
                data.append(edata)
            return jsonify({"success": True, "message": "events list", "data": data}), 200
        else:
            return jsonify({"success": False, "message": "0 events", "data": []}), 200
    except:
        return jsonify({"success": False, "message": "error occured"}), 500
