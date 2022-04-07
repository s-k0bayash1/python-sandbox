import dataclasses


@dataclasses.dataclass(frozen=True)
class Hoge:
    id: int
    name: str

    def foo(self) -> str:
        return f"idは{self.id}、nameは{self.name}"


def main():
    hoge1 = Hoge(id=1, name="test")
    hoge2 = Hoge(id=1, name="test")
    print(hoge1 == hoge2)
    hoge3 = dataclasses.replace(hoge1, name="test2")
    print(hoge3)


if __name__ == "__main__":
    main()
