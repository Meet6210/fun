CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

"""
The WTF_CSRF_ENABLED setting activates the cross-site request forgery 
prevention. Cross-Site Request Forgery (CSRF) is a type of attack that occurs 
when a malicious Web site, email, blog, instant message, or program causes 
a user's Web browser to perform an unwanted action on a trusted site for which
 the user is currently authenticated.
 In most cases, this option is enabled as it makes the app more secure.

The SECRET_KEY setting is only needed when CSRF is enabled, and is used to 
create a cryptographic token that is used to validate a form.
"""