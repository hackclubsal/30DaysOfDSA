public class Main {
public static void main(String[] args){
        System.out.println(isPerfectSquare(25));
    }
    static boolean isPerfectSquare(int num) {
        long start=0;
        long end=num;
        while(start<=end){
            long mid=start+(end-start)/2;
            long val=mid*mid;
            if(val==num){
                return true;
            }
            else if(val>num){
                end=mid-1;
            }
            else{
                start=mid+1;
            }
        }
        return false;
    }
}
