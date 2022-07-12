"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
"""


def next_smaller(n):
    past_number = n
    n = list(str(n))
    len_ = len(n) - 1
    for i in range(len_ - 1, -1, -1):
        for j in range(len_, i - 1, -1):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
                head = n[:i+1]
                tail = n[-1:i:-1]

                return (new_number
                        if (new_number := int("".join(head+tail))) != past_number and head[0] != '0'
                        else -1)
    return -1


print(next_smaller(721), end='\n\n')
print(next_smaller(907), end='\n\n')
print(next_smaller(531), end='\n\n')
print(next_smaller(135), end='\n\n')
print(next_smaller(2071), end='\n\n')
print(next_smaller(414), end='\n\n')
print(next_smaller(123456798), end='\n\n')
print(next_smaller(123456789), end='\n\n')
print(next_smaller(1234567908), end='\n\n')
