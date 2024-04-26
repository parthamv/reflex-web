```python exec
from pcweb.pages.docs import styling
import reflex as rx
from pcweb.quiz.quiz import quiz_component
```

# Style Props

In addition to component-specific props, most built-in components support a full range of style props. You can use any CSS property to style a component.

```python demo
rx.button(
    "Fancy Button",
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="white",
    opacity= 1,
    _hover={
        "opacity": .5,
    }
)
```

See the [styling docs]({styling.overview.path}) to learn more about customizing the appearance of your app.

```python exec
questions = [
    {
        "id": 0,
        "question_type": "multiple_choice",
        "question_body": "Which of the following CSS properties can be used to style a button component in Reflex?",
        "question_image": None,
        "options": ["border_radius", "box_shadow", "background_image", "href"],
        "correct_answers": ["border_radius", "box_shadow", "background_image"]
    },
    {
        "id": 1,
        "question_type": "single_choice",
        "question_body": "What is the effect of the '_hover' property in the provided Reflex button code?",
        "question_image": None,
        "options": ["Changes the button's opacity on click", "Changes the button's color on hover", "Changes the button's opacity on hover", "No effect"],
        "correct_answers": ["Changes the button's opacity on hover"]
    },
    {
        "id": 2,
        "question_type": "multiple_choice",
        "question_body": "Which of the following are valid style props for a Reflex component?",
        "question_image": None,
        "options": ["color", "opacity", "text_decoration", "href"],
        "correct_answers": ["color", "opacity"]
    }
]
```


```python eval
quiz_component(questions)
```