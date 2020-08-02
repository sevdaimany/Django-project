# Django blog

my first django project for practicing .


## requirements
   * Python 3.8
   * Virtual Environment (virtualenv)



## Quick start
 


### To setup the project on your local machine

  #### Create Virtual Environment & Install Django

      pip install virtualenv
      pip install virtualenvwrapper
####

      cd /path/to/dev/folder
      mkdir try_django
      cd try_django
      virtualenv -p python3 djangoenv
  ####
     

* activate virtualenv in Scripts folder

 install django in virtualenv

    pip install -U django
    python  -m pip install pillow



      


   
   1.Click on ```Fork```.

   2.Go to your fork and ```Clone``` the project to your local machine

   3.activate virtualenv

   4.apply the migrations ```python manage.py migrate```

   5.Finally, run the development server ```python manage.py 
runserver```


## Publish your first blog post

  Create an admin account for first start :
    
     python manage.py createsuperuser

For example, set username 'admin' and password '123456'

Then access http://127.0.0.1:8080/admin, type the username and password 
to login :

![github-octocat](https://github.com/sevdaimany/Django-project/blob/master/djangoBlog/pictures/admin.png)



## Screen shots

 * articles list 

![github-octocat](https://github.com/sevdaimany/Django-project/blob/master/djangoBlog/pictures/articles.png)

 * article

![github-octocat](https://github.com/sevdaimany/Django-project/blob/master/djangoBlog/pictures/article.png)

 * signup

![github-octocat](https://github.com/sevdaimany/Django-project/blob/master/djangoBlog/pictures/signup.png)
