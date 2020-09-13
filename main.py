import pyexcel as p

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
    print("%s is aged at %d and works as a %s developer" % (record['Name'], record['Age'], record['Job']))