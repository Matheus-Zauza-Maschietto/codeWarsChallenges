using System;
using C_Challenges.Challenges.DirReduction;

foreach(var item in DirReduction.dirReduc(new string[] {"NORTH", "SOUTH", "EAST", "WEST", "NORTH", "SOUTH"}))
{
    System.Console.WriteLine(item);
}

