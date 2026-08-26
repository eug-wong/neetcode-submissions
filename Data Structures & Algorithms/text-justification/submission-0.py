class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # [
        # "This is an",
        # "example of text",
        # "justification."
        # ]
        # so we just be greedy for each line, take up as much as possible
        # when not possible, make new line

        # justification step...
        # max - 8 chars = 8 spaces to be distrbuted
        # 3 words - 1 = 2 gaps to fill
        # 4 spaces per gap

        # example of text
        # 16 - 13 = 3 spaces to distribute
        # 3 words - 1 = 2 gaps
        # 2 spaces, then 1 space
        lines = []
        i = 0
        while i < len(words):
            line = []
            chars = 0
            while i < len(words) and chars + len(words[i]) + len(line) - 1 < maxWidth:
                line.append(words[i])
                chars += len(words[i])
                i += 1
            
            lines.append(line)

        # do the justification
        res = []
        for i, line in enumerate(lines):
            chars = 0
            for word in line:
                chars += len(word)
            slack = maxWidth - chars
            distribute = slack // (len(line) - 1) if len(line) - 1 > 0 else slack 
            remainder = slack % (len(line) - 1) if len(line) - 1 > 0 else 0
            
            # format strings
            if i == len(lines) - 1:
                res.append(" ".join(line) + " " * (slack - len(line) + 1))
                continue
            
            if len(line) == 1:
                res.append(line[0] + " " * (slack - len(line) + 1))
                continue

            stack = []
            for word in line:
                if not stack:
                    stack.append(word)
                else:
                    stack.append(" " * distribute)
                    if remainder:
                        stack.append(" ")
                        remainder -= 1
                    stack.append(word)
            res.append("".join(stack))

        return res