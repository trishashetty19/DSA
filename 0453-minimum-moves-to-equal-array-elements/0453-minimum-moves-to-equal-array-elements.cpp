class Solution {
public:
    int minMoves(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int min_element=nums[0];
        int moves=0;
        for(int num:nums){
            moves=moves+(num-min_element);
        }
        return moves;
    }
};