from typing import TypedDict

# Note: This should be all we need to define the Lesson type.

class API_Lesson(TypedDict):
    """
    Lesson type used in the Ed API.
    """

class API_Lesson_Content(TypedDict):
    """
    Content type used in the Ed API.
    """

class API_Lesson_Challenge_Content(TypedDict):
    """
    Challenge content type used in the Ed API.
    """