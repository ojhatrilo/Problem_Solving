# n = input("Enter a word:")
# nice = []
# for i in range(len(n)):
#     if i+1<len(n) and n[i].lower() == n[i+1].lower():
#         nice.append(n[i])
#     elif  i>0 and n[i].lower() == n[i-1].lower():
#         nice.append(n[i])
# x = " ".join(nice)
# print(x)
            
            
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_range = (0, 0)
        s_byte = bytearray(s.encode())

        for i in range(len(s) - 1):
            low, up = 0, 0

            for j in range(i, len(s)):
                if s_byte[j] >= ord('a'):
                    low |= 1 << (s_byte[j] - ord('a'))
                else:
                    up |= 1 << (s_byte[j] - ord('A'))
                if low == up and (j + 1 - i) > (max_range[1] - max_range[0]):
                    max_range = (i, j + 1)
                    
        return s_byte[max_range[0]:max_range[1]].decode()

# Driver code
if __name__ == "__main__":
    user_input = input("")
    solution = Solution()
    result = solution.longestNiceSubstring(user_input)
    print(result)
