class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged(nums1.size() + nums2.size()); 
        merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), merged.begin());
        sort(merged.begin(),merged.end());
        int sized=merged.size();  
        if(sized%2==0)
        {
            int ind=sized/2;
            return ((merged[ind-1] + merged[ind])/2.0);
        }
        return merged[sized/2];
    }
};
