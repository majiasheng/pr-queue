class MissingLinkException(Exception):
    def __init__(self) -> None:
        msg = '"link" is missing from request'
        super().__init__(msg)

class LinkDoesNotExistException(Exception):
    def __init__(self, link: str) -> None:
        msg = f'"{link}" does not exist'
        super().__init__(msg)


class BadPriorityAttributeException(Exception):
    def __init__(self) -> None:
        msg = 'urgency/importance/complexity can only be 0 or 1'
        super().__init__(msg)
