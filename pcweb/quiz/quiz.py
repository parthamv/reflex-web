"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# from rxconfig import config

import importlib
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
class Question(rx.Base):
    id: int
    question_type: str
    question_body: str
    question_image: str | None
    options: list[str]
    correct_answers: list[str]
    selected_answers: list[str] = []
    is_correct: bool = False

    def _check_correct_answers(self, answers):
        return answers == self.correct_answers

class State(rx.State):
    """The app state."""
    index : int = 0
    quiz_completed: bool = False
    questions: list[Question] = []
    submitted_answers: dict[int, list[str]] = {}

    def load_questions(self, questions_list):
        self.questions = [Question.parse_obj(q) for q in questions_list]
        print(questions_list)

    def submit_question(self, data, question_id):
        if "_selected_option" in data:
            submitted_answer = [data["_selected_option"]]
        else:  # multiple_choice
            submitted_answer = [key for key, value in data.items() if value == "on"]
        self.submitted_answers[question_id] = submitted_answer
        self.questions[question_id].selected_answers = submitted_answer

        question = self.questions[question_id]
        question.is_correct = question._check_correct_answers(submitted_answer)

    @rx.var
    def current_question(self) -> Question:
        if 0 <= self.index < len(self.questions):
            return self.questions[self.index]
        else:
            # Handle the case where the index is out of range
            # For example, return None or raise a more descriptive error
            return None

    def next_question(self):
        if self.index < len(self.questions) - 1:
            self.index += 1

    def prev_question(self):
        if self.index > 0:
            self.index -= 1

    def submit_quiz(self):
        self.quiz_completed = True

    @rx.var
    def last_question(self):
        return self.index >= len(self.questions) - 1

def multi_choice_question_comp(question : Question) -> rx.Component:
    def is_selected(option: str) -> bool:
        return question.selected_answers.contains(option)

    return rx.form(
        rx.text(question.question_body),
        rx.foreach(
            question.options,
            lambda option: rx.checkbox(
                option,
                name=option,
                default_checked=is_selected(option),
            ),
        ),
        rx.hstack(
            previous_button(),
            rx.cond(
                State.last_question,
                rx.button("Submit", on_click=State.submit_quiz),
                next_button(),
            ),
        ),
        on_submit=lambda data: State.submit_question(data, question.id),
    )

def single_choice_question_comp(question : Question) -> rx.Component:
    return rx.form(
        rx.text(question.question_body),
        rx.radio(
            question.options,
            name="_selected_option",
            default_value=rx.cond(
                question.selected_answers.length() > 0,
                question.selected_answers[0],
                "",
            ),
        ),
        rx.hstack(
            previous_button(),
            rx.cond(
                State.last_question,
                rx.button("Submit", on_click=State.submit_quiz),
                next_button(),
            ),
        ),
        on_submit=lambda data: State.submit_question(data, question.id),
    )

def next_button():
    return rx.button(
        "Next",
        on_click=State.next_question,
    ) 

def previous_button():
    return rx.button(
        "Previous",
        on_click=State.prev_question,
    )

def quiz_comp() -> rx.Component:
    cur_question = State.current_question
    return rx.vstack(
        rx.cond(
            cur_question,
            rx.cond(
                cur_question.question_type == "single_choice",
                single_choice_question_comp(cur_question),
                multi_choice_question_comp(cur_question),
            ),
        ),
    )

def question_result(question : Question) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("Question: ", size="2",),
            rx.text(question.id, size="2"),
        ),
        rx.vstack(
            rx.cond(
                question.is_correct,
                rx.text("Correct!", size="2",),
                rx.text("Incorrect!", size="2",),
            ),
        )
    )

def result_comp() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text("-----Test Result-----", size="3"),
            rx.foreach(
                State.questions,
                question_result,
            ),
        )
    )

def quiz_component(questions_list) -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.cond(
                State.quiz_completed,
                result_comp(),
                quiz_comp(),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        # on_mount=lambda: State.load_questions(questions_list),
        on_mount=State.load_questions(questions_list),
        height="50vh",
    )