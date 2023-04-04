// Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
// Write a function which takes a list of strings and returns each line prepended by the correct number.
// The numbering starts at 1. The format is n: string. Notice the colon and space in between.
// Examples: (Input --> Output)
// [] --> []
// ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace C_Challenges.Challenges.Testing123;
using System.Collections.Generic;
public class LineNumbering 
{
    public static List<string> Number(List<string> lines) 
    {
        foreach(var item in lines.Select((item, index) => (item, index))){
            System.Console.WriteLine($"{item.item}-{item.index}");
        }
        return lines;
    }
}