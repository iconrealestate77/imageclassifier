import getpass
from github import Github
import os

token = getpass.getpass()
g = Github(token)
repo = g.get_repo("iconrealestate77/imageclassifier")

folder = "."
for filename in os.listdir(folder):
    if filename.startswith('.'):
        continue
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            content = f.read()
        try:
            existing = repo.get_contents(filename)
            repo.update_file(filename, f"Update {filename}", content, existing.sha)
            print(f"Updated {filename}")
        except Exception:
            repo.create_file(filename, f"Add {filename}", content)
            print(f"Created {filename}")
