class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.history = [homepage]
        self.len = 1
        

    def visit(self, url: str) -> None:
        self.i += 1
        self.history = self.history[:self.i]
        self.history.append(url)
        self.len = self.i + 1
        

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.history[self.i]
        

    def forward(self, steps: int) -> str:
        self.i = min(self.len - 1, self.i + steps)
        return self.history[self.i]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)