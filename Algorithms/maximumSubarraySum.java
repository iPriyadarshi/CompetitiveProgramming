public class maximumSubarraySum {

    public static int findMaxSubarraySum1(int[] arr) {
        // T.C: O(n^3), S.C: O(1)
        int maxSum = Integer.MIN_VALUE;
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int currentSum = 0;
                for (int k = i; k <= j; k++) {
                    currentSum += arr[k];
                }
                maxSum = Math.max(maxSum, currentSum);
            }
        }
        return maxSum;
    }

    public static int findMaxSubarraySum2(int[] arr) {
        // T.C: O(n^2), S.C: O(1)
        int maxSum = Integer.MIN_VALUE;
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int currentSum = 0;
            for (int j = i; j < n; j++) {
                currentSum += arr[j];
                maxSum = Math.max(maxSum, currentSum);
            }
        }
        return maxSum;
    }

    public static int findMaxSubarraySum3(int[] arr) {
        // T.C: O(n), S.C: O(1)
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;
        for (int i = 0; i < arr.length; i++) {
            currentSum = Math.max(arr[i], currentSum + arr[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int[] arr = { -1, 2, 4, -3, 5, 2, -5, 2 };
        int maxSum = findMaxSubarraySum3(arr);
        System.out.println("Maximum Subarray Sum: " + maxSum);

        int[] arr2 = { -2, -3, -1, -4 };
        int maxSum2 = findMaxSubarraySum2(arr2);
        System.out.println("Maximum Subarray Sum: " + maxSum2);
    }
}