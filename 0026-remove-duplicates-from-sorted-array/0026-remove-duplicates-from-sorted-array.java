class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 0; // first unique number
        for (int i=1; i < nums.length ; ++i){
            if(nums[i]!= nums[j]){
                ++j;    // move next to last unique number
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        return j+1;
    }
}