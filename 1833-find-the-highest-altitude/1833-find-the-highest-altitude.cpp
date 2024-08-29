class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int current_altitude=0;
        int max_altitude=0;

        for(int i=0;i<gain.size();i++){
            current_altitude+=gain[i];
            max_altitude=max(current_altitude,max_altitude);
        }
        return max_altitude;
        
    }
};