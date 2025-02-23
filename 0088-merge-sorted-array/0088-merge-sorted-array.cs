public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        if (n != 0){    //have elements to merge from nums2
            int i = 0;
            while (i < n){
                nums1[m+i] = nums2[i];
                ++i;
            }
            Array.Sort(nums1);
        }
    }
}