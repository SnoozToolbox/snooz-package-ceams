# How to develop in the Snooz platform with git command

## Install git for windows
* Download and install gitforwindows from : https://gitforwindows.org/

## Manage your credentials
### Create an App password from Bitbucket
Select your avatar (Your profile and settings) from the navigation bar at the top of the screen.
Under Settings, select Personal settings.
	i.e. when you are logged in : https://bitbucket.org/account/settings/
On the sidebar, select App passwords.
Select Create app password.
Give the App password a name, usually related to the application that will use the password.
-> copy the password generated
### Store locally the password
In the git bash command window
$ git config --global user.name "your_user_name" 
	ex. git config --global user.name "klacourse"
$ git config --global user.email "your_email"
	ex. git config --global user.email "karine.lacourse.cnmtl@ssss.gouv.qc.ca"
$ git config --global user.password "the_copied_password"
$ git config --global credential.helper store
A popup window shouls ask you to login into Atlassian Bitbucket
	Fill the username and password
	Authorize the access
You should be set for a while.

Sometime (when you work on a station with multiple users)
You have to set the remote url
$ git remote set-url origin "the remote url"
	ex. git remote set-url origin https://klacourse@bitbucket.org/ceamscarsm/scinodes_poc.git


## Clone the Snooz repository (scinode_poc)
This will install the source code for Snooz.
> Make sure you have a bitbucket account: https://bitbucket.org
> Make sure your are added as a team worker (collaborator) on the scinodes_poc repository : 
	https://bitbucket.org/ceamscarsm/workspace/settings/groups

### Download the source code for Snooz (from scinode_poc)
* Launch Git Bash
* In the git bash terminal create your local repository, clone the repository:
	* Go to the remote repository on BitBucket : https://bitbucket.org/ceamscarsm/scinodes_poc/src/master/
	* Click on Clone on the top right corner.
	* Copy the https command line and paste it on the git bash prompt examples : 

			$ cd /c/Users/klacourse/Documents
			$ git clone https://klacourse@bitbucket.org/ceamscarsm/scinodes_poc.git

* Run the script to add the local settings to your git ignore.
		
		$ ./gitignore_local_settings.sh

### Download the source code for plugins in development for Snooz (from ceams_package)
* Launch Git Bash
* In the git bash terminal create your local repository, clone the repository:
	* Go to the remote repository on BitBucket : https://bitbucket.org/ceamscarsm/ceams_package/src/master/
	* Click on Clone on the top right corner.
	* Copy the https command line and paste it on the git bash prompt examples : 

			$ cd /c/Users/klacourse/Documents
			$ git clone https://klacourse@bitbucket.org/ceamscarsm/ceams_package.git

## Setup your work repository for your own Modules and Tools package
You need to create another repository with your own modules and packages and link Snooz to them.

* Fork the "snooz_package_template" repository
	go to : https://bitbucket.org/ceamscarsm/snooz_package_template/src/master/
	click on the ... and fork this repository
	You can rename the repository
* Clone your forked "snooz_package_template" repository
	go to : https://bitbucket.org/[YOUR_USERNAME]/snooz_package_template/src/master/
	* Click on Clone on the top right corner.
	* Copy the https command line and paste it on the git bash prompt examples : 
		$ cd /c/Users/klacourse/Documents
		$ git clone https://klacourse@bitbucket.org/klacourse/snooz_package_template.git


# The proposed Git strategy 
We propose to work on a feature or debug branch in order to keep the master always in a working state.
	Add/commit/push your local modifications from your branch as often as possible.
	This allows to save your last modification on the remote server.
	Enter a log message for each commit to make your changes trackable.
	Once your feature is validated you add it to the master.
	There are many techniques available, use the one you prefer.
	Here we describe how to squash multiple commits from a feature branch into one clean commit in the master.

### Create your branch
	$ git branch branch_name
	$ git checkout branch_name

### Create, modify, delete your files
All your modifications are local only, you can always revert your change to go back to the last commit.

