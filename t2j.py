# Extract text from a txt file and convert it to JSON format
# Author: Arthr K. Kyagulanyi

import json


def main():
    # Open the file
    with open('textt.txt', 'r') as f:
        # Read the file
        text = f.read()

    # Split the text into a list of sentences
    sentences = text.split('.')

    # Create a list of dictionaries
    data = []
    for sentence in sentences:
        # Create a dictionary
        d = {'sentence': sentence}
        # Append the dictionary to the list
        data.append(d)

    # Create a JSON string
    json_string = json.dumps(data, indent=4)

    # Write the JSON string to a file
    with open('data.json', 'w') as f:
        f.write(json_string)


if __name__ == '__main__':
    main()


