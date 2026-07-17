class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_idx = len(digits) - 1
       # if last_idx == -1:
       #     return digits


        if digits[last_idx] != 9:
            digits[last_idx] = digits[last_idx] + 1
            return digits
        
        carry = 1
        for i in range(last_idx, -1, -1):
            add = digits[i] + carry
            if add == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = add
                break;
        
        if carry == 1:
            digits.insert(0, carry)
        
        return digits