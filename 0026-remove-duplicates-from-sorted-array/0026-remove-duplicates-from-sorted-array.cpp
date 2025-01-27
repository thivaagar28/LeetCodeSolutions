class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j= 0;
        for (int i=1; i< nums.size(); ++i){ // first number is always unique
            if(nums[i] != nums[j]){ //compared to last unique
                ++j; // move pointer next to the last unique
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        return j+1;
    }
};