import os
import json
from sklearn.model_selection import train_test_split
from collections import Counter

DATA_PATH= os.path.join(os.path.dirname(__file__), '..','data','raw','support_examples.jsonl')
TRAIN_PATH= os.path.join(os.path.dirname(__file__), '..','data','splits','training.jsonl')
VALIDATE_PATH= os.path.join(os.path.dirname(__file__), '..','data','splits','validate.jsonl')
TEST_PATH= os.path.join(os.path.dirname(__file__), '..','data','splits','test.jsonl')


with open(DATA_PATH, 'r') as f:
    data = list(map(json.loads, f.readlines()))

train_data, temp_data = train_test_split(data, random_state=42,
                                         test_size=0.3,
                                         stratify=[x['intent'] for x in data])

valid_data, test_data = train_test_split(temp_data, random_state=42,
                                         test_size=0.5,
                                         stratify=[x['intent'] for x in temp_data])

print("Training Examples: ",len(train_data))
print("Training 'intent': \n",Counter(x['intent'] for x in train_data))
print('-'*75)
print("Valid Examples: ",len(valid_data))
print("Valid 'intent': \n",Counter(x['intent'] for x in valid_data))
print('-'*75)
print("Test Examples: ",len(test_data))
print("Test 'intent': \n",Counter(x['intent'] for x in test_data))

with open(TRAIN_PATH, 'w', encoding='utf-8') as f:
    for data in train_data:
        record = json.dumps(data)
        f.write(record + '\n')

with open(VALIDATE_PATH, 'w', encoding='utf-8') as f:
    for data in valid_data:
        record = json.dumps(data)
        f.write(record + '\n')

with open(TEST_PATH, 'w', encoding='utf-8') as f:
    for data in test_data:
        record = json.dumps(data)
        f.write(record + '\n')

