class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> merged (m+n);
        int index = 0;
        for (int i=0; i < m; i++){
            merged[index] = nums1[i];
            index +=1;
        }
        for (int j=0; j < n; j++){
            merged[index] = nums2[j];
            index +=1;
        }
        sort(merged.begin(), merged.end());
        nums1 = merged;
    }
};