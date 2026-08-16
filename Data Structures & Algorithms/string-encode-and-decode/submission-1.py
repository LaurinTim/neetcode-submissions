class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            encoded_strs += str(len(s)) + "#" + s
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        strs = []
        pos = 0
        while pos < len(s):
            curr_len = ""
            while s[pos] != "#":
                curr_len += s[pos]
                pos += 1
            pos += 1
            curr_str = s[pos:pos + int(curr_len)]
            pos += int(curr_len)
            strs.append(curr_str)
        return strs