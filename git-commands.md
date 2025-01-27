# Quick Start Git Commands Guide

# 1. Clone a repository to your local machine
git clone <repository_url>
# Example: git clone https://github.com/username/repo.git

# 2. Check the current status of your repository
git status
# Shows the changes in the working directory, staging area, and any untracked files.

# 3. Add files to the staging area
git add <file_name>
# Example: git add myfile.txt
# To add all files: git add .

# 4. Commit changes to the local repository
git commit -m "Your commit message"
# Use meaningful messages to describe changes.

# 5. Push changes to the remote repository
git push
# Pushes the committed changes to the branch in the remote repository.

# 6. Pull the latest changes from the remote repository
git pull
# Fetches and integrates changes from the remote repository.

# 7. Create a new branch
git branch <branch_name>
# Example: git branch feature/new-feature

# 8. Switch to another branch
git checkout <branch_name>
# Example: git checkout feature/new-feature

# 9. Create a new branch and switch to it
git checkout -b <branch_name>
# Example: git checkout -b feature/new-feature

# 10. Merge a branch into the current branch
git merge <branch_name>
# Example: git merge feature/new-feature
# Always resolve conflicts if they arise.

# 11. View the commit history
git log
# Shows the history of commits in the repository.

# 12. Delete a branch locally
git branch -d <branch_name>
# Example: git branch -d feature/new-feature

# 13. Set up a remote repository if not already done
git remote add origin <repository_url>
# Example: git remote add origin https://github.com/username/repo.git

# 14. Check remote repository details
git remote -v
# Lists the URLs of the remote repository.

# 15. Revert a file in the working directory to the last committed state
git checkout -- <file_name>
# Example: git checkout -- myfile.txt

# 16. Discard all local changes (not yet staged) in the working directory
git reset --hard
# Be cautious: This will discard all changes!

# 17. Stash changes for later
git stash
# Saves your uncommitted changes temporarily.
git stash apply
# Reapplies the stashed changes.

# 18. Check your configured user info
git config --list
# Shows all Git configuration.

# 19. Set or change your Git username and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Tips:
# - Always pull changes before starting work: git pull
# - Keep your commit messages clear and concise.
# - Use branches for new features or bug fixes.

