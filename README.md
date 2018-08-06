# Logs Analysis Project
The **logs analysis project** create a reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## Prerequisites
To run this project you need to install python, you'll need database software (provided by a Linux virtual machine) and the data (newsdata.sql) to analyze.

The database includes three tables:

-Authors table

-Articles table

-Log table

## Project content
The project have main python file and text file:

+reporting-tool.py :  the reporting tool answer the following questions.

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time? 
- On which days did more than 1% of requests lead to errors?

+result.txt : is a plain text file that is a copy of what python program printed out.



## How to run

-Go to the virtual machine program.

-Launch Vagrant VM by running : vagrant up

-you can log in with : vagrant ssh

-To load the data, use the command 
: psql -d news -f newsdata.sql 

-change the directory to  python file location and run program using this command:

python reporting-tool.py


## Contributing

-The python file can be updated to answer more analysis questions of 
the database.

## Author
 Nadia Ahmed