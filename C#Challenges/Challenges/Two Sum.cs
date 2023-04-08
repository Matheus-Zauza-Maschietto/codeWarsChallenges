//Find 
namespace C_Challenges.Challenges.TwoSum;
public class Kata
{
  public static int[] TwoSum(int[] numbers, int target)
  {
    var sum = new int[2];
    for(int k=0; k<numbers.Length; k++)
        for(int i=k+1; i<numbers.Length; i++)
            if(numbers[k]+numbers[i]==target){
                sum[0]=k;
                sum[1]=i;
                return sum;
            }
    return sum;
  }
}