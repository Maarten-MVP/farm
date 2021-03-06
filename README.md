Hi Winc Academy,

I think I got to the solution in a different way then the assignment proposes. I hope the result is correct. Please find below an explanation how I went about it:

Key components in my solution:

1) GitHub Action

    The GitHub action runs a serie of commands "on push", meaning everytime a push is made to the repository. The order of the commands is important:
    1) install requirements (pip, flask, ...) to make sure the host can run the tests
    2) run tests 
    3) auto deploy: a short .sh file that does everything to put the changes online

    If point 2 fails, the actions is returned as an error and the process is stopped, meaning, auto deploy is not executed.

2) Self hosted runner

    By configuring a self hosted runner in the GitHub actions, I don't need to execute login commands. By using my VPS as a "runner", the project files are updated with every action run in the "action-runner" folder (/root/action-runner/_work/farm/farm)

3) Gunicorn .service file

    The Gunicorn .service file makes it possible to very easily reload the service and get the new changes running. 

Key problems:

1) the Gunicorn .service file didn't want to run when my working directory was a /root/ folder 

    I came to this conclusion when I tried everything and it worked with other directories, but not directly from the project folder created by GitHub actions. 

    Solution: I created a new project folder in /home/ and added a .sh file as the last step in the GitHub action. This .sh file copies the files from the directory in the root to my new project folder in /home/.

2) Self hosted runner loses conenction to GitHub when your pc goes offline

    If you follow the steps on GitHub (settings -> actins -> create self hosted runner), you end with a ./run.sh command. But this command is not a permanent run and goes offline when you close your CMD or restart your pc. 

    Solution: instead of executing the ./run.sh file you can use another file in the action-runner folder: ./svc.sh
    This file needs to be run in sudo, installed and started:
    sudo ./svc.sh install
    sudo ./svc.sh start
    sudo ./svc.sh stop (to stop the connection with GitHub actions)