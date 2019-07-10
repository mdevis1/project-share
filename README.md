# project-share
1 - Manual Reading App (February 2019 - May 2019 ) (in collaboration with another collegaue):
A program written entirely in Python, which gives to the user the ability
to process a large quantity of readings from remote electrical meters (
.csv format in input) through a GUI. The user has the option to clean,
reorder, select, modify or transform the data to xlsx or json format , and
send the processed file
to a real-time energy management platform. The program uses different
libraries, such as pandas, numpy, json, tkinter, PIL, etc.

2 - Regular Expression
A program written entirely in Python, which gives to the user the ability to find particular regular expression or pattern and extract those data.

3 - Traffic Violations Tracker - Python Class
Data: https://catalog.data.gov/dataset/traffic-violations-56dda

Problem: A large, crowded dataset of traffic violations taken from the county of Montgomery in Maryland. 

Solution: Finding correlations between traffic violations, time of day, and type of violation as well as visualizing results to create efficiency in reading the information. The program also recommends improved policies to the district with the most violations or to the state.

Instructions: Simply running the code every time the dataset is updated will give visual results.

Step 0: Since the dataset is large, we took only the first 10k rows for debugging purposes. We also clean the database. (File Step 0)
•	Plotting the distribution of violation per district by SubAgency chart (File Step 0, Feature #1) and also File Step 0-1
•	Plotting the distribution of violations resulting in an accident relative to time of occurrence (File Step 0, Feature #2)
	Recommendation: Increase traffic enforcement agents in the county between 	the rush hour (3 - 6 pm). 
Step 1: Finds the number of seat belt violations per district. 
Recommendation: Educate the public about wearing seat belts and increase traffic cameras in the district with the highest number.  (File Step 1)

Step 2: Finds the number of alcohol violations per district. 
Recommendation: Increase police checkpoints for the district with the highest number and enforce stricter jail time laws all over the state. (File Step 2)

Step 3: Finds the number of alcohol violations / (commented is the belt violations) per time of the day. 
Recommendation: Increase police checkpoints for the district with the highest number and enforce stricter jail time laws during that time. (File Step 3)

Step 4: Output heat maps of areas with alcohol violations. 
Recommendation: Increase traffic cameras in locations pinpointed to promote increased awareness for drivers. (File Step 4)
Step 5: Output heat maps of areas with seat belt violations. 
Recommendation: Increase traffic cameras in locations pinpointed to promote increased awareness for drivers. (File Step 5)

