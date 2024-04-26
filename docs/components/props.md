```python exec
from pcweb.pages.docs.library import library
from pcweb.pages.docs import state, vars
import reflex as rx
from pcweb.quiz.quiz import quiz_component
```

# Props

Props modify the behavior and appearance of a component. They are passed in as keyword arguments to the component function.

## Component Props

Each component has props that are specific to that component. For example, the `rx.avatar` component has a fallback prop that sets the `fallback` of the avatar.

```python demo
rx.avatar(
    fallback="JD"
)
```

Check the docs for the component you are using to see what props are available.

```md alert success
# Reflex has a wide selection of [built-in components]({library.path}) to get you started quickly.
```

## HTML Props

Components support many standard HTML properties as props. For example: the HTML [id]({"https://www.w3schools.com/html/html_id.asp"}) property is exposed directly as the prop `id`. The HTML [className]({"https://www.w3schools.com/jsref/prop_html_classname.asp"}) property is exposed as the prop `class_name` (note the Pythonic snake_casing!).

```python demo
rx.box(
    "Hello World",
    id="box-id",
    class_name=["class-name-1", "class-name-2",],
)
```

## Binding Props to State

Reflex apps can have a [State]({state.overview.path}) that stores all variables that can change when the app is running, as well as the event handlers that can change those variables.

State may be modified in response to things like user input like clicking a button, or in response to events like loading a page.

State vars can be bound to component props, so that the UI always reflects the current state of the app.

```md alert warning
Optional: Learn all about [State]({state.overview.path}) first.
```

You can set the value of a prop to a [state var]({vars.base_vars.path}) to make the component update when the var changes.

Try clicking the badge below to change its color.

```python demo exec
class PropExampleState(rx.State):
    text: str = "Hello World"
    color: str = "red"

    def flip_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"


def index():
    return rx.badge(
        PropExampleState.text,
        color_scheme=PropExampleState.color,
        on_click=PropExampleState.flip_color,
        font_size="1.5em",
        _hover={
            "cursor": "pointer",
        }
    )
```

In this example, the `color_scheme` prop is bound to the `color` state var.

When the `flip_color` event handler is called, the `color` var is updated, and the `color_scheme` prop is updated to match.


## Try out some challenges


```python exec
questions = [
    {
        "id": 0,
        "question_type": "single_choice",
        "question_body": "What is the purpose of 'props' in Reflex components?",
        "question_image": None,
        "options": [
            "To modify the behavior and appearance of a component",
            "To provide database access",
            "To configure the server settings",
            "To enhance the security of the application"
        ],
        "correct_answers": ["To modify the behavior and appearance of a component"]
    },
    {
        "id": 1,
        "question_type": "multiple_choice",
        "question_body": "Which of the following are examples of props in Reflex?",
        "question_image": None,
        "options": [
            "fallback in rx.avatar",
            "id in rx.box",
            "port number in server configuration",
            "class_name in rx.box"
        ],
        "correct_answers": ["fallback in rx.avatar", "id in rx.box", "class_name in rx.box"]
    },
    {
        "id": 2,
        "question_type": "single_choice",
        "question_body": "What happens when you bind a state variable to a prop in Reflex?",
        "question_image": None,
        "options": [
            "The server restarts.",
            "The UI component updates when the state variable changes.",
            "The component is removed from the UI.",
            "It triggers a download of the component."
        ],
        "correct_answers": ["The UI component updates when the state variable changes."]
    },
    {
        "id": 3,
        "question_type": "true_false",
        "question_body": "In Reflex, standard HTML properties cannot be used as props for components.",
        "question_image": None,
        "options": ["True", "False"],
        "correct_answers": ["False"]
    },
    {
        "id": 4,
        "question_type": "single_choice",
        "question_body": "Which property in the given example is bound to the state variable 'color'?",
        "question_image": None,
        "options": [
            "color_scheme",
            "font_size",
            "on_click",
            "_hover"
        ],
        "correct_answers": ["color_scheme"]
    }
]
```

```python eval
quiz_component(questions)
```