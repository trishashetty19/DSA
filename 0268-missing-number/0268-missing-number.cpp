class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res,sum=0,missing_no,n=nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<n;i++){
            sum+=nums[i];
            res=n*(n+1)/2;
            missing_no=abs(sum-res);
        }
        return missing_no;
    }
};