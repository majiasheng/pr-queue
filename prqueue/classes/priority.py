from .urgency import Urgency
from .importance import Importance
from .complexity import Complexity


'''
urgency > importance > complexity
priority:
    1. urgent + important + not_as_complex
    2. urgent + important + complex
    3. urgent + not_as_important + not_as_complex
    4. urgent + not_as_important + complex
    5. not_as_urgent + important + not_as_complex
    6. not_as_urgent + important + complex
    7. not_as_urgent + not_as_important + not_as_complex
    8. not_as_urgent + not_as_important + complex
'''
priority_matrix = {
    f'{Urgency.URGENT.value}{Importance.IMPORTANT.value}{Complexity.NOT_AS_COMPLEX.value}': 0,
    f'{Urgency.URGENT.value}{Importance.IMPORTANT.value}{Complexity.COMPLEX.value}': 1,
    f'{Urgency.URGENT.value}{Importance.NOT_AS_IMPORTANT.value}{Complexity.NOT_AS_COMPLEX.value}': 2,
    f'{Urgency.URGENT.value}{Importance.NOT_AS_IMPORTANT.value}{Complexity.COMPLEX.value}': 3,
    f'{Urgency.NOT_AS_URGENT.value}{Importance.IMPORTANT.value}{Complexity.NOT_AS_COMPLEX.value}': 4,
    f'{Urgency.NOT_AS_URGENT.value}{Importance.IMPORTANT.value}{Complexity.COMPLEX.value}': 5,
    f'{Urgency.NOT_AS_URGENT.value}{Importance.NOT_AS_IMPORTANT.value}{Complexity.NOT_AS_COMPLEX.value}': 6,
    f'{Urgency.NOT_AS_URGENT.value}{Importance.NOT_AS_IMPORTANT.value}{Complexity.COMPLEX.value}': 7,
}


class Priority:

    def __init__(self,
                 urgency: Urgency = Urgency.DEFAULT,
                 importance: Importance = Importance.DEFAULT,
                 complexity: Complexity = Complexity.DEFAULT) -> None:

        self.urgency = urgency
        self.importance = importance
        self.complexity = complexity

    def get_priority(self) -> int:
        # TODO: verify below are numbers
        matrix_key = f'{self.urgency.value}{self.importance.value}{self.complexity.value}'
        return priority_matrix.get(matrix_key)
