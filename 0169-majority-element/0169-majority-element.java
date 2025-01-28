class Solution {
    public int majorityElement(int[] nums) {
        int exp = (int) nums.length/2;
        for (int i=0; i < nums.length ; ++i){
            int count =1;
            for (int j= i+1; j < nums.length; ++j){
                if (nums[i] == nums[j]){
                    ++count;
                }
            }
            if(count > exp){
                return nums[i];
            }
        }
        return 0;
    }
}