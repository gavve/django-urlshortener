# django-urlshortener

=====
URLShortener
=====

URLShortener is not like every other URLShortener, it finds words in the URL from the words.txt file.
Feel free to add whatever words you like to words.txt

Detailed documentation is in the "docs" directory.

Quick start
-----------
Before doing these steps you need to set up a virtual environment with Django.
If you don't know how to do this, there are documentations in the "docs" directory

1. Add "urlshortener" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'urlshortener',
    ]
	
2. Add your domain that you want to use for the SHORT_URL_BASE in your settings file like this::
	SHORT_URL_BASE = 'http://yourdomainname.com'  

2. Include the urlshortener URLconf in your project urls.py like this::

    url(r'^urlshortener/', include('urlshortener.urls')),

3. Run `python manage.py migrate` to create the urlshortener models.

4. Start the development server and visit http://127.0.0.1:8000/ Here you will see an form where you
	can type in any long url (must start with http://) and hit the button to generate a shorturl

5. After you genereate a short url it will be displayed for you and you can try to visit it and it will
	redirect you to the original website that you first entered.
