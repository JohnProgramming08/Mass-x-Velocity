from .create_db import Question, TopicQuestion, db
from services import Json


class Populate:
    # Add all the questions to the database
    @staticmethod
    def populate_questions():
        question_list = Json.get_questions()
        for question in question_list:
            if not question.get("image_filename"):
                question["image_filename"] = "None"

            new_question = Question(
                question_text=question["question"],
                question_image_filename=question["image_filename"],
                answer=question["answer"],
                answer_units=question["units"],
                working_image_filename=question["working_image_filename"],
                level=question["level"],
                difficulty=question["difficulty"],
            )
            new_question.topic_questions.append(TopicQuestion(topic=question["topic"]))
            db.session.add(new_question)
            db.session.commit()

