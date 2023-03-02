using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace C_Challenges.Challenges;

public static class Kata
{
  public static bool IsPrime(int n)
  {
    if(n <= 1)
    {
        return false;
    }
    if(n != 2)
    {
        if(n % 2 == 0)
        {
            return false;
        }
        if(n % 3 == 0)
        {
            return false;
        }
    }
    int cont = 1;
    bool AddTwo = false;
    while(cont < n)
    {
        if(n % cont == 0)
        {
            return false;
        }
        if(AddTwo){
            cont += 4;
        }
        else{
            cont += 2;
        }
    }
    return true;
  }
}
