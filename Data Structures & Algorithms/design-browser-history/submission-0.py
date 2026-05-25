class PageNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.tail = PageNode(None)
        self.head = PageNode(None)
        self.page = PageNode(homepage)
        self.page.prev = self.head
        self.page.next = self.tail
        self.head.next = self.page
        self.tail.prev = self.page
        

    def visit(self, url: str) -> None:
        new_page = PageNode(url)
        new_page.next = self.tail
        new_page.prev = self.page
        self.page.next = new_page
        self.tail.prev = new_page
        self.page = new_page
        

    def back(self, steps: int) -> str:
        while self.page.prev != self.head and steps > 0:
            self.page = self.page.prev
            steps -= 1
        return self.page.url
        

    def forward(self, steps: int) -> str:
        while self.page.next != self.tail and steps > 0:
            self.page = self.page.next
            steps -= 1
        return self.page.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)