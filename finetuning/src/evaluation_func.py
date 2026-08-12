"""
we have to make sure that format is correct, generated intent and priority 
matches with the expected. Also we should notice the phrasing genearted as action. 
"""
from output_parser import parse_output, is_valid_format

def evaluate_prediction(
        prediction,
        expected_intent,
        expected_priority
                        ):

    parsed = parse_output(prediction)
    format_valid = is_valid_format(parsed)

    intent_correct = (parsed['intent'] == expected_intent)
    priority_correct = (parsed['priority'] == expected_priority)

    return {
        "parsed":parsed,
        "format_valid":format_valid,
        "intent_correct":intent_correct,
        "priority_correct":priority_correct
    }

prediction = """INTENT: password_reset
PRIORITY: medium
ACTION: Provide password reset instructions"""

result = evaluate_prediction(prediction,
                             expected_intent='password_intent',
                             expected_priority='high')

print(result)