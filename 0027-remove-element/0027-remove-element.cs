public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int n = nums.Length;
        int slow = n -1;
        int fast = n -1;

        while(fast >= 0){
            if(nums[fast] == val){
                nums[fast] = nums[slow];
                nums[slow] = val;
                --slow;
            }
            --fast;
        }
        return slow+1;
    }
}