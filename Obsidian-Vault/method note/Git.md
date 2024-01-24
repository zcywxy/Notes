
`open .` will open the current folder through the interface
[Linux note](https://www.yuque.com/crystalbell98/xny4s4/tmtg3e)

`git init` will initiate the git repository under the path
`git status` check current git repository
*do not initiate repo in the existed repo*

`git config user.name` list whether you have a config user name or not
	`git config --global user.name "Yuan Yang"`
`ls -a` can show the hidden file *.git* which track all the changes

commit is the check point

`git add` after working on stuff and making changes, group and call out the changes by `git add` *file name*. `git add .` make all ready to stage
	![[Pasted image 20231224104502.png|200]] ![[Pasted image 20231224105135.png|400]] ![[Pasted image 20231224105151.png|400]]
`git commit -m "my message"` 
	message should be present tense and imperative
	`git commit` will enter the vim editor mode to add the message. We can change the default editor
	`git commit --ammend` enter the last commit log editor to make changes
`git log` option --oneline 
.gitignore
`git branch` view the existed branch
	`git branch <branch-name>` create new branch, the name should not include space, for example: `git branch bug-fix`
	`git switch <branch-name>` switch to other branch. eg: `git switch bug-fix`
	`git checkout <branch-name>` can also switch to other branch but can do more thing. see documents for detail
	`git switch -c <branch-name>` can create and switch to the new branch
	make sure stage every changes before switching the branch
	`git branch -d` delete the branch. `-D` is to forcefully delete unmerged branch
	`git branch -m` move and rename the branch. to rename you have to in the branch you want to rename
`git merge`
	change to the destination branch
	`git merge bugfix`
`git diff` show all changes in our working directory that NOT staged for the next commit
	 ![[Pasted image 20240109200937.png|600]] 
	 `git diff HEAD` show all changes staged or un staged. all new in the working directory 
	 `git diff --staged` show only staged changes
	 `git diff HEAD [file-name]` show changes for specific file. eg `git diff HEAD style/main.css index.html`
	 `git diff branch1..branch2` compare changes between two branches
	 `git diff commit1..commit2`  eg. `git diff 4a9da7b..2912870`
 `git stash`.Stashing: Git provides an easy way of stashing these uncommitted changes so that we can return to the later, without having to make unnecessary commits
	 ![[Pasted image 20240109202955.png|400]] 
	 `git stash pop` remove the most recently stashed changes in you stash and re-apply them to your working copy
	 `git stash apply` take whatever's in the stash and apply it in the same way that pop does without removing it from the stash. This can be useful if you want to apply stashed changes to multiple branches
	if have multiple stashes `git stash list` list all stashes
		 `git stash apply stash@{2}`
		 `git stash drop stash@{2}`
`git checkout d8194d6` Change back to the old version of commit "d8194d6"
	the notification: detached HEAD. means HEAD points at that commit rater than at the branch pointer. HEAD refers to a branch NOT a specific commit
	when you in the old commit: you can go reattach the HEAD or create a new branch and switch to it
`git checkout HEAD~1` refers to the commit before HEAD
	`git checkout HEAD~2` refers to 2 commits before HEAD
	`git checkout HEAD <file>` to discard any changes in that file, reverting back to the HEAD. this is equal to `git checkout --<file>`
`git restore <file-name>` restore the file to the contents in the HEAD. Un-modifying files
	`git restore --source HEAD~1 app.js` 
`git restore --staged secretes.txt` un-stage the file
`git reset <commit-hash>` This will keep the changes in the working directory
	`git reset --hard <commit-has>` this will remove changes in the working directory
`git revert <commit-hash>` rest is deleting the commit entirely. revert is to create the new commit and this commit is to delete previous commit change. we keep the history
`git clone url` This will have the full history of the project which contain all commits and do not need to init. Make sure NOT in a repo

SSH Keys: you need to be authenticated on Github to do certain operations, like pushing up code from your local machine. You generate and configure an SSH key! Once configured, you can connect to Github without having to supply your username/password
`git remote add <name> url`
`git push <remote> <branch>`
