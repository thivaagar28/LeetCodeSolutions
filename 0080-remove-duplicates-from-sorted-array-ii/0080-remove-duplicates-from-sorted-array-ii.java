class Solution {
    public int removeDuplicates(int[] nums) {
        int j=0;
        int c_uniq = nums[0];
        int uniq = 1;
        for (int i = 1; i < nums.length ; ++i){
            if (nums[i] > c_uniq){ // automatic new uniq
                uniq = 1;
                c_uniq = nums[i];
                ++j;
                nums[j] = c_uniq;
            } else{
                if (uniq < 2){ // trailing number and 2nd supposed number only
                    ++uniq;
                    ++j;
                    nums[j] = c_uniq;
                }
            }
        }
        return j+1;
    }
}