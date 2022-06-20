import pandas


def handler(event, context):
    table = pandas.DataFrame({'column': [1, 2, 3, 4, 5]})
    print(table)