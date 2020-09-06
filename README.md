# MezBlog-flask

[![Language](https://img.shields.io/badge/language-python-brightgreen?style=flat-square)](https://www.python.org/)

Hello everyone! This is the repository of my another blog application on Flask from YouTube lessons.

## Table of contents

- [Table of contents](#table-of-contents)
- [Motivation](#motivation)
- [Badges](#badges)
- [Code style](#code-style)
- [Tech/framework used](#techframework-used)
- [Features](#features)
- [Installation](#installation)
- [Fast usage](#fast-usage)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Motivation

I just want more practice with **Flask**.😄

## Badges

Other badges

[![Theme](https://img.shields.io/badge/Theme-Blog-brightgreen?style=flat-square)](https://uk.wikipedia.org/wiki/%D0%91%D0%BB%D0%BE%D0%B3)
[![Platform](https://img.shields.io/badge/Platform-Flask-brightgreen?style=flat-square)](https://flask.palletsprojects.com/en/1.1.x/)

## Code style

I'm using [Codacy](https://www.codacy.com/) for automate my code quality.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f385d31038844f33a9cc939e6a76204f)](https://www.codacy.com/manual/mezgoodle/MezBlog-flask?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/MezBlog-flask&amp;utm_campaign=Badge_Grade)


## Tech/framework used

**Built with**

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

> Also other libraries you can see in the [requirements.txt](https://github.com/mezgoodle/MezBlog-flask/blob/master/requirements.txt)

## Features

On the site with _flask_ you can **create** posts, tags, **manage** them with the admin panel.

## Installation

1. Clone this repository:

```
git clone https://github.com/mezgoodle/MezBlog-flask.git
```

2. Install all dependencies with [pip](https://pip.pypa.io/en/stable/):

```
pip install -r requirements.txt
```

## Fast usage

1. Create database with the following commands:

```
> python
> from app import db
> db.create_all()
> exit()
```

2. Start the development server:

```
> python3 app.py
```

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits

Link to the tutorial [playlist](https://www.youtube.com/watch?v=Y_oyx36AdV0&list=PLlWXhlUMyooZr5R2u2Zwxt6Pw6iwBo5y5) on the YouTube.

## License

MIT © [mezgoodle](https://github.com/mezgoodle)
