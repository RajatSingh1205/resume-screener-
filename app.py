import os
from flask import Flask, request, render_template, jsonify
from utils.scorer import screen_resumes

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/screen", methods=["POST"])
def screen():
    job_desc = request.form.get("job_description", "").strip()
    files = request.files.getlist("resumes")

    if not job_desc:
        return jsonify({"error": "Job description is required"}), 400
    if not files or files[0].filename == "":
        return jsonify({"error": "Upload at least one resume"}), 400

    saved_paths = []
    for f in files:
        if f.filename.endswith(".pdf"):
            path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(path)
            saved_paths.append(path)

    if not saved_paths:
        return jsonify({"error": "Only PDF files are supported"}), 400

    results = screen_resumes(job_desc, saved_paths)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)