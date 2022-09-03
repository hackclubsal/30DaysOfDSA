public class Day3ParthBanker {
    public static void main(String[] args) {
        int arr[][] = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        System.out.println(find(arr, 91));
    }

    static boolean find(int[][] arr, int key){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if(arr[i][j] == key){
                    return true;
                }
            }
        }
        return false;
    }
}
