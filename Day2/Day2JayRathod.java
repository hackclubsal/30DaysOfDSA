  
 public class Day2JayRathod{
    public static void main(String[] args) {    
          
        int [] arr = new int [] {1, 2, 3, 4, 5, 6, 7};     
            
        int k = 3;    
           
                
        for(int i = 0; i < k; i++){    
            int j, last;      
            last = arr[arr.length-1];    
            
            for(j = arr.length-1; j > 0; j--){        
                arr[j] = arr[j-1];    
            }       
            arr[0] = last;    
        }    
        
        System.out.println();    
            
           
        System.out.println("Array after right rotation: ");    
        for(int i = 0; i< arr.length; i++){    
            System.out.print(arr[i] + " ");    
        }    
    }    
} 