
questions = [
    {
        "id": 0,
        "question_type": "multiple_choice",
        "question_body": "Which of the following are types of variables in a Reflex State?",
        "question_image": None,
        "options": ["Base Var", "Computed Var", "Dynamic Var", "Static Var"],
        "correct_answers": ["Base Var", "Computed Var"]
    },
    {
        "id": 1,
        "question_type": "single_choice",
        "question_body": "What type of function is used to modify base variables in Reflex?",
        "question_image": None,
        "options": ["Event Handler", "Computed Function", "Event Trigger", "State Method"],
        "correct_answers": ["Event Handler"]
    },
    {
        "id": 2,
        "question_type": "multiple_choice",
        "question_body": "Which operators are supported by Reflex for performing operations on vars?",
        "question_image": None,
        "options": ["+", "to_string()", "reverse()", "substring()"],
        "correct_answers": ["+", "to_string()", "reverse()"]
    },
    {
        "id": 3,
        "question_type": "single_choice",
        "question_body": "What does the @rx.cached_var decorator indicate about a var?",
        "question_image": None,
        "options": ["It is updated every time the state changes", "It is never updated", "It is only recomputed when dependent vars change", "It can be directly set by event handlers"],
        "correct_answers": ["It is only recomputed when dependent vars change"]
    },
    {
        "id": 4,
        "question_type": "multiple_choice",
        "question_body": "Which statements are true about base vars in Reflex?",
        "question_image": None,
        "options": ["They can be modified directly by event handlers", "They must be JSON serializable", "They are automatically recomputed", "They can store backend-only data"],
        "correct_answers": ["They can be modified directly by event handlers", "They must be JSON serializable"]
    }
]