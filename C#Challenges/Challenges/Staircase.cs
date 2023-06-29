using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Staircase
{

    /*
     * Complete the 'staircase' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void staircase(int n)
    {
        for(int i=1; i<=n; i++){
            
            for(int spaces=0; spaces<n-i; spaces++){
                Console.Write(" ");
            }
            for(int hashTag=0; hashTag<i; hashTag++){
                Console.Write("#");
            }
            Console.WriteLine();
            
        }

    }

}