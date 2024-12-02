class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> memo = new HashMap<>();
        int maxLength = 0;
        int start = 0;
        for(int end = 0; end < s.length(); end++){
            char current = s.charAt(end);
            if (memo.containsKey(current)) {
                start = Math.max(start, memo.get(current) + 1);
            }
            maxLength = Math.max(maxLength, (end - start) + 1);
            memo.put(current, end);
        }
        return maxLength;
    }
}