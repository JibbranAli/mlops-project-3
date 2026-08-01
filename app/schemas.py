from pydantic import BaseModel, Field

class StudentInput(BaseModel):

    hours: float = Field(
        gt=0,
        lt=24,
        description="Hours Studied"
    )
