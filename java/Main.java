public class Main{
    public static void main(String[] args){
        int ONE_BILION = 1000000000;
        int counting = 0;
        int index = 0;
        
        for(index = 0; index < ONE_BILION; index++){
            counting = counting + 1;
        }
        
        System.out.println(counting);
        
    }
}