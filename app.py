from flask import Flask, request, render_template, redirect, make_response, session, flash

from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'yooooooooooooooooooooooo'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session.get('username') != None:
            print('username session', session['username'])
            return render_template('index.html', username=session['username'])
        else:
            flash('You need to login before proceeding!', 'error')
            return redirect('/login')


    elif request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return render_template('index.html', username=username)


@app.route('/grades', methods=['GET', 'POST'])
def grades():
    if request.method == 'GET':

        results   = {}
        avg_to_be = []
        avg       = 0

        for k, v in request.args.items():
            results[k] = v
            print(f'added {v} to avg_to_be')
            avg_to_be.append(int(v))

        avg = sum(avg_to_be)/len(avg_to_be)


        resp = make_response(render_template('grades.html', results=results, avg=avg))
        resp.set_cookie('avg', str(avg))

        return resp

@app.route('/login')
def Login():
    if session.get('username') == None:
        return render_template('login.html')
    else:
        flash('You\'re already logged in!', 'error')
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You\'ve successfully logged out!', 'message')
    return redirect('/login')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
   
    if request.method == 'POST':
      if form.validate() == False:
         print('Form invalid!')
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
        print('Yoooooooo')
        return 'success'
        #  return render_template('success.html')
    elif request.method == 'GET':
        print('I\'m here')
        return render_template('contact.html', form = form)


if __name__ == '__main__':
    app.debug(True)
    app.run()