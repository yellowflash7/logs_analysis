# logs_analysis

About
==========
Reporting tool to analyze the database and present a log report.

How to Run
==========

* Install vagrant and virtualbox
* Clone this repository in your vagrant directory  https://github.com/udacity/fullstack-nanodegree-vm.
* Clone the files from this repository in you vagrant directory
* Download the database from here and place the files in vagrant directory https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
* Run the following commands 

1. cd into your vagrant directory
2. vagrant up (get your virtual machine up and running)
3. vagrant ssh (login to your system)
4. psql -d news -f newsdata.sql   (Loads the databse)
5. psql -d news (connect to the database)

* create the following view

             * create view newt as select title,author,count(*) as t_views from articles,log where log.path like concat('%',articles.slug) 
              group by articles.title,articles.author order by t_views;

             * create view error_view as select date(time),round(100.0*sum(case log.status when '200 OK' then 0 else 1  
              end)/count(log.status),2) as "Perror" from log group by date(time) order by "Perror" desc;

* Browse into your vagrant directory and go in log_analysis
* Now the run log.py
