import os
import yaml
import shutil
import time
from datetime import date, timedelta, datetime
from subprocess import Popen, PIPE

CURRENT_PATH = os.path.abspath(".")
OPTION_LIST = None
with open(CURRENT_PATH + "/option.yaml") as file:
    OPTION_LIST = yaml.full_load(file)

def CheckRepoExist():
    folder_name = "/backup"
    if os.path.exists(CURRENT_PATH + folder_name) is False:
        os.mkdir(CURRENT_PATH + folder_name)
    if os.path.exists(CURRENT_PATH + "/" + OPTION_LIST["repo_name"]):
        buckup_folder_name = str(date.today())
        shutil.move(CURRENT_PATH + "/" + OPTION_LIST["repo_name"], CURRENT_PATH + folder_name + "/" + buckup_folder_name)

def CloneRepo():
    p1 = Popen(['git', 'clone', OPTION_LIST["clone_url"]], stdout=PIPE)
    p1.wait()
    os.chdir("./" + OPTION_LIST["repo_name"])
    p2 = Popen(['git', 'pull', '--all'], stdout=PIPE)
    p2.wait()
    os.chdir(CURRENT_PATH)

def RemoveExpiredRepos():
    folder_name = "/backup"
    os.chdir(CURRENT_PATH + folder_name)
    limit_date = date.today() - timedelta(days=7)
    dir_list = [f for f in os.listdir("./")]
    for dir in dir_list:
        folder_date = datetime.strptime(dir, '%Y-%m-%d').date()
        if limit_date > folder_date:
            shutil.rmtree(dir)

def main():
    CheckRepoExist()
    CloneRepo()
    RemoveExpiredRepos()

if __name__ == "__main__":
    main()