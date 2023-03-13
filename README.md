**SHOPPING LIST**

- A Shopping List application

User's Goal

- User wants to have a shopping list on their phone, accessible by login to their account.  The user wants to create a shopping list, add items to the list, edit items, add comments, mark items as urgent or as done, and delete items from their shopping list.
- User wants response messages to their actions, sucessful or unsuccessful.

Add an image of the finished site here. I like to use amiresponsive to get an image of my site on all device sizes, and amiresponsive allows you to click links on the page and scroll, so each device can show a different element of your site.

Link to the live site [here](https://mym-shopping-list.herokuapp.com/).

If you want to add optional shields.io badges to your README, I like to add them to this section.

**CONTENTS**

User Experience

Strategy

Our user is looking for a efficient convenient means of maintaining a shopping list, having it to hand when shopping, and sharing it with household members. Branding should be clean, uncluttered, without distraction, but not sparse.  The features are created with user ease of use in mind.

Scope

A simple, uncomplicated, uncluttered shopping list is the MVP for the present. Features are: Login, Create, Add, Update and Delete items on the list.  The six-week deadline is tight.  MVP is priority.

Structure

User will only have access to features and functionality following registration and login and has restricted shopping list view until successful login.  Registration and Login links are on the Nav bar and also on a reminder text paragraph underneath the restricted shopping list.  Successful login expands Home page view and returns an authenticated view of Shopping list, with add, edit, star, filter and delete features.  Logout feature is automatic following successful login and appears on Nav bar.  Logout returns the user to restricted list view.

Skeleton

Visual iconography for ease of use, repeated on each page in the same location where appropriate.  A user will be familiar with clicking on icons to perform an action, this app will conform with this convention.  Uncluttered, simple UI. Use of wireframes to confirm the important information is seen first and to ensure labels, navigation and arrangement will make sense to the user.

Surface

Colours will be crisp, clean, sophisticated.  Black on white, cool clean colour palette.  White background #ffffff, dark grey text #4b4f58, list container colour rgba (240, 251, 247, 1) or #f3f4f6.  Fonts will follow the clean, uncluttered scope with Roboto, Caveat Semi-bold 600, Nanum Myeongjo Regular 400 in combination look sleak and are easy to read on all devices.

- The User's interaction with this application should be easy and natural.  Use of icons will make actions like add, edit and delete intuitive. Efficient use of response messages will confirm successful actions to the user, with unsuccessful action messages easy to understand.

User Stories

| Features/Functionality                                                      | Problem Statement                                                                   | User Story                                                                                                      |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
|                                                                             | How do I develop a List application that provides all this functionality to a user? | As a (role) I can (capability) so that (received benefit).                                                      |
|                                                                             |                                                                                     |                                                                                                                 |
| REGISTRATION - Authorisation/Authentication - Epic                          |                                                                                     |                                                                                                                 |
|                                                                             |                                                                                     |                                                                                                                 |
| Registration                                                                |                                                                                     | As a new user I can register to the List App so that I can access all the application's functionality securely. |
| Login                                                                       |                                                                                     | As a registered user I can Login with username and password.                                                    |
| Logout                                                                      |                                                                                     | As a logged-in user I can Logout of the app when finished using the list.                                       |
|                                                                             |                                                                                     |                                                                                                                 |
| CRUD                                                                        |                                                                                     |                                                                                                                 |
| Read                                                                        |                                                                                     | As an unregistered user, I can only see the updated list on the Home page.                                      |
| Add Item to List                                                            |                                                                                     | As a logged in user I can click Add so that I can add an item to my List                                        |
| Edit existing Item on List                                                  |                                                                                     | As a logged in user I can click Edit so that I can edit the detail of an item on my List                        |
| Toggle/Tick list item as complete                                           |                                                                                     | As a logged in user I can tick the checkbox of an item so that I can mark the item as done.                     |
| Delete list item                                                            |                                                                                     | As a logged in user I can delete an item so that I can remove it from the list.                                 |
| Mark an item on the List as urgent                                          |                                                                                     | As a logged in user I can tick a star icon so that the item is marked Urgent.                                   |
|                                                                             |                                                                                     |                                                                                                                 |
| COMMENTING                                                                  |                                                                                     |                                                                                                                 |
| Add a comment to an item, re bulb wattage, specific shop, size of item etc. |                                                                                     | As a logged in user I can add a comment to an item so that that item has more detail                            |
|                                                                             |                                                                                     |                                                                                                                 |
| FILTERING                                                                   |                                                                                     |                                                                                                                 |
| Filter view                                                                 |                                                                                     | As a logged in user I can filter my shopping list by category so that I know where to shop.                     |

**Design**

Colour Scheme
Typography
Imagery
Wireframes
Features

General Features on Each Page
Future Implementations
Accessibility
Technologies Used

##TECHNOLOGIES

Languages Used
Frameworks, Libraries & Programs Used
Deployment & Local Development

##DEPLOYMENT
Local Development
How to Fork
How to Clone

Testing

Credits

Code Used
Content
Media
Acknowledgments
User Experience (UX)
👩🏻‍💻 View an example of a completed user experience section here

User Stories
Add your user stories here. You want to include first time visitors and returning visitors here as a minimum. Think about each group, and the experience and journey you want them to have on your site. It really helps to think about this before you start coding, and will really help with creating your wireframes.

Design

I began my design of the database structure by creating an Entity Relationship Diagram, which can be viewed [here](assets/images/Shopping List ERD.png).  The Diagram helped me to consider what to include in each Model and the relationships between the models of the database.
 
👩🏻‍💻 View an example of a completed design section here

Colour Scheme
Add all information about your colour scheme for your site here. You can explain why you choose the colours you did?

I like to include a palette of the colour scheme here, my favourite site for creating a colour palette is coolors, but there are lots of other sites that also do the same thing, like ColorSpace, Muzli Colors, Adobe Colour Wheel and Canva to name a few.

Typography

Google Fonts was used for the following fonts:

Roboto is used as a traditional, backup font.

Nanum Myeongjo is used for the header text on the site, Regular 400 weight. It is a sans-serif font.

Caveat font is used for the shopping list items, SemiBold 600 weight. It is a cursive font and suits a traditional handwritten shopping list style.

If you've imported fonts to use in your project, add some information about them here. You can include information like:

Why did you choose the font you have? Is this an accessibly friendly font? What weights have you included?

I also like to include an image of the fonts chosen as a reference.

Google Fonts is a popular choice for importing fonts to use in your project, as it doesn't require you to download the fonts to use them.

Imagery
Use this section to explain what sort of imagery you plan to use through your site.

##Wireframes

I created my wireframes using Balsamiq, a link to my file is [here]()
###Early UX Design Wireframe images

[Restricted Homepage](assets/images/wireframes/Authentication-restricted-homepage-wireframe.png)

User Registration [form](assets/images/wireframes/Registration-form-wireframe.png)

Registered user Login [form](assets/images/wireframes/Login-form-wireframe.png)

User Authentication Confirmed [Homepage expanded view](assets/images/wireframes/Authentication-confirmed-homepage-wireframe.png), with additional user functionality

There are lots of different options to create your wireframes - Code Institute students can access Balsamiq as part of the course.

Some other options include Figma, AdobeXD, Sketch and Mockup to name just a few! Or you can even go old school and get those wireframes completed using pen and paper. Just snap an image of the completed wireframes to add the images to the README.

Features
👩🏻‍💻 View an example of a completed user experience section here

This section can be used to explain what pages your site is made up of.

General features on each page
If there is a feature that appears on all pages of your site, include it here. Examples of what to include would the the navigation, a footer and a favicon.

I then like to add a screenshot of each page of the site here, i use amiresponsive which allows me to grab an image of the site as it would be displayed on mobile, tablet and desktop, this helps to show the responsiveness of the site.

Future Implementations
What features would you like to implement in the future on your site? Would you like to add more pages, or create login functionality? Add these plans here.

Accessibility
Be an amazing developer and get used to thinking about accessibility in all of your projects!

This is the place to make a note of anything you have done with accessibility in mind. Some examples include:

Have you used icons and added aria-labels to enable screen readers to understand these? Have you ensured your site meets the minimum contrast requirements? Have you chosen fonts that are dyslexia/accessible friendly?

Code Institute have an amazing channel for all things accessibility (a11y-accessibility) I would highly recommend joining this channel as it contains a wealth of information about accessibility and what we can do as developers to be more inclusive.

###Technologies Used

👩🏻‍💻 View an example of a completed Technologies Used section here

###Languages Used

Languages in this project were Python, HTML, CSS and JavaScript.

###Frameworks, Libraries & Programs Used

Django framework and Bootstrap CSS were both used in this project.


GitHub;
Balsamiq - Version: 4.5.5 - Editor Version: 5.3.1
Smartdraw - ERD 2 Template.

(add the version used).

A great tip for this section is to include them as you use them, that way you won't forget what you ended up using when you get to the end of your project.

##Deployment

The site is deployed using Heroku - [MYM Shopping List](https://mym-shopping-list.herokuapp.com/)

###To Deploy the site using Heroku:

- Login (or signup) to Heroku;
- From the dashboard, click on 'New' and select 'Create New App';
- Populate the App Name field with your new Project or Application name, and select your local region ie. Europe. Click 'Create App' button.

The app is now created and is listed in the Heroku dashboard.

In the 'Settings' tab, add the Config Variables:

- DATABASE_URL: 'Paste ElephantSQL URL';
- SECRET_KEY: 'Paste in your secret key';
- PORT: 8000;
- CLOUDINARY_URL: Cloudinary://*.

In the 'Deploy' tab:
- Select 'GitHub' from the Deployment method section;
- Connect to the GitHub repository for this project;
- Select 'Enable Automatic Deploys' from the the Automatic Deploy section.

###Create a new database on ElephantSQL

Heroku uses an ephemeral file system - which means it is wiped clean every time Heroku updates, or every time the app is redeployed.

So Gunicorn which will act as the web server for the project, and the project will also use a server-based database called 'Postgres'.  It will be seperated from the  application, so it will survive even if the application server is destroyed.

###To Create the Postgres database:

- Login or signup to ElephantSQL;
- Click 'Create New Instance';
- Populate the 'Name' field with the name of the Project or Application;
- Leave the 'Plan' field with the pre-populated Tiny Turtle content;
- Leave the 'Tags' field blank;
- Click the 'Select Region' button and choose 'EU-West-1' as the local region;
- Click the 'Review' button, ensure all the content is correct, with the correct spelling, then click 'Create Instance'.

The Postgres database is now created on ElephantSQL and you can see it on your ElephantSQL dashboard. 

###Connect Gitpod development environment to Postgres database

Through Gitpod, connect ElephantSQL through settings.py with a variable named 'DATABASE_URL', and then migrate the database structure to the newly connected ElephantSQL database.

Test the connection in ElephantSQL:

- Select the database instance from the dashboard;
- Select 'Browser' tab, then click on 'Table Queries'.

You should see that the dropped down list has been populated from the Django migrations.

###Create Procfile in Gitpod

Heroku needs a Profile so it knows how to run a project.

In the newly created Procfile, add the line 'web: gunicorn PROJECTNAME.wsgi'.
 - 'web:' tells Heroku that this is a process that should accept http traffic;
 - 'gunicorn' is a web server installed for the project, a web services gateway server;
 - '.wsgi' stands for 'web services gateway server' and is the standard that allows Python services to integrate with web servers.

 The Project is now deployed.

How to Fork
Place instructions on how to fork your project here.

How to Clone
Place instructions on how to clone your project here.

Testing
Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.

Testing is documented in TESTING.md file [here](TESTING.md)

##Credits

README.md - I used the [README.md example](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) by Kera Kudmore to plan and layout my headings and content, to ensure I didn't omit any important content.

On the CI Slack Community I saw a reference to [this YouTube video](https://www.youtube.com/watch?v=RwWhQTSV44Q) on building a CRUD Application using Class-based views, which helped supplement the learning from the FST Django Module from this course, in particular using CreateView to add an item to the database, and the reference to Django Widget Tweaks to collect the fields from the database and render form input elements in a html file if necessary.

- On further research about [Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) and looking at the [following YouTube video](https://www.google.com/search?q=django+widget-tweaks+vs+crispy-forms&rlz=1C1ONGR_enIE1019IE1019&sxsrf=AJOqlzWoraYzLPN2lHNHFLqvsMPTx369yA%3A1678736692259&ei=NH0PZMmbD9CGgQbl2pzgAg&oq=is+django+widget+tweaks+the+same+as+crispy&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgEMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADSgQIQRgAUABYAGDDFmgBcAF4AIABAIgBAJIBAJgBAMgBCMABAQ&sclient=gws-wiz-serp#fpstate=ive&vld=cid:b254270b,vid:ynToND_xOAM), it appears to be the most Pythonic way to create forms for my project.

Reverse_lazy tool was referenced in [this YouTube video](https://www.youtube.com/watch?v=RwWhQTSV44Q) which is a tool I imported from django.urls and used in my Create function to return the user to the home page upon successfully adding a new item to the shopping list.

The Credits section is where you can credit all the people and sources you used throughout your project.

Code Used
If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

Content
Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

 Media
If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.

 Acknowledgments
If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.