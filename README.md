# Local-Server-File-Storage app

 - This is a simple file storer created using flask. 
 
 - This project is a similar to other online file storage app ,e.g:- google drive,dropbox ,etc
 
 - Everyone can run run this on localserver or  can host this online.
 
 - Feel free to contribute and bring changes in this project.   


# Install the neccessary libraries and modules
 - Activate your virtualenv and run the following command in your terminal(LINUX) or cmd(WINDOWS)
 
   $ pip3 install -r requirements.txt


# Creating the database

 - Create a database --> DATA
 
 - Execute the commands from DATA.sql to mysql to create the table.
 
# Running the app on your localhost

 - Open terminal or cmd and write the following command.
 
 - $ python3 main.py
 
# --------Important---------

- open main.py, at the ver end you will find "app.run(host = '192.168.43.155')" , '192.168.43.155' is my ip.

- you can replace this "app.run(host = '192.168.43.155')" with "app.run()" to run it on localhost.

- To use this locally on your phone you can use "app.run(host= your-ip)", to get your ip run the following command.

  --> In linux , open terminal:
  
      $ ifconfig , you will get your ip.
  
  --> In windows, open cmd:
      
      $ ipconfig , you will get your ip.
  
