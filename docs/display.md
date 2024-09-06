## Sariah's idea for an interactive GUI in Python
Hi y'all. Because we need an interactive GUI in Python that runs on Linux, I have started by creating a small file that uses GTK that should run smoothly on Ubuntu (or other distros hopefully). To get set up for now (in the future we should have a shell script that should install all dependencies in one go) the two most important packages are libgtk-4-1 and libgtk-4-dev. On Ubuntu, you should have Python installed by default but if not you'll need that too obviously. If you aren't familiar, the command you will need to run is "sudo apt-get" ___. Then, you can run "python3 main.py" in your terminal and see a box that will be the start of our GUI!

# Documentation
https://www.gtk.org/docs/installations/linux/
https://github.com/Taiko2k/GTK4PythonTutorial 