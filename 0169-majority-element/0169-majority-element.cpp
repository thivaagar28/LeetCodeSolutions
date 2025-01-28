class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int exp = floor(nums.size()/2);
        for (int i= 0; i < nums.size(); ++i){
            int count = 1;
            for (int j=i+1; j < nums.size() ; ++j){
                if(nums[i] == nums[j]){
                    ++count;
                }
            }
            if (count > exp){
                return nums[i];
            }
        }
        return 0;
    }
};