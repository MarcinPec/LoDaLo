
![Logo](https://i.ibb.co/FVSWt50/lodalo-logo.png)



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



# LoDaLo - Login Data Lord

A password manager written in Python, the purpose of which is to securely store logins, passwords, URLs in csv files, as well as generate and analyze strenght of passwords.


## Features

- Classic strong password generator with a built-in security analyzer
- Login generator based on a given template
- Artificial intelligence-based associative password generator with built-in security analyzer
- Database manager with automatic and manual refresh system based on .csv files
- Simple CSV file encryption mechanism
- Application login system requiring knowledge of only one password, identical to most commercial applications of this type
- User interface based on the Flutter toolkit for Python - FLET


## Screenshots

![App Screenshot](https://i.ibb.co/vj7RFLn/1.png)
![App Screenshot](https://i.ibb.co/FD8SbP7/2.png)
![App Screenshot](https://i.ibb.co/3zYx4Ph/3.png)
![App Screenshot](https://i.ibb.co/k32gFp6/4.png)



## Description of the project

The manager works by using a simple graphical navigation interface created based on the Flet framework, through which the user can select the functionality he is interested in - a classic generator, an associative generator or a login database. Gaining access to the application is possible as in the case of other commercial programs of this type, i.e. after entering the main password in the login window, which is displayed each time the application is started and stored in an encrypted text file. This password can only be changed via the "REDEFINE!" option. in the LoDaLo settings panel. Due to the encryption mechanism used, direct editing of the .txt file may prevent access to the application.

Classic passwords are generated via the GenPass class, whose attributes are the password length and the content of its components, i.e. numbers and/or letters and/or special characters. This class checks the status of component elements based on simple rules of Boolean algebra - True/False. The GenPass class consists of 4 methods - 3 generators with decorators that convert the resulting generator expression into a string or list, and 1 method that composes a password from a string. For better exception management, a custom LengthError class was used, which is an exception thrown by the application when it tries to generate a password that is too long.

Creating logins is done in a similar way to generating classic passwords, with the total length of the login and therefore the length of the generated part being determined by a given pattern. Therefore, the GenLogin class, unlike GenPass, accepts an additional pattern attribute. The remaining functionalities of this class are identical to those of the GenPass class.

Associative passwords in LoDaLo are generated using the AssociationalBigramPassGen class, which generates passwords based on bigrams (pairs of letters) from the provided dictionary data (Polish and English words). The class offers various options for generating passwords, including the ability to separate segments with special characters.

The module responsible for displaying the database of collected login data and for interacting with it is the basic functional element of the LoDaLo program. The operation of this module is based on generating a table containing the record ID number, URL address, login, password, password strength and its time resistance to brute force cracking. The database allows you to add a new record, edit an existing record, and delete selected records. Providing the complete URL of the login page allows it to be opened in the default browser using the "Open in browser..." function generated for each record separately.

The password security analyzer was created based on the AI ​​library for Python - PyTorch. The code of this module consists of two classes: PasswordStrengthModel and PasswordStrengthTimer. These classes are used to assess and estimate the strength of a password and the time needed to crack it using a simple neural network model and mathematical calculations.




## Tech

**GUI:** flet

**Logic:** asyncio, os, webbrowser, random, string, csv, colections

**AI:** pytorch

**Unit tests:** pytest


## Installation and launch of the LoDaLo

To properly run the LoDaLo project, you must first install the following libraries and frameworks in your environment:
- flet – enter the command in the terminal:

```bash
  pip install flet
```

- pytorch - enter the command in the terminal:
```bash
  pip install pytorch
```

    
- asyncio - enter the command in the terminal:
```bash
  pip install asyncio
```
- pytest - enter the command in the terminal:

```bash
  pip install pytest
```

To run the entire project, execute the file: .

```bash
  l0_lodalo_main_fin_gui.py
```
    
## Running Tests

For the discussed project, a set of 1529 unit tests was designed based on the pytest library. The test scenarios were edited and saved in the file test_lodalo_engines.py. The tests included assertions with parameterization regarding the correct (consistent with the specified) length of passwords and the correct selection of password components - letters, numbers or special characters - depending on the test scenario. Modules containing logical engines for the classic, associative password and login generator were tested. Therefore, test_lodalo_engines.py has been divided into 3 sections testing individual engines. To run the test_lodalo_engines.py file, enter:


```bash
  pytest test_lodalo_engines.py
```


## Video demonstration of LoDaLo

https://youtu.be/E9md5IyXBYY

## Authors

- [Marcin 'MarcinPec' Pecuch](https://www.github.com/MarcinPec)


## License

[MIT](https://choosealicense.com/licenses/mit/)

