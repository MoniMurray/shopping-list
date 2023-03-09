PROJECT PORTFOLIO 4 SHOPPING LIST - TESTING
👩🏻‍💻 View an example of this section here

Add an image of the finished site here. I like to use amiresponsive to get an image of my site on all device sizes, and amiresponsive allows you to click links on the page and scroll, so each device can show a different element of your site.

The site is deployed using Heroku - [MYM Shopping List](https://mym-shopping-list.herokuapp.com/)

If you want to add optional shields.io badges to your TESTING file, I like to add them to this section (Shields.io have some badges for W3C validation which makes it easy to see at a glance whether the project has passed validation).

CONTENTS
AUTOMATED TESTING

W3C Validator
Lighthouse
WAVE
MANUAL TESTING

Testing User Stories
Full Testing
BUGS

Known Bugs
Solved Bugs
AUTOMATED TESTING
The Automated Testing includes all the testing that is carried out by a program, like W3C HTML validation.

 W3C Validator
👩🏻‍💻 View an example of a completed W3C HTML & CSS validation section here

The most popular HTML validator is W3C. There are two ways to validate the HTML for your first milestone - you can copy the live link for your site page and paste into the validate by URI field, or you can copy all the code for your page and paste this into the validate by direct input field.

URI Input
If you validate with your sites URL, you can run the validation and then copy the link from the address bar and insert the link here as your proof of validation.

W3C URI Validator

Direct Input
If you validate with the code, you will need to screenshot the validation results and then link the image here.

W3C Direct Input Validator

CSS Validation
CSS Validation can only be done by copying and pasting the CSS file contents into the direct input. Make sure that the checkbox for CSS is selected.

W3C CSS Validation

Lighthouse
👩🏻‍💻 View an example of a completed lighthouse testing section here

Lighthouse Testing is part of the Chrome Developer Tools. For more information on how to use this tool, please visit chrome Lighthouse.

You will need to run the Lighthouse testing on each individual page of your site, for desktop as a minimum. If you have time it would be great to also add in the mobile testing.

Lighthouse Testing

WAVE
👩🏻‍💻 View an example of a completed WAVE testing section here

WAVE is an accessibility testing tool. I like to run this on each page of my site and take a screenshot of the results to add here. They have a website for testing and a Chrome extension.

Wave Desktop

Wave Exetension

MANUAL TESTING
Testing User Stories
👩🏻‍💻 View an example of a completed user stories testing section here

This is where you will test the user stories you created in the README against your site. Use the User Stories table for this Test Case list, the Acceptance Criteria Tasks are repurposed to become the Tests  - use an additional column to add any supporting images by way of links.

AUTOMATED TESTING

I tested this project using [Django TestCase](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
Testing Features
👩🏻‍💻 View a feature list table here

This is where you will test the features as you create them in the README against your site. Use a table for this section - base the table on the User Acceptance Criteria for the User Cases.

Full Testing
👩🏻‍💻 View an example of a completed full testing section here

Full testing is when you go through the site and test every single thing that can be tested.  Display in a table.

Coverage Tool

This needs to be installed.  

pip3 install coverage

to run this tool:

coverage run --source=list manage.py test

It tells you what % of the app's code has been tested - it does not tell you what % of your code passed the tests. It generates a report which should be pasted into here.  To generate an overview report type:

coverage report

To generate an interactive HTML report use the following command:

coverage html

This will create a new folder called htmlcov in which tere is an index.html file, to view the file type:

python3 -m http.server

Open browser, inspect files

Write any remaining tests Coverage reports has gone untested.

BUGS
Known Bugs
List (or put in a table) all known bugs on your site here as soon as you find them. This will prevent you from forgetting any at the end. Some (if not all) of these bugs will hopefully make their way over to the next section, solved bugs, as you progress through your project.

Solved Bugs
👩🏻‍💻View an example of a completed bugs section here

This is where all solved bugs go once squashed. List what the bug was, and how you managed to fix it. You can also include images/videos here if you wanted.