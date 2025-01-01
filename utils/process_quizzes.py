import os
import requests
import json
import shutil
from constants import QUIZ_URL

def download_quiz(udemy, quiz_id, download_folder_path, title_of_output_quiz, task_id, progress, portal_name):
    progress.update(task_id, description=f"Downloading Quiz {title_of_output_quiz}", completed=0)

    quiz_filename = f"{title_of_output_quiz}.json"
    quiz_url = QUIZ_URL.format(portal_name=portal_name, quiz_id=quiz_id)
    quiz_response = udemy.request(quiz_url).json()

    with open(os.path.join(os.path.dirname(download_folder_path), quiz_filename), 'w', encoding='utf-8', errors='replace') as file:
        json.dump(quiz_response, file, indent=4)

    progress.console.log(f"[green]Downloaded {title_of_output_quiz}[/green] ✓")
    progress.remove_task(task_id)

    shutil.rmtree(download_folder_path)
