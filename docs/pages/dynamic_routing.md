```python exec
import reflex as rx
from pcweb import constants, styles
from pcweb.quiz.quiz import quiz_component

dynamic_routes = (
"""
class State(rx.State):
    @rx.var
    def post_id(self) -> str:
        return self.router.page.params.get('pid', 'no pid')
        
@rx.page(route='/post/[pid]')
def post():
    \'''A page that updates based on the route.\'''
    return rx.heading(State.post_id)

app = rx.App()
"""
)


catch_all_route = (
"""
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        usernames = args.get('username', [])
        return f'Posts by {', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[...username]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()
"""  
)


optional_catch_all_route = (
"""
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        usernames = args.get('username', [])
        return f'Posts by {', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[[...username]]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()
"""  
)
```

# Dynamic Routes

Dynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible
and adaptable web applications. This section covers regular dynamic routes, catch-all routes,
and optional catch-all routes, each with detailed examples.

## Regular Dynamic Routes

Regular dynamic routes in Reflex allow you to match specific segments in a URL dynamically.

Example:

```python
{dynamic_routes}
```

In this case, a route like `/user/john/posts/5` would display "Posts by john: Post 5".

## Catch-All Routes

Catch-all routes in Reflex allow you to match any number of segments in a URL dynamically.

Example:

```python
{catch_all_route}
```

In this case, the `...username` catch-all pattern captures any number of segments after
`/users/`, allowing URLs like `/users/2/john/` and `/users/1/john/doe/` to match the route.

## Optional Catch-All Routes

Optional catch-all routes, enclosed in double square brackets (`[[...]]`). This indicates that the specified segments
are optional, and the route can match URLs with or without those segments.

Example:

```python
{optional_catch_all_route}
```

Optional catch-all routes allow matching URLs with or without specific segments.
Each optional catch-all pattern should be independent and not nested within another catch-all pattern.

```md alert
# Catch-all routes must be placed at the end of the URL pattern to ensure proper route matching.
```

### Routes Validation Table

| Route Pattern                                         | Example URl                                            |    valid |
|:------------------------------------------------------|:-------------------------------------------------------|---------:|
| `/users/posts`                                        | `/users/posts`                                         |    valid |
| `/products/[category]`                                | `/products/electronics`                                |    valid |                                                  |         |
| `/users/[username]/posts/[id]`                       | `/users/john/posts/5`                                  |    valid |
| `/users/[...username]/posts`                          | `/users/john/posts`                                    |  invalid |
|                                                       | `/users/john/doe/posts`                                |  invalid |
| `/users/[...username]`                                | `/users/john/`                                         |    valid |
|                                                       | `/users/john/doe`                                      |    valid |
| `/products/[category]/[...subcategories]`             | `/products/electronics/laptops`                        |    valid |
|                                                       | `/products/electronics/laptops/lenovo`                 |    valid |
| `/products/[category]/[[...subcategories]]`           | `/products/electronics`                                |    valid |
|                                                       | `/products/electronics/laptops`                        |    valid |
|                                                       | `/products/electronics/laptops/lenovo`                 |    valid |
|                                                       | `/products/electronics/laptops/lenovo/thinkpad`        |    valid |
| `/products/[category]/[...subcategories]/[...items]`  | `/products/electronics/laptops`                        |  invalid |
|                                                       | `/products/electronics/laptops/lenovo`                 |  invalid |
|                                                       | `/products/electronics/laptops/lenovo/thinkpad`        |  invalid |




```python exec
questions = [
    {
        "id": 0,
        "question_type": "multiple_choice",
        "question_body": "What can you use Reflex's dynamic routes for in web applications?",
        "question_image": None,
        "options": [
            "Display static text",
            "Create flexible and adaptable URL structures",
            "Upload files",
            "Send emails"
        ],
        "correct_answers": ["Create flexible and adaptable URL structures"]
    },
    {
        "id": 1,
        "question_type": "multiple_choice",
        "question_body": "Which of the following is an example of a catch-all route in Reflex?",
        "question_image": None,
        "options": [
            "`/users/[id]/posts/[...username]`",
            "`/products/[category]/[id]`",
            "`/users/posts`",
            "`/services/[service_id]`"
        ],
        "correct_answers": ["`/users/[id]/posts/[...username]`"]
    },
    {
        "id": 2,
        "question_type": "multiple_choice",
        "question_body": "What does the optional catch-all route (`[[...username]]`) indicate in Reflex?",
        "question_image": None,
        "options": [
            "The segments are mandatory",
            "The segments are optional and the URL can match with or without them",
            "The segments are encrypted",
            "None of the above"
        ],
        "correct_answers": ["The segments are optional and the URL can match with or without them"]
    },
    {
        "id": 3,
        "question_type": "single_choice",
        "question_body": "What should be the placement of catch-all routes in the URL pattern according to Reflex documentation?",
        "question_image": None,
        "options": [
            "At the beginning",
            "In the middle",
            "At the end",
            "Anywhere"
        ],
        "correct_answers": ["At the end"]
    },
    {
        "id": 4,
        "question_type": "multiple_choice",
        "question_body": "Which of these URL patterns are valid for a Reflex application as per the Routes Validation Table?",
        "question_image": None,
        "options": [
            "`/users/john/doe`",
            "`/products/electronics/laptops/lenovo`",
            "`/services/123`",
            "`/users/[...username]/posts`"
        ],
        "correct_answers": [
            "`/users/john/doe`",
            "`/products/electronics/laptops/lenovo`"
        ]
    }
]

```


```python eval
quiz_component(questions)
```


