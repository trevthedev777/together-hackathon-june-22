# TESTING

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[What You Need :arrow_right:](https://connect-with.herokuapp.com/)**.

## Table of Content

* [Code Validation](#Code-Validation)
  * [W3C](#W3C)
  * [Flake8](#Flake8)
* [Manual Testing](#Manual-Testing)
  * [Functionality Testing](#Functionality-Testing)

## Code Validation

All code validation has been done using text input. The code was copied from the source code in the browser. This allows to check HTML without getting error because of Jinja templating language.

### W3C

W3C Markup Validation Service and W3C CSS Validation Service have been used to check all the pages of the website for semantic and syntax errors.
The results show no errors and the code is valid.

* [W3C Markup Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

### Flake8

Flake8 was used to validate the Python code for semantic and syntax errors.  
The results are positive, and the code is valid.  

* Warnings were found:
Two of those warnings are coming from signals being imported in apps.py of the checkout and products apps. They are designed to be used that way from my best knowledge and therefore were left with the warning.  
The third warning is for 3 line too long from the Django boilerplate in settings.py.  
We decided to leave the unused file as they will be part of future feature of the website.

## Manual Testing

* Manual testing was executed on several browsers (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari and Opera) and shows good functionality across them all.
* The responsiveness of the website for different viewport sizes was tested by dragging the window up, down, left and right.  
* The following tests have been executed several times at different viewport breakpoints and on different devices.  
* Fellow Code Institute students tested the website on different devices.

### Functionality Testing

#### General features

* Buttons change state/style
  * on hover :heavy_check_mark:
  * on focus :heavy_check_mark:
  * on active :heavy_check_mark:
  * on click and expected behavior happens :heavy_check_mark:
* Link change state/style
  * on hover :heavy_check_mark:
  * on focus :heavy_check_mark:
  * on active :heavy_check_mark:
  * on click and expected behavior happens :heavy_check_mark:
* Forms validation
  * inputs/ content :heavy_check_mark:
  * on submit :heavy_check_mark:
* Modal Triggers :heavy_check_mark:
