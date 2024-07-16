<h1>Quick Pics API</h1>
<p>To build a social media app that allows users to create posts and follow each other.</p>

<h2>Links</h2>
<h3>Link to API on Heroku https://api-backend-project-3eba949b1615.herokuapp.com/</h3>
<h3>Link to Quick Pics frontend on Heroku https://frontend-project5-8507d8b525c6.herokuapp.com/</h3>
<h3>Link to Quick Pics frontend repository https://github.com/JoshRudge22/frontend-project5</h3>

<h2>Building API</h2>
<p>To help build my API I had help from the code institute tutors, my mentor Antonio, I watched the code institute DFI API walkthrough and used the code institute cheat sheet they provided.</p>

<h2>Agile</h2>
<p>I used the github projects to manage the app whilst using the Agile Method. I created 10 user stories both from the users side and external users side, with acceptable acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks in order to complete the user story. You can click here https://github.com/JoshRudge22/Project5-API/issues to view them.</p>

<h2>Data Model</h2>

![data model](https://github.com/user-attachments/assets/3567f333-002e-4fa2-9664-d1578e28ef4a)

<ul>
  <li>Profile App: Is where the user creates a number, they are given an Id after they have created their own username. Once this has been assigned then the user can update their information such as location , bio, full name and their own profile image</li>
  <li>Posts App: User uploads an image and creates a caption which will then have its own id. Depending on what page you would look at the post for this example the Following Feed the created_at is used to order to posts in newest first.</li>
  <li>Likes App: User can like an image when they do we use the id to add on their liked posts in the frontend. Again its ordered by the newest post the user likes.</li>
  <li>Comments App: User can comment an image when they do we use the id to add on their comment list in the frontend. Again its ordered by the newest post the user has left a comment on.</li>
  <li>Follow App: User can follow another user as we get the id of that user and add them to the following list as an example. Order by created_at for</li>
  <li>Contact App: User fills out a form so they can get in contact with the site admin or the email address in the views.py</li>
</ul>

<h2>Features</h2>
<h4>Homepage</h4>
<p>When you open the backend app you will see a message welcoming you to the app</p>

![Root Route](https://github.com/user-attachments/assets/a00e53d8-e095-4e5a-b66c-7831ed4a2e5b)

<h4>Profile</h4>

![profiles list](https://github.com/user-attachments/assets/abacebcc-f9b4-4d7b-b05b-53aadd1d79cf)

<p>Fields in the serializers are 'profile_id', 'user', 'full_name', 'bio', 'location', 'profile_image', 'created_at', 'is_owner', 'following_count', 'followers_count'</p>

![User profile view](https://github.com/user-attachments/assets/e7085a2e-d691-493a-beee-6c00658b6148)

<p>This is the result whenever you either click on a users profile or search for their name, location or username</p>

![Profiles update](https://github.com/user-attachments/assets/f097fdc1-b67f-42a3-a5e1-d4dd2b6f8caa)

<p>Here is how the user will be able to update their profile</p>

![Profiles Delete](https://github.com/user-attachments/assets/3e66c650-c546-486a-9b7b-2ae9c198adc0)

<p>This is where the user will be able to delete their profile and everything that they have ever created</p>

<h4>Posts</h4>

![feed list](https://github.com/user-attachments/assets/d996d1c8-5993-49c3-b5d3-c57a451db122)

<p>Two feeds are pretty much the same however the following feed only shows posts of users the current user is following.</p>

![posts list](https://github.com/user-attachments/assets/704f63eb-373b-486f-8211-bc9ee59224e5)

<p>The the post list will show all the posts the current user has created.</p>

<h4>Likes</h4>

![Likes List](https://github.com/user-attachments/assets/6bb74585-b2a3-4b57-96c3-3c3681568e6a)

<p>Here is how the user can view which other users have either liked their post or someone else post.</p>

<h4>Follow</h4>


![Follow Count](https://github.com/user-attachments/assets/db3cf84c-be15-495a-b658-f470c6d76f9a)

<p>I added the count to the view that updates every time any user either gets followed or unfollowed.</p>

![Followers List](https://github.com/user-attachments/assets/7c0c8a16-3e6c-4c79-b7f4-0641500296d1)

<p>Then just like the count the follow pages get updates and show the current user the usernames of the followers.</p>

<h4>Contact</h4>

![Contact Form](https://github.com/user-attachments/assets/2b3a92e2-19ca-41ba-aac8-a1252e4fe3d5)

![Contact Admin](https://github.com/user-attachments/assets/0ffd883c-52ad-450b-8b12-2797d189d3a2)

<p>Contact form once submitted then gets sent to the email address in views.py and the admin panel</p>

<h4>Comments</h4>

![Comments](https://github.com/user-attachments/assets/d759a476-9439-4581-a07a-f31f59f3d5c9)

<p>Here is the list that the user will see both on a post that has comments on it and the comments list page in the frontend.</p>

<h2>Deployment</h2>
<h4>The project was deployed to Heroku. To deploy, please follow the process below:</h4>

<ul>
  <li>To begin with we need to create a GitHub repository from the Code Institute template by following the link and then click 'Use this template'.</li>
  <li>Fill in the details for the new repository and then click 'Create Repository From Template'.</li>
  <li>When the repository has been created, click on the 'Gitpod' button to open it in the GitPod Editor.</li>
  <li>Now it's time to install Django and the supporting libraries that are needed, using the following commands:</li>
  <li>pip3 install 'django<4' gunicorn, pip3 install 'dj_database_url psycopg2 and pip3 install 'dj3-cloudinary-storage</li>
  <li>When Django and the libraries are installed we need to create a requirements file.</li>
  <li>pip3 freeze --local > requirements.txt - This will create and add required libraries to requirements.txt</li>
  <li>Now it's time to create the project.
      django-admin startproject YOUR_PROJECT_NAME . - This will create the new project.</li>
  <li>When the project is created we can now create the applications. My project consists of the following apps; Profiles, Comments, Contact, Likes, Follow and Posts.</li>
  <li>python3 manage.py startapp APP_NAME - This will create an application</li>
  <li>We now need to add the applications to settings.py in the INSTALLED_APPS list.</li>
  <li>Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.</li>
  <li>python3 manage.py makemigrations - This will prepare the migrations, python3 manage.py migrate - This will migrate the changes, python3 manage.py runserver - This runs the server. To test it, click the open browser button that will be visible after the command is        run.</li>
  <li>Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.</li>
  <li>Once signed into your Heroku account, click on the button labelled 'New' to create a new app.</li>
  <li>Choose a unique app name, choose your region and click 'Create app".</li>
  <li>Next we need to connect an external PostgreSQL database to the app from ElephantSQL. Once logged into your ElephantSQL dashboard, you click 'Create New Instance' to create a new database. Give the database a:</li>
  <li>Name</li>
  <li>Tiny Turtle Free Plan</li>
  <li>Selected data centre near you and click 'Create Instance'. Return to your ElephantSQL Dashboard, and click into your new database instance. Copy the Database URL and head back to Heroku.</li>
  <li>Back in your Heroku app settings, click on the 'Reveal Config Vars' button. Create a config variable called DATABASE_URL and paste in the URL you copied from ElephantSQL. This connects the database into the app.</li>
  <li>Go back to GitPod and create a new env.py in the top level directory. Then add these rows.</li>
  <li>import os - This imports the os library</li>
  <li>os.environ["DATABASE_URL"] - This sets the environment variables.</li>
  <li>os.environ["SECRET_KEY"] - Here you can choose whatever secret key you want.</li>
  <li>Back in the Heroku Config Vars settings, create another variable called SECRET_KEY and copy in the same secret key as you added into the env.py file. Don't forget to add this env.py file into the .gitignore file so that it isn't commited to GitHub for other users       to find.
  </li>
  <li>Now we have to connect to our environment and settings.py file. In the settings.py, add the following code:</li>
  <li>import os, import dj_database_url, if os.path.isfile("env.py"):, import env, In the settings file, remove the insecure secret key and replace it with: SECRET_KEY = os.environ.get('SECRET_KEY')</li>
  <li>Now we need to comment out the old database settings in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).</li>
  <li>Instead, we add the link to the DATABASE_URL that we added to the environment file earlier.</li>
  <li>Save all your fields and migrate the changes again.</li>
  <li>python3 manage.py migrate</li>
  <li>Now we can set up Cloudinary (where we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.</li>
  <li>Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):</li>
  <li>os.environ["CLOUDINARY_URL"] = "cloudinary://************************"</li>
  <li>Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.</li>
  <li>Back in the settings.py file, we now need to add our Cloudinary Libraries we installed earlier to the INSTALLED_APPS list. Here it is important to get the order correct.</li>
  <li>cloudinary_storage, django.contrib.staticfiles and cloudinary</li>
  <li>For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.</li>
  <li>To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to the ALLOWED_HOSTS list:</li>
  <li>ALLOWED_HOSTS = ['frontend-project5-8507d8b525c6.herokuapp.com', 'localhost']</li>
  <li>Now we just need to create the basic file directory in Gitpod.</li>
  <li>Create a file called *Procfile and add the line web: gunicorn api.wsgi to it.</li>
  <li>Now you can save all the files and prepare for the first commit and push to Github by writing the lines below, git add ., git commit -m "Deployment Commit and git push</li>
  <li>Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.</li>
  <li>Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!</li>
  <li>The live link to the Happening API on Heroku can be found here. And the Github repository can be found here.</li>
</ul>

<h2>Cloning And Setting Up This Project</h2>
<h4>To clone and set up this project you need to follow the steps below.</h4>
<ul>
  <li>When you are in the repository, find the code tab and click it.</li>
  <li>To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.</li>
  <li>Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.</li>
  <li>Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.</li>
  <li>To be able to get the project to work you need to install the requirements. </li>
  <li>pip3 install -r requirements.txt - This command downloads and installs all required dependencies that is stated in the requirements file.</li>
  <li>The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github
    (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.</li>
  <li>python3 manage.py migrate - This will do the necessary migrations.</li>
  <li>python3 manage.py runserver - If everything i setup correctly the project is now live locally.</li>
</ul>

<h2>Credits</h2>
<ul>
  <li>Friends and Faimly for creating profile and providing feedback</li>
  <li>Code Institute Tutors</li>
  <li>Slack Community</li>
  <li>Code Institute DFI Walkthrough and Cheat Sheet</li>
  <li>Mentor Antonio</li>
  <li>Slack Community</li>
</ul>
