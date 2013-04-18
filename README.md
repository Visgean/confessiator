Confessiator
=============

Confessiator is a tool to enable your facebook users confess anonymously to your Facebook wall.



Installation on Openshift: 
==========================

1. register on [Redhats Openshift](https://www.openshift.com/)
2. [install openshift tools](https://www.openshift.com/get-started) - sudo gem install rhc && gem update rhc and run ''' rhc setup'''
3. create confessiator project: '''bash rhc app create <name> python-2.7''' (replace with your name)
4. add postgresql db: ''' rhc cartridge add postgresql-8.4 --app <name>'''
5. add cron: ''' rhc cartridge add cron-1.4 --app <name>'''
6. pull this repo: ''' git clone https://github.com/Visgean/confessiator.git'''
7. obtain git repo url from https://openshift.redhat.com/app/console/applications/<name> add this url to repo from previous step: git remote add openshift ssh://<repo_url>
8. register new application on facebook, set login name to your application url <sudbomain>.rhcloud.com
9. get ssh details on https://openshift.redhat.com/app/console/applications/<name> -> click on 'WANT TO LOG IN TO YOUR APPLICATION?' and log to it
10. on remote machine create file credentials with your secret tokens: ''' nano ~/app-root/data/credentials.py''' using following [pattern](https://github.com/Visgean/confessiator/blob/master/confessiator/credentials_template.py) and edit it accordingly.
11. push to the server: ''' git push openshift ''' from the cloned repo
12. $$$ profit!