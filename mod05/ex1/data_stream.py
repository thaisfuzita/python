#!/usr/bin/env python3

import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.number = 0
        self.storage = []
        self.name = ""

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        item = self.storage.pop(0)
        return item


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Numeric Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            for item in data:
                if (
                    not isinstance(item, (int, float))
                    or isinstance(item, bool)
                ):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self.storage.append((self.number, str(data)))
            self.number += 1
        else:
            for num in data:
                self.storage.append((self.number, str(num)))
                self.number += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            self.storage.append((self.number, data))
            self.number += 1
        else:
            for text in data:
                self.storage.append((self.number, text))
                self.number += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Log Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                if not all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in d.items()
                ):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper dict data")
        if isinstance(data, dict):
            item = ": ".join(data.values())
            self.storage.append((self.number, item))
            self.number += 1
        else:
            for d in data:
                item = ": ".join(d.values())
                self.storage.append((self.number, item))
                self.number += 1


class DataStream:
    def __init__(self) -> None:
        self.dp: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.dp.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            found = False
            for dp in self.dp:
                if dp.validate(element):
                    dp.ingest(element)
                    found = True
                    break
            if not found:
                print(
                        f"DataStream error - "
                        f"Can't process element in stream: {element}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.dp:
            print("No processor found, no data")
            return
        for dp in self.dp:
            print(
                f"{dp.name}: total {dp.number} items "
                f"processed, remaining {len(dp.storage)} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    ds = DataStream()
    ds.print_processors_stats()
    print()
    print("Registering Numeric Processor\n")
    ds.register_processor(np)
    data = [
        'Hello world', [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
                'log_message': 'User wil is connected'}
        ],
        42, ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {data}")
    ds.process_stream(data)
    ds.print_processors_stats()
    print()
    print("Registering other data processors")
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    ds.process_stream(data)
    ds.print_processors_stats()
    print()
    print(
            "Consume some elements from the data processors: "
            "Numeric 3, Text 2, Log 1"
        )
    for i in range(3):
        np.output()
    for i in range(2):
        tp.output()
    for i in range(1):
        lp.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
