# Setting up Git for submissions


1. Install Git on your system (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

1. Sign up for GitHub (https://github.com/).

1. Go to https://education.github.com/ and sign up for the Student Developer Pack to get unlimited private repositories. You are a "student" and you want an "individual account". Once you have completed these first steps, you are then ready to create your private GitHub repository for this class.

1. Locally on your machine, clone this repository: `git clone git@github.com:sdobnik/aics-project.git`. This will create a copy of the repository on your own computer.

1. On the GitHub website, log in and create a **private** remote repository called *aics-project*. Make sure that the box Initialize this repository with a README is **unticked**. Ignore Quick setup instructions on the following page.

1. Add me (*sdobnik*) as a collaborator for this repository (check out settings on the repo website). If you are setting up a repository for your group, then also add all your other group members are collaborators.

1. Back in the terminal, set the origin of the repository that you cloned from me to be your remote repository that you just made. Change USERNAME below to your username. This tells git which remote repository to push your changes to when you `git push`. Enter the following command `git remote set-url origin https://github.com/USERNAME/aics-project.git`.

1. Now you are ready to start working on your repository using the standard procedure: `git pull`, `git add lab1`, `git commit -am "Project draft."`, `git push` (sometimes `git push remote origin`).

1. Check that the files have been updated in your remote github repository by navigating to https://github.com/USERNAME/aics-project (change USERNAME to your username)



## Submitting your work

1. Let us know through Canvas submission when you would like to submit your project, inclusing a commit id, e.g. `c310619433ab7210fd1106d6061a3abb6aecdac2` which you get by typing `git log`.

1. We will provide comments in the `README.md` in the Github folder. Try to keep all information there and on Canvas discussion forums (rather than random email messages) as this will be helpful to keep track of ideas when it comes times to wrote the report. Use `README.md` for keeping a working plan or table of contents for your project. You are encoraged to take notes of your results as you run the experiments that we can discuss with you. For this please create a `notes` folder where you can save your notes as individual [Markdown files](https://guides.github.com/features/mastering-markdown/) (just like this one).

1. Note that GitHub cannot host individual files that are larger than 100 MB and repositories larger than 1GB. If you try to push a file larger than this, GitHub will complain. You can upload such files (which will be corpora and supplementary data) to our Box folder. Contact me for details.


The guide has been adapted from https://github.com/rlbarter/stat215a
