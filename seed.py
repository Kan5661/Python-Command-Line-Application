from peewee import *
from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('notes', user='kanlin', password='12345',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Note(BaseModel):
    heading = CharField()
    note = TextField()

db.drop_tables([Note])
db.create_tables([Note])

Note(heading='sample note heading', note='sample note').save()


app = Flask(__name__)

@app.route('/note/', methods=['GET', 'POST'])
@app.route('/note/<id>', methods=['GET', 'PUT', 'DELETE'])

def note(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Note.get(note.id == id)))
        else:
            note_list = []
            for note in Note.select():
                note_list.append(model_to_dict(note))
            return jsonify(note_list)

    if request.method == 'POST':
        new_note = dict_to_model(Note, request.get_json())
        new_note.save()
        return jsonify({"success": True})
    
    if request.method == 'DELETE':
        Note.delete().where(Note.id == id).execute()
        return f"note {id} deleted"


app.run(debug=True, port=1234)