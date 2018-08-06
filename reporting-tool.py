#!/usr/bin/env python3
# log analysis project which build informative summry
# from database contains newspaper articles as well as
# web server log for the site
# done by : Nadia Al shezawy

import psycopg2

DBNAME = "news"

# Data Base queries

# question 1 querey , return most popular three articles
popular_articles = """
    select articles.title, COUNT(*) as view
    from log
    join articles
    ON articles.slug=SUBSTRING(log.path ,POSITION('article/' IN log.path)+8)
    Group by title
    order by view Desc
    limit 3"""

# question 2 querey , retunr most popular authors
popular_authors = """
    select authors.name, count(*) as view
    from log
    join articles
    ON articles.slug=SUBSTRING(log.path ,POSITION('article/' IN log.path)+8)
    join authors
    on authors.id=articles.author
    group by authors.name
    order by view desc"""

# question 3 querey , return which day error was more thatn 1%
error_rate = """
    select day , error
    from log3
    where error > .01"""


# a method for sql query
def DB_query(query_msg):

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_msg)
    posts = c.fetchall()
    db.close()
    return posts


# Return The most three articles and print result
def most_popular_articles():

    articles = DB_query(popular_articles)
    print "\nThe most popular articles are :\n"
    for title, views in articles:
        print(" \"{}\" -- {} views".format(title, views))


# Return The most popular author and print result
def most_popular_authors():

    authors = DB_query(popular_authors)
    print "\nThe most popular authorss are :\n"
    for name, views in authors:
        print(" \"{}\" -- {} views".format(name, views))


# Return The day with error more than 1 %
def day_error():

    error = DB_query(error_rate)
    print "\nDays with more than 1% error:\n"
    for day, rate in error:
        print("""{0:%B %d, %Y}--{1:.2f} % errors""".format(day, 100*rate))


# calling the three function
most_popular_articles()
most_popular_authors()
day_error()