### Add and commit your changes in the current branch
	$ git add . --all
	$ git commit -m "your personal log message"

### Push your change into the remote reposity server
The first time you push on a new branch you have to push with the option --set-upstream
	$ git push --set-upstream origin branch_name
otherwise
	$ git push

### Squash multiple commits from a feature branch into the master
Once your feature is validated and you want to add it to the master.
	https://makandracards.com/makandra/527-squash-several-git-commits-into-a-single-commit
	https://gist.github.com/patik/b8a9dc5cd356f9f6f980
Switch to the master branch and make sure you are up to date
	$ git checkout master
	$ git pull
Merge your feature branch into the master branch locally
	$ git merge branch_name
To solve conflicts
	To get the file from the feature branch
		$ git checkout --theirs path_to_file
	To get the file from the master 
		$ git checkout --ours path_to_file
Reset the local master branch to origin's state:
	$ git reset origin/master
Now all of your changes are considered as unstaged changes. 
You can test snooz, run pipeline, validate and modify the files if needed.
You can add/commit/push them into one clean commit that includes the whole code for a feature.
	$ git add . --all
	$ git commit -m "Your log message"
	$ git push

# Other useful commands

## To get the local git status (file modified locally)
	$ git status

## To get the last remote version of a file
	$ git checkout path_to_file

## To go back to the last remote version of a current branch 
When you want to get rid of all the local modifications
	$ git reset --hard HEAD
	$ git reset --hard origin/branch_name

## How to branch
To list branches all branches
	$ git branch -a
To list active remote branch
	$ git ls-remote --heads origin
To delete branch locally
	$ git branch -d branch_name
To delete branch remotely
	$ git push origin --delete branch_name
To delete all local branches
	$ git branch | grep -v "master" | xargs git branch -D 
To rename a remote branch
	$ git checkout <old_name>
	$ git branch -m <new_name>
	$ git push origin -u <new_name>
	$ git push origin --delete <old_name>
	
## How to manage conflicts
*** Git merge scenario ***
Ours is the current branch (destination of the merge)
Theirs is the branch to merge into (source of the merge)
You have to checkout the destination branch

	To merge the feature branch (source) into the master (destination)
		$ git checkout master
		$ git merge branch_name
	To select the changes done in master (destination)
		$ git checkout --ours /path/to/file
	To select the changes done in the feature branch (source)
		$ git checkout --theirs /path/to/file

	To merge the master (source) into the feature branch (destination)
		$ git checkout branch_name
		$ git merge master
	To select the changes done in master (source)
		$ git checkout --theirs /path/to/file
	To select the changes done in feature (destination)
		$ git checkout --ours /path/to/file

## To TAG
Example to tag the master
	$ git checkout master
	$ git tag -a v1.0.0 -m "first version distributed v1.0.0"
	$ git push origin v1.0.0
To checkout a tagged version
	$ git checkout v1.0.0
To delete the tag on any remote before you push
	$ git push origin :refs/tags/<tagname>
To replace the tag to reference the most recent commit
	$ git tag -fa <tagname>
	$ git push -f origin <tagname>
To tag an older commit
	$ git tag -a vx.x.x commit_id -m "message"
	$ git push origin --tags
	ex) $ git tag -a v0.3.0 122cbd2 -m "RapidEyeMovementTools linked to CEAMSModules v3.0.0"
		$ git push origin --tags 
git tag -a v1.0.0 f4ebce6 -m "Snooz with CEAMSModules v2.0.0 and CEAMSTools v2.0.0"
To rename a tag
	# Create a new local tag named `new` from tag `old`.
	$ git tag new old          
	# Delete local tag `old`.
	$ git tag -d old       
	# Push `new` to your remote named "origin", and delete    
	$ git push origin new :old 
	# tag `old` on origin (by pushing an empty tag name to it).

## To add back a file tracked in git
	$ git update-index --no-skip-worktree path_to_file
		ex) git update-index --no-skip-worktree .vscode/launch.json

## How to ignore new ext file
Make changes in .gitignore file.
	$ git status

                                                                        