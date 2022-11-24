#!/usr/bin/env python
# coding: utf-8

# In[30]:


from flask import Flask, render_template


# In[31]:


app = Flask(__name__,static_url_path='/static')


# In[32]:


@app.route('/')
def bot():
    return render_template('Chatbot.html')


# In[ ]:


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




