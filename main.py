import os
from pandas import read_csv, merge


# associating data frames to correct files (only works if there is the two files needed in and nothing else)
files = os.listdir()
for file in files:
    if file.endswith(".csv"):
        if file.find("Followers") >= 0:
            followers = read_csv(file)["profileUrl"]
        else:
            following = read_csv(file)["profileUrl"]
            
            
# extracting who i am following but isn't following me back
difference = merge(following, followers, how="outer", indicator=True).query('_merge=="left_only"')["profileUrl"]
print(difference)




# choose to delete files after use
while True:
    ans = input("Do you want to delete files? (yes/no): ")
    if ans.lower() in ["yes", "y"]:
        print("Files deleted")
        for file in files:
            if file.endswith(".csv"):
                os.remove(file)
        break
    elif ans.lower() in ["no", "n"]:
        print("Files kept")
        break
    else:
        print("Invalid input. Please enter yes/no.")
        
        