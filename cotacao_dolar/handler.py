import json

import pandas


def hello(event, context):
    table = pandas.DataFrame({'column': [1, 2, 3, 4, 5]})
    print(table) 

if __name__ == "__main__": 
    hello(None, None)