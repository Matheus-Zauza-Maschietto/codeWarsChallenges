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

class MinMaxSum
{

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void minMaxSum(List<int> arr)
    {
        arr.Sort();
        int maxSum =arr.Sum()-arr[0];
        int minSum = arr.Sum()-arr[arr.Count-1];
        Console.WriteLine(minSum+" "+maxSum);
    }

}