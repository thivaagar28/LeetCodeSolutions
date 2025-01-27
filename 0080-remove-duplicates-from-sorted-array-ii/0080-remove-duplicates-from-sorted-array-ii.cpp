class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j = 0;
        int uniq = 1;
        int c_uniq = nums[0];

        for (int i=1; i< nums.size() ; ++i){
            if (nums[i] > c_uniq){ //next number > so automatic new unique
                c_uniq = nums[i];
                uniq = 1;
                ++j; //place for new unique
                nums[j] = c_uniq;
            } else{ //trailing numbers
                if (uniq < 2){
                    ++uniq;
                    ++j; // points to suppose place of second trailed number
                    nums[j] = c_uniq; 
                }
            }
        }
        return j+1;
    }
};