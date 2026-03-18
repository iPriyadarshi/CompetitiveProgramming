// https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A

import java.util.Scanner;

public class SegmentTreeForTheSum {

    long[] tree;
    int n;

    public SegmentTreeForTheSum(int[] arr) {
        this.n = arr.length;
        this.tree = new long[4 * n];
        build(arr, 0, 0, n - 1);
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        build(arr, node * 2 + 1, start, mid);
        build(arr, node * 2 + 2, mid + 1, end);
        tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2];
    }

    public void set(int index, int value) {
        update(0, 0, n - 1, index, value);
    }

    private void update(int node, int start, int end, int index, int value) {
        if (start == end) {
            tree[node] = value;
            return;
        }
        int mid = (start + end) / 2;
        if (index <= mid) {
            update(node * 2 + 1, start, mid, index, value);
        } else {
            update(node * 2 + 2, mid + 1, end, index, value);
        }
        tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2];
    }

    public long query(int left, int right) {
        return query(0, 0, n - 1, left, right);
    }

    private long query(int node, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return 0;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        long p1 = query(node * 2 + 1, start, mid, left, right);
        long p2 = query(node * 2 + 2, mid + 1, end, left, right);
        return p1 + p2;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            SegmentTreeForTheSum segTree = new SegmentTreeForTheSum(arr);

            for (int i = 0; i < m; i++) {
                int type = sc.nextInt();
                if (type == 1) {
                    int index = sc.nextInt();
                    int value = sc.nextInt();
                    segTree.set(index, value);
                } else {
                    int left = sc.nextInt();
                    int right = sc.nextInt();
                    System.out.println(segTree.query(left, right - 1));
                }
            }
        }
    }
}