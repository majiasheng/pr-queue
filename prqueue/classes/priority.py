from typing import Any, Dict
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

priority_matrix_reversed = {
    0: {
        'urgency': Urgency.URGENT.value,
        'importance': Importance.IMPORTANT.value,
        'complexity': Complexity.NOT_AS_COMPLEX.value
    },
    1: {
        'urgency': Urgency.URGENT.value,
        'importance': Importance.IMPORTANT.value,
        'complexity': Complexity.COMPLEX.value
    },
    2: {
        'urgency': Urgency.URGENT.value,
        'importance': Importance.NOT_AS_IMPORTANT.value,
        'complexity': Complexity.NOT_AS_COMPLEX.value
    },
    3: {
        'urgency': Urgency.URGENT.value,
        'importance': Importance.NOT_AS_IMPORTANT.value,
        'complexity': Complexity.COMPLEX.value
    },
    4: {
        'urgency': Urgency.NOT_AS_URGENT.value,
        'importance': Importance.IMPORTANT.value,
        'complexity': Complexity.NOT_AS_COMPLEX.value
    },
    5: {
        'urgency': Urgency.NOT_AS_URGENT.value,
        'importance': Importance.IMPORTANT.value,
        'complexity': Complexity.COMPLEX.value
    },
    6: {
        'urgency': Urgency.NOT_AS_URGENT.value,
        'importance': Importance.NOT_AS_IMPORTANT.value,
        'complexity': Complexity.NOT_AS_COMPLEX.value
    },
    7: {
        'urgency': Urgency.NOT_AS_URGENT.value,
        'importance': Importance.NOT_AS_IMPORTANT.value,
        'complexity': Complexity.COMPLEX.value
    },
}

priority_matrix_reversed_enum = {
    0: {
        'urgency': Urgency.URGENT,
        'importance': Importance.IMPORTANT,
        'complexity': Complexity.NOT_AS_COMPLEX
    },
    1: {
        'urgency': Urgency.URGENT,
        'importance': Importance.IMPORTANT,
        'complexity': Complexity.COMPLEX
    },
    2: {
        'urgency': Urgency.URGENT,
        'importance': Importance.NOT_AS_IMPORTANT,
        'complexity': Complexity.NOT_AS_COMPLEX
    },
    3: {
        'urgency': Urgency.URGENT,
        'importance': Importance.NOT_AS_IMPORTANT,
        'complexity': Complexity.COMPLEX
    },
    4: {
        'urgency': Urgency.NOT_AS_URGENT,
        'importance': Importance.IMPORTANT,
        'complexity': Complexity.NOT_AS_COMPLEX
    },
    5: {
        'urgency': Urgency.NOT_AS_URGENT,
        'importance': Importance.IMPORTANT,
        'complexity': Complexity.COMPLEX
    },
    6: {
        'urgency': Urgency.NOT_AS_URGENT,
        'importance': Importance.NOT_AS_IMPORTANT,
        'complexity': Complexity.NOT_AS_COMPLEX
    },
    7: {
        'urgency': Urgency.NOT_AS_URGENT,
        'importance': Importance.NOT_AS_IMPORTANT,
        'complexity': Complexity.COMPLEX
    },
}


class Priority:

    def __init__(self,
                 urgency: Urgency = Urgency.DEFAULT,
                 importance: Importance = Importance.DEFAULT,
                 complexity: Complexity = Complexity.DEFAULT) -> None:

        self.urgency = urgency
        self.importance = importance
        self.complexity = complexity

    @staticmethod
    def decode_prority(priority: int, get_int: bool = False) -> Dict[str, Any]:
        return priority_matrix_reversed_enum.get(priority, None) if not get_int else priority_matrix_reversed.get(priority, None)

    def get_priority(self) -> int:
        matrix_key = f'{self.urgency.value}{self.importance.value}{self.complexity.value}'
        fall_back_priority = len(priority_matrix)
        return priority_matrix.get(matrix_key, fall_back_priority)
