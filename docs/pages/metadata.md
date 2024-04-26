```python exec

import reflex as rx
from pcweb.quiz.quiz import quiz_component

meta_data = (
"""
@rx.page(
    title='My Beautiful App',
    description='A beautiful app built with Reflex',
    image='/splash.png',
    meta=meta,
)
def index():
    return rx.text('A Beautiful App')

@rx.page(title='About Page')
def about():
    return rx.text('About Page')


meta = [
    {'name': 'theme_color', 'content': '#FFFFFF'},
    {'char_set': 'UTF-8'},
    {'property': 'og:url', 'content': 'url'},
]

app = rx.App()
"""  

)

```

# Page Metadata

You can add page metadata such as:

- The title to be shown in the browser tab
- The description as shown in search results
- The preview image to be shown when the page is shared on social media
- Any additional metadata

```python
{meta_data}
```

```python exec
questions = [
    {
        "id": 0,
        "question_type": "single_choice",
        "question_body": "What is the purpose of the '@rx.page' decorator in Reflex?",
        "question_image": None,
        "options": [
            "To define a new class",
            "To declare a function as a webpage",
            "To import a module",
            "To update the app's settings"
        ],
        "correct_answers": ["To declare a function as a webpage"]
    },
    {
        "id": 1,
        "question_type": "multiple_choice",
        "question_body": "Which attributes can be included in the page metadata in Reflex?",
        "question_image": None,
        "options": [
            "Title",
            "Description",
            "Preview Image",
            "Content Type"
        ],
        "correct_answers": ["Title", "Description", "Preview Image"]
    },
    {
        "id": 2,
        "question_type": "single_choice",
        "question_body": "What does the 'meta' list define in the Reflex app?",
        "question_image": None,
        "options": [
            "The list of pages in the app",
            "The server-side configurations",
            "Additional metadata for the webpage",
            "CSS styles for the app"
        ],
        "correct_answers": ["Additional metadata for the webpage"]
    },
    {
        "id": 3,
        "question_type": "single_choice",
        "question_body": "In Reflex, what is the function of the 'rx.text' method shown in the examples?",
        "question_image": None,
        "options": [
            "To write text to the server log",
            "To display text on a webpage",
            "To configure the app settings",
            "To send text to the database"
        ],
        "correct_answers": ["To display text on a webpage"]
    },
    {
        "id": 4,
        "question_type": "multiple_choice",
        "question_body": "What information can be specified in the '@rx.page' decorator?",
        "question_image": None,
        "options": [
            "Function name",
            "Page title",
            "Page description",
            "Meta tags"
        ],
        "correct_answers": ["Page title", "Page description", "Meta tags"]
    }
]

```

```python eval
quiz_component(questions)
```