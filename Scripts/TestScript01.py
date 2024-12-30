import os

github_secret = os.getenv('GITHUB_SECRET')

words = github_secret.split()

for word in words:
        print(word)