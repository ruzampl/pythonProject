class Page:
    def __init__(self, url: str, threads_cnt: int):
        self.url = url
        self.threads_cnt = threads_cnt

    def get_url(self) -> str:
        return self.url

    def set_url(self, url: str):
        self.url = url

    def get_threads_cnt(self) -> int:
        return self.threads_cnt

    def set_threads_cnt(self, threads_cnt: int):
        self.threads_cnt = threads_cnt

    def print_url(self) -> None:
        print(f"Nazwa strony:")
        print(f"{self.url}")


