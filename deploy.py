import os
import subprocess
from datetime import datetime

def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        exit(1)

github_token = os.getenv("GITHUB_TOKEN")
if not github_token:
    print("Error: GITHUB_TOKEN is not set")
    exit(1)

run_command("git init")
run_command("git add .")

commit_message = f"Hexo source {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
run_command(f"git commit -m \"{commit_message}\"")

run_command("git remote remove origin")

run_command(f"git remote add origin https://{github_token}@github.com/enlt/blog.git")
run_command("git push -f origin main")

run_command("hexo clean")
run_command("hexo generate")
run_command("hexo deploy")