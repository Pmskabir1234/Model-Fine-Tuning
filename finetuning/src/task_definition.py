ALLOWED_INTENTS = {
    "password_reset",
    "billing_issue",
    "account_aompromise",
    "refund_request",
    "technical_problem",
    "feature_request",
    "account_closure",
}

ALLOWED_PRIORITIES = {
    "high",
    "medium",
    "low"
}

OUTPUT_FIELDS = {
    "INTENT",
    "PRIORITY",
    "ACTION"
}

TASK_DESCRIPTION = """
Given a technical  support request, generate a structured response
containing intent, priority, and recommended action.
"""

