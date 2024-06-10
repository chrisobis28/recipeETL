Greetings Hello Fresh Team!
Here is the program I put together for the assignment I was given during the technical evaluation round! (2 hours)

Python version 3.12.4 and Pip 24.0 were used for creating this, even though other versions surely work as well for creation and verification. The modules imported can easily be installed and set-up using "pip install *", where * stands for the names of them: "pip install json", "pip install editdistance", "pip install csv", "pip install isodate".

Explanation of the code: the code defines a simple ETL (extract, transform, load) pipeline that prepares a dataset of recipes for further use, precisely filtering out those that do not contain "chilies" in their "ingredients" field and also assigns a difficulty level to all recipe instances. Imported from a JSON format [1] , the data is then loaded in a csv file.

[1] - I have a quick note to make here, the "recipes.json" file that was given to me had to be modified to match a JSON format of an array of objects (recipes in this case), therefore I have created "data_with_commas.json" with "[]" added and commas at the end of every row.

Thank you for your time and this great opportunity! Looking forward to your feedback!
Chris Obis, Data Engineering Intern Candidate