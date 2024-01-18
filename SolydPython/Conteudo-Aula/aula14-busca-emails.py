import re
import requests

"""
Problem: getting all emails present on a website

 Solution: make get requests and later search for email regular expressions using the RE library and get all appearances of emails present in the website's HTML.
 We then present the found emails to the user.
"""


site_request = input("Write the text to find emails: ")

site = requests.get(site_request)

finding_emails = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", site.text)

if finding_emails:
    print("*"*50)
    print("Emails Finding:")
    print("-"*50)
    for i, j in enumerate(finding_emails):
        print(i, j)