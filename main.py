import numpy as np
from PIL import Image
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


def top_color(file_path):
    image = Image.open(file_path)
    image_data = np.array(image)
    flatten = image_data.reshape(-1, 3)
    unique_colors, counts = np.unique(flatten, axis=0, return_counts=True)
    sorted_indices = np.argsort(-counts)
    sorted_colors = unique_colors[sorted_indices]
    return sorted_colors[:100]


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['POST', 'GET'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = f.filename
        file_path = os.path.join(app.static_folder, 'photos', filename)
        f.save(file_path)

        colors = top_color(file_path)
        colors = [tuple(row) for row in colors]
        colors = [(int(r), int(g), int(b)) for r, g, b in colors]

        return render_template("home.html", form=form, color=True, colors=colors, file=filename)

    return render_template("home.html", form=form, color=False)


if __name__ == "__main__":
    os.makedirs(os.path.join(app.static_folder, 'photos'), exist_ok=True)
    app.run(debug=True)
