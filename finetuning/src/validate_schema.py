"""
The example for model training will be in the given format:
example = {
    "id": "support_000001",

    "messages": [
        {
            "role": "user",
            "content": "I forgot my password and can't log in.",
        },
        {
            "role": "assistant",
            "content": (
                "INTENT: password_reset\n"
                "PRIORITY: medium\n"
                "ACTION: Provide password reset instructions"
            ),
        },
    ],

    "intent": "password_reset",
    "priority": "medium",
}
"""

from task_definition import ALLOWED_INTENTS, ALLOWED_PRIORITIES
import os
import json

EXAMPLE_PATH = os.path.join(os.path.dirname(__file__),"..","data", "raw", "support_examples.jsonl")

def validate_example(example):
    errors = []

    if not example.get('id'):
        errors.append("missing id")

    if not isinstance(example.get("messages"), list):
        errors.append("messages_not_list")

    if len(example.get('messages',[])) != 2:
        errors.append("invalid_message_count")

    if example.get('intent') not in ALLOWED_INTENTS:
        errors.append("invalid_intent")

    if example.get('priority') not in ALLOWED_PRIORITIES:
        errors.append('invalid_priority')

    return errors


with open(EXAMPLE_PATH, "r") as f:
    examples = list(map(json.loads, f.readlines()))



def formating_to_canonical(examples):
    formatted_examples = []
    for example in examples:
        assistant_content = (
            f"INTENT: {example.get('intent')}\n"
            f"PRIORITY: {example.get('priority')}\n"
            f"ACTION: {example.get('action')}"
        )
        formatted = {
            'id': example.get('id'),
            'messages': [
                {'role': 'user', 'content': example.get('input')},
                {'role': 'assistant', 'content': assistant_content}
            ],
            'intent': example.get('intent'),
            'priority': example.get('priority')
        }
        formatted_examples.append(formatted)
    return formatted_examples

examples_formatted = formating_to_canonical(examples)

all_errors = []
for example in examples_formatted:
    err = validate_example(example)
    if err:
        all_errors.append((example.get('id'), err))

print(f"Total examples validated: {len(examples_formatted)}")
print(f"Total validation errors: {len(all_errors)}")
if all_errors:
    print("Sample errors:", all_errors[:5])