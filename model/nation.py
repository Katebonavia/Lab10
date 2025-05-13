from dataclasses import dataclass


@dataclass
class Nation:
    StateAbb: str
    CCode: int
    StateNme: str

    def __eq__(self, other):
        return self.CCode == other.CCode

    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return f"{self.CCode} - {self.StateAbb}"
