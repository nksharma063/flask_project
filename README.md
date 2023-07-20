#Python Graded Assignment by Hero DevOps

 
##This repo will contain files below questions or problem statement
### Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password. 

### The program should continuously monitor the CPU usage of the local machine.

●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.

●       The program should run indefinitely until interrupted.

●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

### The program should read a configuration file (you can provide them with a sample configuration file).

●       It should extract specific key-value pairs from the configuration file.

●       The program should store the extracted information in a data structure (e.g., dictionary or list).

●       It should handle errors gracefully in case the configuration file is not found or cannot be read.

●       Finally save the output file data as JSON data in the database.

●       Create a GET request to fetch this information.

###Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

 

Sample Command:

python backup.py /path/to/source /path/to/destination

By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.





Steps Followed in the python files
****# Welcome to the flask_project wiki!****

## Project for login page, verify the cpu usage and using try and except.

### Created environment using venv, and three branches with name test, dev and main.

#### We will create one different .py files and app.py file and try to complete the graded assignment for usage. 

<h1><b>`_Password check_`</b></h1>
#### We have passed multiple if statement to check the condition give as per required Document, user can pass string which should contain digit, special character which is included in `_string.punctuation_` method, it should contain one upper and one lower.

#`_CPU check_`
## we have imported WMI library which is the closes to windows OS, put some filter such as if os is windows then it will convert the current directory to forward slash using '//', it will show us the value of utilization till interrupted by the user.

# Reading configuration file, [Please note that input in the API need be in http://locahost:5000/getData/[filenames.extension, filename.extension]]
##_It is designed in such a way that it should get two files in a row, i can remodified as well for just one file too if required_.

<h2>You can also call the getJSON() to get the output in JSON format on console as desired. However we have also implemented API with name <h1>`_getRequestConfig_`</h1> which will call the file and environment need to there, dependency is included in <h2>`_requirement.txt_`</h2>. We have first implemented <h1>readDirFIleLocation</h1>, get current working directory using getCWD and then iterate over path to get the precise string path to each file.
then we used extracted data in form of dict from <h1>extractdata(file)</h1> which will server the dict file <h1>getJSON()</h1> function in later function to save in mongo db and fetch from it and server it and serve as _json object_ to console or `_dict_` data to mongo db.</h2>

#Doing regular backups
we will get two dircteory location from user using directory fucntion.

Iterate over file using PATH.iter() and check if it matches then will use time methods to add the timestamp to archived file.
</body>
</html>
