import pyexcel as p

def write_and_read_xls():
    """ Make sure the .xls document is closed before running 
        this script. This function writes a list of dictionaries
        to edit the .xls file and than it reads the document
    """

    # Records that will be added to the .xls file
    a_list_of_dictionaries = [
    {
        "Name": 'Linus',
        "Age": 28,
        "Job": 'backend',
    },
    {
        "Name": 'Wozniak',
        "Age": 29,
        "Job": 'backend',
    },
    {
        "Name": 'Tesla',
        "Age": 30,
        "Job": 'devops',
    },
    {
        "Name": 'Mozart',
        "Age": 26,
        "Job": 'frontend',
    }
    ]

    # Edits .xls
    p.save_as(records=a_list_of_dictionaries, dest_file_name="test.xls")

    # Reads .xls's records
    records = p.iget_records(file_name="test.xls")
    for record in records:
        print("%s is %d years old and works as a %s developer" % (record['Name'], record['Age'], record['Job']))

write_and_read_xls()

def write_multiple_sheets():
    content = {
        'Sheet 1':
            [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0]
            ],
        'Sheet 2':
            [
                ['X', 'Y', 'Z'],
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]
            ],
        'Sheet 3':
            [
                ['O', 'P', 'Q'],
                [3.0, 2.0, 1.0],
                [4.0, 3.0, 2.0]
            ]
    }
    book = p.get_book(bookdict=content)
    book.save_as("output.xls")
    records = p.iget_records(file_name="output.xls")
    for record in records:
        print(record)

write_multiple_sheets()