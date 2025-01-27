class Solution {
    public int removeElement(int[] nums, int val) {
        int [] newnums = nums.clone(); 
        
        int k =0;
        for (int i=0; i < newnums.length; ++i){
            if(newnums[i]!= val){
                nums[k] = nums[i];
                ++k;
            }
        }

        return k;
    }
}