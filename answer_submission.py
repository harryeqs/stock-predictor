class Answer(Enum):
    under = "0"
    fair = "1"
    over = "2"


def answer_submission(answer: Answer, price_options):
    if 