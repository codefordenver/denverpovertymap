## PUT YOUR INPUT STATEMENTS HERE


# PULL IN DATA
import csv
def pull_in_data(filename):
    with open(filename) as f:
        lis = [line.split() for line in f]        # create a list of lists
        for i, x in enumerate(lis):  
            if i > 1 and i < 66:
                print ("{0}".format(x))
    # put your code here to pull in the data
    # do some research to see how to pull in a CSV and use your resources if you need them
pull_in_data("./data.csv")


# CLEAN DATA
# def clean_data():
    # put your code here to clean the data



# if you want to test your f