import pyexcel

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

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="test.xls")