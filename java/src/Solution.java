import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

/**
 * Created by Daniel on 26/10/15.
 * Template
 */
public class Solution {
    int solve(List<Integer> A) {
        return A.get(0);
    }

    public static void main(String[] args) throws FileNotFoundException {
        Solution solution = new Solution();
        Scanner in = new Scanner(new File("java/src/0.in"));
        // Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int T = Integer.valueOf(in.nextLine());
        for (int i = 0; i < T; i++) {
            List<Integer> A = Arrays.stream(in.nextLine().split(" ")).map(Integer::valueOf).collect(Collectors.toList());
            // long[] A = Arrays.stream(in.nextLine().split(" ")).mapToLong(Long::valueOf).toArray();
            out.println(solution.solve(A));
        }
        out.flush();
    }
}
