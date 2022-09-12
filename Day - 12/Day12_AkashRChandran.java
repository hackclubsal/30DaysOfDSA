import java.util.Arrays;

public class Day12_AkashRChandran {
	static int countWindowDistinct(int win[], int K) {
		int dist_count = 0;
		for (int i = 0; i < K; i++) {
			int j;
			for (j = 0; j < i; j++)
				if (win[i] == win[j])
					break;
			if (j == i)
				dist_count++;
		}
		return dist_count;
	}

	static void countDistinct(int arr[], int N, int K) {

		for (int i = 0; i <= N - K; i++)
			System.out.print(countWindowDistinct(Arrays.copyOfRange(arr, i, arr.length), K) + " ");
	}

	public static void main(String args[]) {
		int arr[] = {4,1,1}, K = 2;
		countDistinct(arr, arr.length, K);
	}
}