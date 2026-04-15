# Why venv is better than `pip install` to system Python?
# Answer: venv is better than `pip install` to system Python because it isolates the project's dependencies from the system's dependencies.
# This means that you can install different versions of the same package for different projects without affecting each other.
# This is important because it allows you to use different versions of the same package for different projects, and it also allows you to use different versions of the same package for different versions of the same package.

#  ------------- Some more details -------------


#  What is the main risk of installing many Python packages with `pip` into the system Python on a shared laptop used for DevOps work?
#  Answer: The main risk of installing many Python packages with `pip` into the system Python on a shared laptop used for DevOps work is that it can break the system's dependencies.

# What does `python -m venv .venv` create, in plain language?
# It just creates a virtual env for that particular project allowing installing dependencies particular to that project. 

# After activating a venv, which `python` runs when you type `python` in that terminal — system or venv?
# The venv's python.

# You clone a repo that has `requirements.txt` but no `.venv`. What two-step process do you use before running the project’s scripts?
# 1. Create a venv
# 2. Install the dependencies

# True/False ?: You should commit the entire `.venv` folder to Git so teammates get the same packages automatically.
# False. You should commit the `requirements.txt` file to Git so teammates get the same packages automatically.
# Because the venv folder is specific to the project and the dependencies are specific to the project.
# If you commit the venv folder, it will be specific to the project and the dependencies will be specific to the project.
# If you commit the requirements.txt file, it will be specific to the project and the dependencies will be specific to the project.
# If you commit the venv folder, it will be specific to the project and the dependencies will be specific to the project.

#  ------------- Some more details -------------


