class ListNode:

    def __init__(self, nextt = None, prev = None, url = ""):
        self.nextt = nextt
        self.prev = prev
        self.url = url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(None, None, homepage)
        self.current.prev = self.current
        self.current.nextt = self.current
        
    def visit(self, url: str) -> None:
        newNode = ListNode(None, self.current, url)
        self.current.nextt = newNode
        self.current = self.current.nextt
        self.current.nextt = self.current

    def back(self, steps: int) -> str:
        for _ in range(steps):
            self.current = self.current.prev
        
        return self.current.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            self.current = self.current.nextt
        
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)