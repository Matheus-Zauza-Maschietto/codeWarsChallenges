using System;
using System.Collections.Generic;
namespace C_Challenges.Challenges.DirReduction;
public class DirReduction {
  
    public static string[] dirReduc(string[] arr) {
        var Directions = new List<string>();
        foreach(string item in arr){
            Directions.Add(item);
        }

        // for(int index=0; index<Directions.Count; index++){
        //     if(Directions.Contains("NORTH") && Directions.Contains("SOUTH")){
        //         Directions.Remove("NORTH");
        //         Directions.Remove("SOUTH");
        //     }
        //     if(Directions.Contains("EAST") && Directions.Contains("WEST")){
        //         Directions.Remove("EAST");
        //         Directions.Remove("WEST");
        //     }
        // }
        for(int index=0; index<Directions.Count; index++){
            if(Directions[index] == "NORTH" && Directions[index+1] == "SOUTH"){
                Directions.RemoveAt(index);
                Directions.RemoveAt(index+1);
            }
            if(Directions[index] == "EAST" && Directions[index+1] == "WEST"){
                Directions.RemoveAt(index);
                Directions.RemoveAt(index+1);
            }
        }
        Directions.Sort();
        var array = new string[Directions.Count];
        for(int index=0;index<Directions.Count;index++){
            array[index]=Directions[index];
        }
        return array;
    }
}