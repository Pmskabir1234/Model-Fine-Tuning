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

    if prediction is None or expected_intent is None or expected_priority is None:
            raise ValueError("Missing required arguments: predictions, expected_intents, and expected_priorities must be provided.")
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


def evaluate_macro_f1(
        predictions=None,
        expected_intents=None,
        expected_priorities=None,
                     ):

    if predictions is None or expected_intents is None or expected_priorities is None:
        raise ValueError("Missing required arguments: predictions, expected_intents, and expected_priorities must be provided.")

    parsed_intents = []
    parsed_priorities = []
    for pred in predictions:
        parsed = parse_output(pred)
        parsed_intents.append(parsed['intent'])
        parsed_priorities.append(parsed['priority'])

    y_true_intent = [val if val is not None else "unknown" for val in expected_intents]
    y_pred_intent = [val if val is not None else "unknown" for val in parsed_intents]

    y_true_priority = [val if val is not None else "unknown" for val in expected_priorities]
    y_pred_priority = [val if val is not None else "unknown" for val in parsed_priorities]

    try:
        from sklearn.metrics import f1_score
        intent_f1 = f1_score(y_true_intent, y_pred_intent, average='macro', zero_division=0.0)
        priority_f1 = f1_score(y_true_priority, y_pred_priority, average='macro', zero_division=0.0)
    except ImportError:
        def _calc_macro_f1(y_true, y_pred):
            if not y_true:
                return 0.0
            classes = set(y_true).union(set(y_pred))
            if not classes:
                return 0.0
            f1_scores = []
            for c in classes:
                tp = sum(1 for t, p in zip(y_true, y_pred) if t == c and p == c)
                fp = sum(1 for t, p in zip(y_true, y_pred) if t != c and p == c)
                fn = sum(1 for t, p in zip(y_true, y_pred) if t == c and p != c)
                precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
                recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
                f1_scores.append(f1)
            return sum(f1_scores) / len(f1_scores)

        intent_f1 = _calc_macro_f1(y_true_intent, y_pred_intent)
        priority_f1 = _calc_macro_f1(y_true_priority, y_pred_priority)

    return {
        "intent_macro_f1": intent_f1,
        "priority_macro_f1": priority_f1
    }


