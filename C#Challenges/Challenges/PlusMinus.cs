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

class PlusMinus
{

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<int> arr)
    {
        decimal positiveNumbers = arr.Where(number => number > 0).Count();
        decimal negativeNumbers = arr.Where(number => number < 0).Count();
        decimal zeroNumbers = arr.Count - positiveNumbers - negativeNumbers;
        
        Console.WriteLine(positiveNumbers/arr.Count);
        Console.WriteLine(negativeNumbers/arr.Count);
        Console.WriteLine(zeroNumbers/arr.Count);
    }

}