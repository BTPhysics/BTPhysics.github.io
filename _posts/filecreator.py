numbers_of_topics = []
month = "10"
day = 1
for x in range(19):
    day_output = day + x
    day_output = str(day_output)
    f = open("_posts/2018-" + month + "-" + day_output + "-.md", "w+")
