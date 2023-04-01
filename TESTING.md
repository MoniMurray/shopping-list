PROJECT PORTFOLIO 4 THE SHOPPING LIST - TESTING


👩🏻‍💻 View an example of this section here

Add an image of the finished site here. I like to use amiresponsive to get an image of my site on all device sizes, and amiresponsive allows you to click links on the page and scroll, so each device can show a different element of your site.


CONTENTS

1. [AUTOMATED TESTING](#automated testing)

2. [MANUAL TESTING](#manual testing)



AUTOMATED TESTING<a name="automated testing"></a>

Automated Testing includes all testing that is carried out by a program -  W3C HTML validation and CSS Validation, PEP8 Python Compliance, Lighthouse responsiveness.

 W3C Validator
👩🏻‍💻 View an example of a completed W3C HTML & CSS validation section here

The most popular HTML validator is W3C. There are two ways to validate the HTML for your first milestone - you can copy the live link for your site page and paste into the validate by URI field, or you can copy all the code for your page and paste this into the validate by direct input field.

URL Input
If you validate with your sites URL, you can run the validation and then copy the link from the address bar and insert the link here as your proof of validation.

W3C URL Validator

Direct Input
If you validate with the code, you will need to screenshot the validation results and then link the image here.

W3C Direct Input Validator

CSS Validation

CSS Validation can only be done by copying and pasting the CSS file contents into the direct input. Make sure that the checkbox for CSS is selected.

W3C CSS Validation

Python Code testing

[CI Python Linter](https://pep8ci.herokuapp.com/)

Lighthouse
👩🏻‍💻 View an example of a completed lighthouse testing section here

Lighthouse Testing is part of the Chrome Developer Tools. For more information on how to use this tool, please visit chrome Lighthouse.

You will need to run the Lighthouse testing on each individual page of your site, for desktop as a minimum. If you have time it would be great to also add in the mobile testing.

WAVE
👩🏻‍💻 View an example of a completed WAVE testing section here

WAVE is an accessibility testing tool. I like to run this on each page of my site and take a screenshot of the results to add here. They have a website for testing and a Chrome extension.

Wave Desktop

Wave Exetension

I tested this project using [Django TestCase](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)

Testing Features
👩🏻‍💻 View a feature list table here

This is where you will test the features as you create them in the README against your site. Use a table for this section - base the table on the User Acceptance Criteria for the User Cases.

Full Testing
👩🏻‍💻 View an example of a completed full testing section here

Full testing is when you go through the site and test every single thing that can be tested, which should be displayed in a table.

Coverage Tool

The Coverage testing tool evaluates your whole project and reports on what percentage of the project has been tested with automated testing.  This tool needs to be installed, in the CLI type:  

pip3 install coverage

To run the Coverage tool, in the CLI type:

coverage run --source=list manage.py test

Coverage tells you what percentage of the application's code has been tested - it does not tell you what percentage of your code passed the tests. Coverage generates a report in HTML, in the CLI type:

coverage report

To generate an interactive HTML report use the following command in the CLI:

coverage html

This will create a new folder called 'htmlcov' in which there is an index.html file.  As with all html files, in order to view the file, in the CLI type:

python3 -m http.server

Open the browser to inspect files which will indicate where in the application tests still need to be performed.

Write any remaining tests Coverage reports has gone untested.

BUGS
Known Bugs
List (or put in a table) all known bugs on your site here as soon as you find them. This will prevent you from forgetting any at the end. Some (if not all) of these bugs will hopefully make their way over to the next section, solved bugs, as you progress through your project.

Solved Bugs
👩🏻‍💻View an example of a completed bugs section here

This is where all solved bugs go once squashed. List what the bug was, and how you managed to fix it. You can also include images/videos here if you wanted.

MANUAL TESTING<a name="manual testing"></a>

Testing User Stories
Full Testing
BUGS

Known Bugs
Solved Bugs

Manual testing tests as follows:

- Each Feature
- Each User Story
- Visual Responsiveness
- Browser Compatibility Testing
- Report on Bugs resolves/unresolved


Testing User Stories
👩🏻‍💻 View an example of a completed user stories testing section here

This is where I tested the User Stories I created and listed in [AGILE.md](AGILE.md) against my application. I have used the User Stories table for this Test Case list, the Acceptance Criteria Tasks are repurposed to become the Tests.

*insert Manual Testing table*

BUGS
Known Bugs
List (or put in a table) all known bugs on your site here as soon as you find them. This will prevent you from forgetting any at the end. Some (if not all) of these bugs will hopefully make their way over to the next section, solved bugs, as you progress through your project.

Solved Bugs
👩🏻‍💻View an example of a completed bugs section here