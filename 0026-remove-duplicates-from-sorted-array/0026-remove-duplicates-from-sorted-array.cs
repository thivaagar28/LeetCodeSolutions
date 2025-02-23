public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int slow = 0;
        int fast = 1;

        while(fast < nums.Length){
            if(nums[fast] > nums[slow]){
                ++ slow;
                nums[slow] = nums[fast];
            }
            ++fast;
        }

        return slow+1;
    }
}