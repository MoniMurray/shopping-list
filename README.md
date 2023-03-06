PROJECT NAME TO GO HERE
👩🏻‍💻 View an example of this section here

Add a Blurb about the site here, what does it do, why did you build it?

Add an image of the finished site here. I like to use amiresponsive to get an image of my site on all device sizes, and amiresponsive allows you to click links on the page and scroll, so each device can show a different element of your site.

Add a link to the live site here, for Milestone 1 this will be the GitHub Pages Link from when you deployed the site.

If you want to add optional shields.io badges to your README, I like to add them to this section.

CONTENTS
User Experience

User Stories
Design

Colour Scheme
Typography
Imagery
Wireframes
Features

General Features on Each Page
Future Implementations
Accessibility
Technologies Used

Languages Used
Frameworks, Libraries & Programs Used
Deployment & Local Development

Deployment
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
👩🏻‍💻 View an example of a completed design section here

Colour Scheme
Add all information about your colour scheme for your site here. You can explain why you choose the colours you did?

I like to include a palette of the colour scheme here, my favourite site for creating a colour palette is coolors, but there are lots of other sites that also do the same thing, like ColorSpace, Muzli Colors, Adobe Colour Wheel and Canva to name a few.

Typography
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

Technologies Used
👩🏻‍💻 View an example of a completed Technologies Used section here

Languages Used
Make a note here of all the languages used in creating your project. For the first project this will most likely just be HTML & CSS.

Frameworks, Libraries & Programs Used
Add any frameworks, libraries or programs used while creating your project.

Make sure to include things like git, GitHub, the program used to make your wireframes, any programs used to compress your images, did you use a CSS framework like Bootstrap? If so add it here (add the version used).

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

Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file here

##Credits

README.md - I used the [README.md example](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) by Kera Kudmore to plan and layout my headings and content, to ensure I didn't omit any important content.

The Credits section is where you can credit all the people and sources you used throughout your project.

Code Used
If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

Content
Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

 Media
If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.

 Acknowledgments
If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.