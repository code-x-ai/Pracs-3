from flask import Flask, jsonify, request
app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul Sharma", "course": "MSc IT"},
    {"id": 2, "name": "Nidhi Thakur", "course": "MSc IT"},
    {"id": 3, "name": "Amit Kumar",  "course": "MSc IT"},
]

@app.route("/students", methods=["GET"])
def get_all():
    return jsonify(students)

@app.route("/students/<int:sid>", methods=["GET"])
def get_one(sid):
    for s in students:
        if s["id"] == sid:
            return jsonify(s)
    return jsonify({"message": "Student not found"}), 404

@app.route("/students", methods=["POST"])
def add():
    # pip install flask
    d = request.get_json()
    if not d or "id" not in d or "name" not in d or "course" not in d:
        return jsonify({"message": "Bad Request: missing fields"}), 400
    students.append(d)
    return jsonify({"message": "Student added successfully", "student": d}), 201

@app.route("/students/<int:sid>", methods=["PUT"])
def update(sid):
    d = request.get_json()
    for s in students:
        if s["id"] == sid:
            s.update(d)
            return jsonify({"message": "Student updated successfully", "student": s})
    return jsonify({"message": "Student not found"}), 404

@app.route("/students/<int:sid>", methods=["DELETE"])
def delete(sid):
    global students
    students = [s for s in students if s["id"] != sid]
    return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
