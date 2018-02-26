# Dependencies
import json

# Read JSONs
sample = "Sample.json"

# Sample 1 Data
with open(sample) as data_file:
    sample_data = json.load(data_file)

    # Cleaned up JSON
    print(
        json.dumps(
            sample_data[0],
            sort_keys=True,
            indent=4,
            separators=(
                ',',
                ': ')))
    print("------------------------------------------------------------------")

    # Using the Sample_Data provided above, write code to answer each of the
    # following questions:

    # Question 1: With what account are the tweets in the Sample associated?
    # Question 2: How many followers does this account have associated with it?
    # Question 3: How many tweets are included in the Sample?
    # Question 4: How many tweets total has this account made?
    # Question 5: What was the text in the most recent tweet?
    #             Hint: You may need to look into "encding utf-8 in python"
    # Question 6: What was the text associated with each of the tweets
    #             included in this sample data?
    # Question 7 (Bonus): Which of the user's tweets was most frequently
    # retweeted? How many retweets were there?
