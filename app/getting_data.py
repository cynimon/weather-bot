from wtforms import Form, StringField
import requests as r

request = r.post('0.0.0.0:8080')


class RegistrationForm(Form):
    userid = StringField('userid')
    username = StringField('name')


def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user = User()
        user.userid = form.userid.data
        user.username = form.username.data
        user.save()
        r.Response.('register')
    return r.render_response('register.html', form=form)
