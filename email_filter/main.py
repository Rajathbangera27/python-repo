import re

def fun(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)

def filter_mail(emails):
    return list(filter(fun, emails))
print("Enter the no emails")
n = int(input())
print("enter the email id")
emails = []
for i in range(n):
    emails.append(input())

valid_emails = filter_mail(emails)

valid_emails.sort()

print(valid_emails)