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

- neew to add this three view for part three question

```
    create log1
    create view  log1 as select DATE_TRUNC('day',log.time) as day,
    log.status,count(*) as request
    from log
    where status='200 OK'
    group by day,log.status
    order by day;```




```
    create view log2 as select DATE_TRUNC('day',log.time) as day,log.status,count(*) as error
    from log
    where log.status !='200 OK'
    group by day, log.status
    order by day;
```


```
    create view log3 as select log1.day as day,
    CAST(log2.error AS float)/CAST((log1.request+log2.error) As float) as error
    from log1
    join log2
    on log1.day=log2.day;
```

-change the directory to  python file location and run program using this command:

python reporting-tool.py




## Contributing

-The python file can be updated to answer more analysis questions of 
the database.

## Author
 Nadia Ahmed