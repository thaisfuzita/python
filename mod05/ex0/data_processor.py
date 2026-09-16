#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.number = 0
        self.storage = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        item = self.storage.pop(0)
        return item


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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
    def validate(self, data: Any) -> bool:
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
    def validate(self, data: Any) -> bool:
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f" Trying to validate input '42': {np.validate(42)}")
    print(f" Trying to validate input 'Hello': {np.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    data1: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {data1}")
    np.ingest(data1)
    print(" Extracting 3 values...")
    for i in range(3):
        rank, value = np.output()
        print(f" Numeric value {i}: {value}")
    print()

    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f" Trying to validate input '42': {tp.validate(42)}")
    data2: list[str] = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data2}")
    tp.ingest(data2)
    print(" Extracting 1 value...")
    for i in range(1):
        rank, value = tp.output()
        print(f" Text value {i}: {value}")
    print()

    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f" Trying to validate input 'Hello': {lp.validate('Hello')}")
    data3: list[dict] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data3}")
    lp.ingest(data3)
    print(" Extracting 2 values...")
    for i in range(2):
        rank, value = lp.output()
        print(f" Log entry {i}: {value}")


if __name__ == "__main__":
    main()
