#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[3]:


app=Flask(__name__)


# In[4]:


from flask import request,render_template
import joblib
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        Income = request.form.get("Income")
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        print(Income,Age,Loan) 
        model=joblib.load("Creditcards")
        pred=model.predict([[float(Income),float(Age),float(Loan)]])
        print(pred)
        s="The predicted default score is:"+str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__=="__main__":
    app.run()
    


# In[ ]:




