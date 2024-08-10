class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        self.restore_ip_addresses_rec(s, 0, [], result)

        return result

    def restore_ip_addresses_rec(self, s, index, current_segments, result):
        if index == len(s) and len(current_segments) == 4:
            result.append(".".join(current_segments))
            return

        if len(current_segments) >= 4:
            return
        
        for i in range(1, 4):
            if index + i > len(s):
                break

            segment = s[index: index + i]
            if self.valid_ip_address_segment(segment):
                current_segments.append(segment)
                self.restore_ip_addresses_rec(s, index + i, current_segments, result)
                current_segments.pop()
    
        
    def valid_ip_address_segment(self, segment):
        if len(segment) == 0:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        try:
            num = int(segment)
            return 0 <= num <= 255
        except ValueError:
            return False