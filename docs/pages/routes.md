```python exec
import reflex as rx
from pcweb import constants, styles
from pcweb.quiz.quiz import quiz_component


route = (
"""
def index():
    return rx.text('Root Page')

def about():
    return rx.text('About Page')


def custom():
    return rx.text('Custom Route')

app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
"""
)

nested_routes = (
"""
@rx.page(route='/nested/page')
def nested_page():
    return rx.text('Nested Page')

app = rx.App()
"""

)

  
routes_get_query_params = (
"""
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        username = args.get('username')
        post_id = args.get('id')
        return f'Posts by {username}: Post {post_id}'

@rx.page(route='/user/[username]/posts/[id]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()
"""  
)


page_decorator = (
"""
@rx.page(route='/', title='My Beautiful App')
def index():
    return rx.text('A Beautiful App')
"""  
)

current_page_link = (
"""
class State(rx.State):
    
    @rx.var
    def current_url(self) -> str:
        return self.router.page.full_raw_path
"""  
)


current_page_info = (
"""
class State(rx.State):
    def some_method(self):
        current_page_route = self.router.page.path
        current_page_url = self.router.page.raw_path
        # ... Your logic here ...

"""  
)

client_ip = (
"""
class State(rx.State):
    def some_method(self):
        client_ip = self.router.session.client_ip
        # ... Your logic here ...

"""  
)
```

# Pages

Pages in Reflex allow you to define components for different URLs. This section covers creating pages, handling URL
arguments, accessing query parameters, managing page metadata, and handling page load events.

## Adding a Page

You can create a page by defining a function that returns a component.
By default, the function name will be used as the route, but you can also specify a route.

```python
{route.strip()}
```

In this example we create three pages:

- `index` - The root route, available at `/`
- `about` - available at `/about`
- `/custom` - available at `/custom-route`

## Page Decorator

You can also use the `@rx.page` decorator to add a page.

```python
{page_decorator}
```

This is equivalent to calling `app.add_page` with the same arguments.

```md alert
# Index is a special exception where it is available at both `/` and `/index`. All other pages are only available at their specified route.
```

## Nested Routes

Pages can also have nested routes.

```python
{nested_routes}
```

This component will be available at `/nested/page`.

## Getting the Current Page Link

The `router.page.path` attribute allows you to obtain the path of the current page from the router data,
for dynamic pages this will contain the slug rather than the actual value used to load the page.

To get the actual URL displayed in the browser, use `router.page.raw_path`. This
will contain all query parameters and dynamic path segments.

```python
{current_page_info}
```

In the above example, `current_page_route` will contain the route pattern (e.g., `/posts/[id]`), while `current_page_url`
will contain the actual URL (e.g., `http://example.com/posts/123`).

To get the full URL, access the same attributes with `full_` prefix.

Example:

```python
{current_page_link}
```

In this example, running on `localhost` should display `http://localhost:3000/user/hey/posts/3/`

## Getting Client IP

You can use the `router.session.client_ip` attribute to obtain the IP address of the client associated
with the current state.

```python
{client_ip}
```

```python exec
questions = [
    {
        "id": 0,
        "question_type": "multiple_choice",
        "question_body": "What can be achieved using the '@rx.page' decorator in the Reflex framework?",
        "question_image": None,
        "options": [
            "Define a static route",
            "Create a nested route",
            "Add a page with a specific route and title",
            "Access client IP address"
        ],
        "correct_answers": ["Add a page with a specific route and title"]
    },
    {
        "id": 1,
        "question_type": "single_choice",
        "question_body": "Which attribute would you use to get the actual URL displayed in the browser including query parameters?",
        "question_image": None,
        "options": [
            "router.page.path",
            "router.page.raw_path",
            "router.session.client_ip",
            "router.page.params"
        ],
        "correct_answers": ["router.page.raw_path"]
    },
    {
        "id": 2,
        "question_type": "multiple_choice",
        "question_body": "In the Reflex framework, which of the following statements are true regarding pages?",
        "question_image": None,
        "options": [
            "You can use function names as default routes",
            "Every page must be explicitly added with 'app.add_page()'",
            "@rx.page decorator cannot specify custom routes",
            "Nested routes can be created for more complex page structures"
        ],
        "correct_answers": [
            "You can use function names as default routes",
            "Nested routes can be created for more complex page structures"
        ]
    },
    {
        "id": 3,
        "question_type": "single_choice",
        "question_body": "What is used to handle dynamic URL segments and query parameters in a Reflex application?",
        "question_image": None,
        "options": [
            "router.page.full_raw_path",
            "router.page.params",
            "router.session.client_ip",
            "router.page.path"
        ],
        "correct_answers": ["router.page.params"]
    },
    {
        "id": 4,
        "question_type": "single_choice",
        "question_body": "Where in the Reflex framework would you find the client's IP address?",
        "question_image": None,
        "options": [
            "router.page.raw_path",
            "router.page.path",
            "router.session.client_ip",
            "router.page.params"
        ],
        "correct_answers": ["router.session.client_ip"]
    }
]
```

```python eval
quiz_component(questions)
```
