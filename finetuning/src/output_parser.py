"""
Our format -
INTENT: <intent>
PRIORITY: <priority>
ACTION: <action

The order matters too.

We should not casually accept:
ACTION: ...
INTENT: ...
PRIORITY: ...

Because evaluation rules need to be determininstic.
"""
from task_definition import ALLOWED_INTENTS, ALLOWED_PRIORITIES

def parse_output(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    result = {
        "intent":None,
        "priority":None,
        "action":None
    }

    for line in lines:
        if line.startswith("INTENT:"):
            result['intent'] = line.split(":", 1)[1].strip()

        elif line.startswith("PRIORITY:"):
            result['priority'] = line.split(":", 1)[1].strip()

        elif line.startswith("ACTION:"):
            result["action"] = line.split(
                ":", 1
            )[1].strip()

    return result
        
# text = """INTENT: password_reset
# PRIORITY: medium
# ACTION: Provide password reset instructions"""


def valdating_priority(response : dict) -> bool:
    return response['priority'] in ALLOWED_PRIORITIES

def validating_intents(response: dict) -> bool:
    return response['intent'] in ALLOWED_INTENTS

# x = parse_output(text)
# print(x,end='\n')
# print(valdating_priority(x))
# print(validating_intents(x))

def is_valid_format(parsed):
    return(
        parsed['intent'] is not None
        and parsed['priority'] is not None
        and parsed['action'] is not None
        and validating_intents(parsed)
        and valdating_priority(parsed)
        and bool(parsed['action'].strip())
    )
# print(is_valid_format(x))