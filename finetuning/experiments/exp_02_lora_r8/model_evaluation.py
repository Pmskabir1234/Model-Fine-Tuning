import sys
from pathlib import Path

# Set the repo root explicitly
PROJECT_ROOT = Path(r"C:\Users\saaad kabir\Desktop\Fine Tunnig\finetuning").resolve()
SRC_DIR = PROJECT_ROOT / "src"

if not SRC_DIR.exists():
    raise FileNotFoundError(f"Could not find project root containing 'src': {PROJECT_ROOT}")

sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(SRC_DIR))

from src import task_definition
from src import output_parser
from src.evaluation_func import evaluate_prediction
import json

EVAL_DATA = Path(__file__).resolve().parent / "eval_pred.jsonl"

with open(EVAL_DATA, 'r') as f:
    pred_samples = list(map(json.loads, f.readlines()))

correct_intent = 0
correct_priority = 0
correct_format = 0

for sample in pred_samples:
    details = evaluate_prediction(sample['prediction'], sample['expected_intent'], sample['expected_priority'])
    if details['format_valid']:
        correct_format += 1
    if details['intent_correct']:
        correct_intent += 1
    if details['priority_correct']:
            correct_priority += 1

print('Total Samples: ', len(pred_samples))
print(f'Total valid formats: {correct_format} Percentage(%): {round(correct_format/len(pred_samples),2)}')
print(f'Total correct intents: {correct_intent} Percentage(%): {round(correct_intent/len(pred_samples),2)}')
print(f'Total valid formats: {correct_priority} Percentage(%): {round(correct_priority/len(pred_samples),2)}')

    
