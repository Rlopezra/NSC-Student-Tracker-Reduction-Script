# NSC Student Tracker Reduction Script

I created a Python script to restructure the file to make the Student Tracker File manageable. It condenses  students  enrollment records so that there's only one enrollment record for each institution a student attended.

For example, instead of having a record for each semester I attended Evergreen Valley College:

|First Name|Last Name|Student ID|College Name|Term Start Date|Term End Date|College Sequence|Graduated?| CIP|Graduation Date|
-----------------------------------------------------------------------------------------------------------------------------
|Ronald    | Lopez   | 0000001 | Evergreen Valley| 8/12/2015 | 12/3/2015 | 1                |          |     |              |
|Ronald    | Lopez   | 0000001 | Evergreen Valley| 1/4/2016  | 5/15/2016 | 1                |          |     |              |
|Ronald    | Lopez   | 0000001 | Evergreen Valley| 1/4/2016  | 5/15/2016 | 1                |          |     |              |
|Ronald    | Lopez   | 0000001 | Evergreen Valley| 8/12/2016 | 12/3/2016 | 1                |          |     |              |
|Ronald    | Lopez   | 0000001 | Evergreen Valley| 1/4/2017  | 5/15/2017 | 1                |          |     |              |
|Ronald    | Lopez   | 0000001 | Evergreen Valley|           |           |                  |     Y    |111.1| 6/8/2017     |

The script will create a record that has the term start date of the first term and end date of the last term enrolled at EVC.

|First Name|Last Name|Student ID|College Name|Term Start Date|Term End Date|College Sequence|Graduated?| CIP|Graduation Date|
-----------------------------------------------------------------------------------------------------------------------------
|Ronald    | Lopez   | 0000001 | Evergreen Valley| 8/12/2015 | 5/15/2017 | 1                |     Y    |111.1| 6/8/2017     |


Instead of having a file that has 3 million records, I only have to deal with 40,000 - 60,000 records.

The only modification necessary to run this script is to change the input and output file directory.
If the student unique identifier is in the 'Your Unique Identifier' column, then change all instances of 'Requester Return Field' to 'Your Unique Identifier'.
 
If you need to install Python, I recommend using Anaconda which packages Python and its most popular modules such as Pandas, SciKit, Matplotlib, SeaBorn, and Numpy together. Just make sure you choose Anaconda for Python 3.6. You can run the script in either Jupyter Notebook or Spyder (if you’re using Anaconda).
 
https://www.continuum.io/downloads 
