class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int j=0;
        sort(nums.begin(),nums.end());
        int n=nums.size();
        for(int i=1;i<n;i++){
            if(nums[i]==nums[i-1]){
                 j=nums[i];
            }
        }
        return j;


    }
};