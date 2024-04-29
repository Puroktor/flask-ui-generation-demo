from dataclasses import dataclass
from enum import Enum
from typing import Optional

from flaskUIGenerator import ui_field


class TestStatus(str, Enum):
    FIRST = "FIRST"
    SECOND = "Custom Second"
    THIRD = "third"


@dataclass
class TestDto2:
    description2: Optional[str]
    description1: str = ui_field("Some description")


@dataclass
class TestDto1:
    status: TestStatus
    text_list: list[str]
    # Unfortunately, fields with default values must go at the end
    id: int = ui_field("ID description")
    flag: bool = ui_field("Flag description")
    test_dto2: TestDto2 = ui_field("Inner DTO")
