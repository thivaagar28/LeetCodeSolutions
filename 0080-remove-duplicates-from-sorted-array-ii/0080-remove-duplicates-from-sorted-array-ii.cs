public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int slow = 0;
        int fast = 1;
        int count = 1;

        while(fast < nums.Length){
            if(nums[fast] > nums[slow]){
                ++slow;
                nums[slow] = nums[fast];
                count = 1;
                ++fast;
                continue;
            }
            //found same number
            if(count < 2){
                //this is 2nd appearance
                ++slow;
                nums[slow] = nums[fast];
                ++count;
            }
            ++fast;
        }
        return slow+1;
    }
}