
from flask import Flask,render_template,session,redirect,url_for,flash,request


from forms import NameForm,submit
from . import main 
bdd=[]
bod=[]

@main.route('/', methods=['GET', 'POST'])
def index():
 name=None
 form = NameForm()
 ford=submit()
 
 if form.validate_on_submit():
         name= form.name.data
         form.name.data=""
         bdd.append(name)
         return redirect(url_for('main.index'))
 if ford.boole.data==True:
            ford.boole.data=False
            re=request.form['text']
            l=0
            for idd in bdd:
                 if idd==re:
                         bod.append(re)
                         del bdd[l]
                         break
                 l=l+1      
            return redirect(url_for('main.index'))
 return render_template('a.html', form=form, name=bdd,ford=ford,bod=bod)

@main.route('/favicon.ico',methods=['GET','POST'])
def favico():
       return redirect(url_for('static',filename='favicon.ico'))

@main.route('/clearn', methods=['GET', 'POST'])
def clearn():
        
        #return redirect(url_for('static',filename='favicon.ico',_external=True))
        return redirect(url_for('main.index'))
