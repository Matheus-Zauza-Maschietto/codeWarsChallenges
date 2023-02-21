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
    if(n % 2 == 0 && n != 2)
    {
        return false;
    }
    if(n % 3 == 0 && n != 3)
    {
        return false;
    }
    for(int cont = 1; cont < n; cont+=2)
    {
        if(n % cont == 0)
        {
            return false;
        }
    }
    return true;
  }
}
