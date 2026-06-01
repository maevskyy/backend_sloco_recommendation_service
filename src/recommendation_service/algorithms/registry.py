from dataclasses import dataclass


@dataclass(frozen=True)
class AlgorithmDescriptor:
    name: str
    version: str


class AlgorithmRegistry:
    def __init__(self) -> None:
        self._algorithms: list[AlgorithmDescriptor] = []

    def list_algorithms(self) -> list[AlgorithmDescriptor]:
        return list(self._algorithms)


registry = AlgorithmRegistry()

