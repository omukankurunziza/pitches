from flask import render_template,request,redirect,url_for,abort
from . import main

from .forms import UpdateProfile, PitchForm, CommentsForm
from ..models import  Comment, Pitch, User 
from flask_login import login_required, current_user
from .. import db,photos







#Views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting pitch
    
    product_pitch = Pitch.query.filter_by(category = 'Product Pitch').all()
    pickup_lines = Pitch.query.filter_by(category = 'Pickup Lines').all()
    interview_pitch = Pitch.query.filter_by(category = 'Interview Pitch').all()
    promotion_pitch = Pitch.query.filter_by(category = 'Promotion Pitch').all()

   


    title = 'Home- Welcome to The best Pitching Website Online'


 

    return render_template('index.html', title = title )

@main.route('/pitch/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()    

    if pitch_form.validate_on_submit():
        pitch = Pitch(title = pitch_form.title.data, category = pitch_form.category.data, description = pitch_form.pitch_description.data)

        db.session.add(pitch)
        db.session.commit() 
        
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html', pitch_form = pitch_form)   

@main.route('/pitch/comments', methods = ['GET', 'POST'])
@login_required
def comments():    
    comments_form = CommentsForm() 
    comments = Comment.query.all()    

    if comments_form.validate_on_submit():       

        # Updated comment instance
        new_comment = Comment(description = comments_form.description.data)

        # Save review method
        new_comment.save_comment()

        return redirect(url_for('main.comments'))
    
    return render_template('comments.html', comments_form = comments_form, comments = comments)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user) 



@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

