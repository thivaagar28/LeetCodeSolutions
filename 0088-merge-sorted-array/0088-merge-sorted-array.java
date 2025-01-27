class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n!=0) { // have elements in num2 or don't need merging
            int j=0;
            if (m==0){ //no element in nums1
                for (int i=0 ; i < n ; ++i){ // hence starting index refers to 0
                    nums1[i] = nums2[j];
                    ++j;
                }
            } else{ //existing elements in nums1
                for (int i=m ; i < m+n ; ++i){ // starting index should be after elements in number 1
                    nums1[i] = nums2[j];
                    ++j;
                }
            }
        }
        Arrays.sort(nums1);
    }
}