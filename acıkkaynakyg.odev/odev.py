# Personel Yönetimi
from flask import Flask, jsonify, request

app = Flask(__name__)

#Personel listemiz
personnel = []

#Personel Ekleme fonksiyonu
@app.route('/personnel', methods=['POST'])
def add_personnel():
    new_person = request.json
    personnel.append(new_person)
    return jsonify(new_person), 201

#Personelleri listeleme fonksiyonu
@app.route('/personnel', methods=['GET'])
def get_personnel():
    return jsonify(personnel), 200

#Personelleri günceleme fonksiyonu
@app.route('/personnel/<int:person_id>', methods=['PUT'])
def update_personnel(person_id):
    if 0 <= person_id < len(personnel):
        personnel[person_id] = request.json
        return jsonify(personnel[person_id]), 200
    else:
        return jsonify({"error": "Personel bulunamadı"}), 404

#Personelleri silme fonksiyonu
@app.route('/personnel/<int:person_id>', methods=['DELETE'])
def delete_personnel(person_id):
    if 0 <= person_id < len(personnel):
        deleted_person = personnel.pop(person_id)
        return jsonify(deleted_person), 200
    else:
        return jsonify({"error": "Personel bulunamadı"}), 404

if __name__ == '__main__':
    app.run(debug=True)
