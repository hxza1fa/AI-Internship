import json
import pydantic

valid_cuts = {"Fair", "Good", "Very Good", "Premium", "Ideal"}
valid_colors = {"D", "E", "F", "G", "H", "I", "J"}
valid_clarities = {"I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"}

categorical_cols = {"cut", "color", "clarity"}

class Diamond(pydantic.BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float

    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_numerical_features(cls, values):
        if any(val <= 0 for val in values.values() if isinstance(val, (int, float))):
            raise ValueError("All numeric values must be greater than 0.")
        return values

    @pydantic.validator("cut")
    @classmethod
    def validate_cut(cls, value):
        if value not in valid_cuts:
            raise ValueError("The cut provided must be within the given cut list.")
        return value

    @pydantic.validator("color")
    @classmethod
    def validate_color(cls, value):
        if value not in valid_colors:
            raise ValueError("The color provided must be within the given color list.")
        return value

    @pydantic.validator("clarity")
    @classmethod
    def validate_clarity(cls, value):
        if value not in valid_clarities:
            raise ValueError("The clarity provided must be within the given clarity list.")
        return value

    @classmethod
    def from_json(cls, filename: str) -> "Diamond":
        with open(filename, "r") as file:
            diamond_json = json.load(file)
        return cls(**diamond_json)