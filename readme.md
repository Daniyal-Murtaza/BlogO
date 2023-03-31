# Deploy BlogO into Local Server
Following is the roadmap to deploy this project into local server:

### **Pre-Requisites:**
- Python version (3.x) where x can be anything should be installed
https://www.python.org/downloads/
- Django should be installed
https://docs.djangoproject.com/en/4.1/topics/install/
- An IDE for instance, VSCode
https://code.visualstudio.com/download

### **Steps:**
1. Clone the repo:
```
git clone <repo url> 
```

2. Create a virtual environment:
```
python -m venv env
```

3. Activate the virtual environment:
```
source env/bin/activate
```

4. Install requirements:
```
pip install -r requirements.txt
```

5. Run migrations:
```
pyton manage.py migrate
```

6. Create Superuser (For login and create your own post) otherwise Guest can just view the home page:
```
python manage.py createsuperuser
```

7. Run server:
```
python manage.py runserver
```

8. By running the command in step 7, it will give you a link (http://127.0.0.1:8000/). You can click on that to directly redirect into the website or you can just write (http://localhost:8000) in the browser.

### **Work Distribution:**
- Daniyal Murtaza: 50%
- Hammad Hussain: 50%
- We have done this homework with total coordination with each other.

### **Refernces:**
- https://getbootstrap.com/docs/5.3/getting-started/introduction/
- https://fonts.google.com/
- https://www.w3schools.com/django/django_urls.php
- Some of the aid was also taken from GPT in our project.

### **Note:**
- For a dummy user (already made super user), you can just login with following credentials:
username: daniyal
password: Daniyal52782








