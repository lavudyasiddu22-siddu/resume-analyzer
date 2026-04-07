from flask import Flask, render_template, request
from analyzer.resume import Resume
from analyzer.job import JobDescription
from analyzer.analyzer import ResumeAnalyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    matched = []
    missing = []
    error = None

    if request.method == "POST":
        print("POST RECEIVED")  # DEBUG

        file = request.files.get("resume")
        job_desc_text = request.form.get("job_desc")

        if not file or file.filename == "":
            error = "Please upload a PDF file."
            return render_template("index.html", error=error)

        resume = Resume(file)

        if resume.text == "error":
            error = "Invalid PDF file!"
            return render_template("index.html", error=error)

        job_desc = JobDescription(job_desc_text)
        analyzer = ResumeAnalyzer(resume, job_desc)

        score = analyzer.calculate_similarity()
        matched, missing = analyzer.skill_analysis()

        print("Score:", score)

        return render_template(
            "index.html",
            score=score,
            matched=matched,
            missing=missing,
            error=None
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)