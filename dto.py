from dataclasses import dataclass
from datetime import date
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
    description1: str = ui_field("Some description", min_length=5, pattern="Example.*")


@dataclass
class TestDto1:
    status: TestStatus
    text_list: list[str]
    # Unfortunately, fields with default values must go at the end
    id: int = ui_field("ID description", min=0)
    flag: bool = ui_field("Flag description")
    some_date: str = ui_field("Custom date", date_format="yyyy/MM/dd")
    test_dto2: TestDto2 = ui_field("Inner DTO")
