#! /usr/bin/env python3

import psycopg2

if __name__ == '__main__':
q1_result = {}
q1_result['question'] = "\t1.The three most popular articles of alltime :\n"
q2_result = {}
q2_result['question'] = "\t2.The most popular article authors of alltime:\n"
q3_result = {}
q3_result['question'] = """\t3.Number of days with more than 1percent of
                        requests that lead to an error:\n"""

q1 = "select title,t_views from newt limit 3;"

q2 = """select authors.name,sum(newt.t_views) as t_views from authors,newt
where newt.author=authors.id group by authors.name order by t_views desc;"""

q3 = "select* from error_view where \"Perror\">1.00;"

# fucntion to execute the querys


def get_query(query):
    dbase = psycopg2.connect(database='news')
    cursor = dbase.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    dbase.close()
    return results


# funtion to display results for query 1 and 2
def display_results(q_result):
    print(q_result['question'])
    for i in q_result['result']:
        print(str(i[0]) + '=' + str(i[1]) + 'views')


# fetch the results
q1_result['result'] = get_query(q1)
q2_result['result'] = get_query(q2)

# pass the results for q1 and q2 in display function to print them
display_results(q1_result)
display_results(q2_result)


def display_q3_results(q_result):
    print(q_result['question'])
    for i in q_result['result']:
        print(str(i[0]) + '=' + str(i[1]) + '%')


q3_result['result'] = get_query(q3)
# pass the result for q3 in display function to print them
display_q3_results(q3_result)
