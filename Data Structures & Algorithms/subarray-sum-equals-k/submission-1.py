class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        sseq = 0
        dict_with_seq_sum_from_beg_equal_to_key_freq = {0: 1}

        for num in nums:
            total += num
            diff = total - k

            sseq += dict_with_seq_sum_from_beg_equal_to_key_freq.get(diff, 0)
            if total in dict_with_seq_sum_from_beg_equal_to_key_freq:
                dict_with_seq_sum_from_beg_equal_to_key_freq[total] += 1
            else:
                dict_with_seq_sum_from_beg_equal_to_key_freq[total] = 1
        return sseq