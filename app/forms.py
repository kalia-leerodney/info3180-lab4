#from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired



class UploadForm(FlaskForm):
    picture = FileField('Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])