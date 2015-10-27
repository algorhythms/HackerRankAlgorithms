package MaximiseSum;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;

/**
 * Created by Daniel on 26/10/15.
 */
public class Solution {
    /**
     * Balanced Binary Search Tree (ADT)
     *
     * Java notice:
     * 1. modulo can return negaitve
     * 2. prefer long over int
     */
    long solve(long N, long M, long[] A) {
        if (N != A.length)
            System.exit(1);

        long s = 0;
        TreeSet<Long> ts = new TreeSet<>();
        long maxa = 0;
        for(long a: A) {
            s = (s+a)%M;

            long upper = s;
            try { upper = ts.ceiling(s+1); }
            catch (NullPointerException e) {}
            maxa = Math.max(maxa, Math.max(s, (s-upper+M)%M));

            ts.add(s);
        }
        return maxa;
    }

    public static void main(String[] args) throws FileNotFoundException {
        Solution solution = new Solution();
        Scanner in = new Scanner(new File("java/src/0.in"));
        // Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int T = Integer.valueOf(in.nextLine());
        for (int i = 0; i < T; i++) {
            long[] NM = Arrays.stream(in.nextLine().split(" ")).mapToLong(Long::valueOf).toArray();
            long[] A = Arrays.stream(in.nextLine().split(" ")).mapToLong(Long::valueOf).toArray();
            out.println(solution.solve(NM[0], NM[1], A));
        }
        out.flush();
    }
}
