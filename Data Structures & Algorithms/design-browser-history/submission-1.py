class PageNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = PageNode(homepage)
        

    def visit(self, url: str) -> None:
        new_page = PageNode(url)
        new_page.prev = self.page
        self.page.next = new_page
        self.page = new_page
        

    def back(self, steps: int) -> str:
        while self.page.prev and steps > 0:
            self.page = self.page.prev
            steps -= 1
        return self.page.url
        

    def forward(self, steps: int) -> str:
        while self.page.next and steps > 0:
            self.page = self.page.next
            steps -= 1
        return self.page.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)