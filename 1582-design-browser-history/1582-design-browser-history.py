class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.page_ind = 0
        self.size = 1

    def visit(self, url: str) -> None:
        if self.page_ind + 1 >= len(self.pages):
            self.pages.append(url)
        else:
            self.pages[self.page_ind + 1] = url
        self.page_ind += 1
        self.size = self.page_ind + 1

    def back(self, steps: int) -> str:
        self.page_ind = max(0, self.page_ind - steps)
        return self.pages[self.page_ind]

    def forward(self, steps: int) -> str:
        self.page_ind = min(self.size-1, self.page_ind + steps)
        return self.pages[self.page_ind]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)