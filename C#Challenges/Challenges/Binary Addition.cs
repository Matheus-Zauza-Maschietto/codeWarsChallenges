// Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
// The binary number returned should be a string.
// Examples:(Input1, Input2 --> Output (explanation)))
// 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
// 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

using System;
namespace C_Challenges.Challenges.AddBinary;
public static class Kata
{
  public static string AddBinary(int a, int b)
  {
        List<int> binaryTable = new List<int>();
        int contador = 0, sum = a+b;
        string binary = "";

        while(Math.Pow(2, contador) < (a+b)){
          binaryTable.Add((int)Math.Pow(2, contador));
          
          contador++;
        }
        contador--;
        while(contador >= 0){
          if(sum-binaryTable[contador] >= 0){
            sum = sum-binaryTable[contador];
            binary += "1";
          }
          else{
            binary += "0";
          }
          contador--;
        }

        return binary;
  }
}