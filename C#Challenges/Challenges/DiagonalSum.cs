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

class Result
{

    /*
     * Complete the 'diagonalDifference' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    public static int diagonalDifference(List<List<int>> arr)
    {
        List<int> diagonalSum = new List<int>(){0, 0};
        
        for(int i=0; i<arr.Count; i++){
            diagonalSum[0]+=arr[i][i];
        }
        
        int maxIndex = arr.Count-1;
        for(int i=maxIndex; i>=0; i--){
            diagonalSum[1]+=arr[maxIndex-i][i];
        }

        return Math.Abs(diagonalSum[0]-diagonalSum[1]);
    }

}