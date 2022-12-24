using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace C_Challenges.Challenges;

    class MorseCodeDecoder
{
	public static string Decode(string morseCode)
	{
        Dictionary<string, string> dict = new Dictionary<string, string>(){{"", " "}, {".-", "A"}, {"-…", "B"}, {"-.-.", "C"}, {"-..", "D"},
                                                                           {".", "E"}, {"..-.", "F"}, {"-.", "G"}, {"....", "H"}, {"..", "I"},
                                                                           {".-", "J"}, {"-.-", "K"}, {".-..", "L"}, {"-", "M"}};
        		List<string> strEnconded = new List<string>(morseCode.Split(" "));
        foreach(var item in strEnconded){
            System.Console.Write(item);
        }
        return "";
	}
}
