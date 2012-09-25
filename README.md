Redmine-T2MC: redmine textile to markdown converter
===

This is a small script I wrote for a particular situation I faced: I used redmine for a few months using the textile syntax in both wiki pages and knowledgebase articles. Since then, I have come to love markdown and use it everyday. So I needed a way to convert all the database textile content into markdown without much hassle. This is what this script is all about.

### Dependencies & assumptions

This script assumes you're using redmine 1.3 and the [knowledge base plugin](https://github.com/alexbevi/redmine_knowledgebase) (you may edit the script if you're not). Other dependencies:

* You must have [pandoc](http://johnmacfarlane.net/pandoc/) installed (you may use homebrew it using mac os)
* You must have python installed on your machine
* You must have django installed (more on this later)

### Usage

You should be able to run the `converter.py` straight away:

```
  python converter.py
```

What it does is use django settings in order to leverage the django's ORM middleware and deal with models instead of raw sql.

The `app` folder must contain the `models.py` because django wants it that way. The `models.py` inside that folder is a result of the django's inspectdb feature. It goes like this:

```
  django-admin.py startproject dumb_project
  cd dumb_project
  django-admin.py startapp app
  cd app
  python manage.py inspectdb > models.py
```
  
Then just move the `app` folder to the one `converter.py` is in (and don't care if it doesn't make sense).

You may remove all classes from the `models.py` file except the ones you actually need: `WikiContents` and `KbArticles`.