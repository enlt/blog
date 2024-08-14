import os
import subprocess
from datetime import datetime

def run_command(command, ignore_errors=False):
    print(f"{command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        if not ignore_errors:
            print(f"{command}\n{result.stderr}")
            exit(1)
    return result

github_token = os.getenv("GITHUB_TOKEN")
if not github_token:
    print("Error: GITHUB_TOKEN is not set")
    exit(1)

run_command("git add .")

commit_message = f"Hexo source {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
run_command(f"git commit -m \"{commit_message}\"")

run_command("git remote remove origin", ignore_errors=True)

run_command(f"git remote add origin https://{github_token}@github.com/enlt/blog.git")

run_command("git push -f origin main")

run_command("hexo c")
run_command("hexo g")
run_command("hexo d")