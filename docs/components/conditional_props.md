```python exec
import reflex as rx
from pcweb.quiz.quiz import quiz_component
```

# Conditional Props

Sometimes you want to set a prop based on a condition. You can use the `rx.cond` function to do this.

```python demo exec
class PropCondState(rx.State):

    value: list[int]
    
    def set_end(self, value: int):
        self.value = value


def cond_prop():
    return rx.slider(
        default_value=[50],
        on_value_commit=PropCondState.set_end,
        color_scheme=rx.cond(PropCondState.value[0] > 50, "green", "pink"),
        width="100%",
    )
```

```python exec

questions = [
    {
        "id": 0,
        "question_type": "single_choice",
        "question_body": "What function is used in Reflex to set a property based on a condition?",
        "question_image": None,
        "options": ["rx.set", "rx.cond", "rx.prop", "rx.config"],
        "correct_answers": ["rx.cond"]
    },
    {
        "id": 1,
        "question_type": "single_choice",
        "question_body": "What does the 'color_scheme' property of the slider depend on in the given code snippet?",
        "question_image": None,
        "options": ["The length of the value list", "The first element of the value being greater than 50", "The width of the slider", "The default value of the slider"],
        "correct_answers": ["The first element of the value being greater than 50"]
    },
    {
        "id": 2,
        "question_type": "multiple_choice",
        "question_body": "Which options correctly describe the use of the 'rx.cond' function in the code snippet?",
        "question_image": None,
        "options": ["It is used to change the color scheme of a widget", "It determines the method called on value commit", "It is used to configure the default value of the slider", "It sets the color based on the slider's value"],
        "correct_answers": ["It is used to change the color scheme of a widget", "It sets the color based on the slider's value"]
    },
    {
        "id": 3,
        "question_type": "single_choice",
        "question_body": "What type of component is being configured in the example code?",
        "question_image": None,
        "options": ["Button", "Slider", "Textbox", "Checkbox"],
        "correct_answers": ["Slider"]
    }
]

```


```python eval
quiz_component(questions)
```

