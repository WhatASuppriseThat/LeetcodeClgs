package com.chimpanzeetypewriter._001_010;

import java.util.HashMap;
import java.util.Map;

public class Two_Sum {

    public static void main(String[] args) {
        var sol = new Solution();
        int target = 3456;
        int[] array = new int[]{1,2,3,4,5,6,7};
        sol.twoSum(array, target);
    }

    static class Solution {

        public int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                int x = nums[i];
                if (map.containsKey(target - x)) {
                    return new int[]{map.get(target - x), i};
                }
                map.put(x, i);
            }
            throw new IllegalArgumentException("No two sum solution");
        }
    }

}


