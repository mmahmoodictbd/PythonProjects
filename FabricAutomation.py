from fabric.api import *
from datetime import datetime
from fabric.utils import puts, warn

# This script is intended to do all sort of task for ebajar.com

PROD_SERVER = 'ubuntu@52.76.40.148:22'

# Setting env
env.hosts = [PROD_SERVER]
env.key_filename = "~/Downloads/SpringinOfficeMahmoodPC.pem"
env.base = "/vol"
env.user = "ubuntu"

# Variables
GIT_REPO_URL="https://mmahmoodictbd@bitbucket.org/mmahmoodictbd/ebajar.com.git"
GIT_PULL_NEW_CODE ="git pull origin master"
MVN_BUILD_WAR = "mvn clean compile package >/dev/null 2>&1 &"
MVN_BUILD_WAR_FILE_PATH = "/vol/Code/ebajar.com/target/Ebajar.war"

DB_NAME = "ebajar"
DB_USER = "dev"
DB_PASS = "Zza*c^RR^@Dn+R9s"
DB_DUMP_BACKUP_PATH = "/vol/DbDumps"

CODE_PATH = "/vol/Code/ebajar.com"
OLD_WARS_PATH = "/vol/OldWars"
TOMCAT_PATH = "/vol/apache-tomcat-8.0.24-ebajar-prod"
TOMCAT_WAR_PATH = "/vol/apache-tomcat-8.0.24-ebajar-prod/webapps/ROOT.war"
TOMCAT_WEBAPPS_PATH = "/vol/apache-tomcat-8.0.24-ebajar-prod/webapps"

# Build Server
def build():

    #copyItself()
    #dbdump()
    shutdownTomcat()
    copyOldWarToBackup()
    deleteEverythingInTomcatWebapps()
    gitPullAndCreateWar()
    moveWarToTomcatWebapps()
    startTomcat()

def copyOldWarToBackup():
    oldWarName = datetime.now().strftime('Ebajar_%Y-%m-%d_%H:%M:%S.war')
    run('mv %s %s >/dev/null 2>&1 &' %(TOMCAT_WAR_PATH, OLD_WARS_PATH))
    with cd(OLD_WARS_PATH):
        run('mv ROOT.war %s >/dev/null 2>&1 &' %(oldWarName))

def deleteEverythingInTomcatWebapps():
    with cd(TOMCAT_WEBAPPS_PATH):
        run("rm -rf *")

def gitPullAndCreateWar():
    with cd(CODE_PATH):
        run(GIT_PULL_NEW_CODE)
        run(MVN_BUILD_WAR)

def moveWarToTomcatWebapps():
    run('mv %s %s >/dev/null 2>&1 &' %(MVN_BUILD_WAR_FILE_PATH, TOMCAT_WEBAPPS_PATH))
    with cd(TOMCAT_WEBAPPS_PATH):
        run("mv Ebajar.war ROOT.war 2>/dev/null")

def shutdownTomcat():
    puts("Shuting down tomcat...")
    with cd(TOMCAT_PATH):
        run("./bin/shutdown.sh  >/dev/null 2>&1 &")
        run("fuser -k 8080/tcp >/dev/null 2>&1 &")
        puts("Tomcat shutdown successfully.")
def startTomcat():
    with cd(TOMCAT_PATH):
        run("./bin/start.sh >/dev/null 2>&1 &")

def dbdump():
    
    sqlDumpFileName = datetime.now().strftime('dump_%Y-%m-%d_%H:%M:%S')
    run('mysqldump -u %s -p%s %s  | bzip2 > %s/%s.sql.bz2' %(DB_USER, DB_PASS, DB_NAME, DB_DUMP_BACKUP_PATH, sqlDumpFileName))
    

# Need this because cron job need to call dbdumplocal
def copyItself():
    put('deploy_ec2_fab.py', '/vol')

# Cron job added using command - sudo crontab -e, see it using sudo crontab -l
# Cron job @everyday 10PM
# 0 22 * * * /usr/bin/fab -f /vol/deploy_ec2_fab.py dbdumplocal 
def dbdumplocal():
    
    sqlDumpFileName = datetime.now().strftime('dump_%Y-%m-%d_%H:%M:%S')
    local('mysqldump -u %s -p%s %s  | bzip2 > %s/%s.sql.bz2' %(DB_USER, DB_PASS, DB_NAME, DB_DUMP_BACKUP_PATH, sqlDumpFileName))
