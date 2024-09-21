#include<bits/stdc++.h>
using namespace std;
#define int long long int

int findMaxPetals(vector<int>& petals, int maxCoins) {
    int numFlowers = petals.size();
    sort(petals.begin(), petals.end());
    
    int currentSum = 0;
    int maxSum = 0;
    int left = 0;

    for (int right = 0; right < numFlowers; right++) {
        currentSum += petals[right];
        
        while (petals[right] - petals[left] > 1) {
            currentSum -= petals[left++];
        }
        
        while (currentSum > maxCoins) {
            currentSum -= petals[left++];
        }
        
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}

signed main() {
    int testCases;
    cin >> testCases;
    
    while (testCases--) {
        int numFlowers, maxCoins;
        cin >> numFlowers >> maxCoins;
        
        vector<int> petals(numFlowers);
        for (int i = 0; i < numFlowers; i++)
            cin >> petals[i];
        
        cout << findMaxPetals(petals, maxCoins) << "\n";
    }
    
    return 0;
}
