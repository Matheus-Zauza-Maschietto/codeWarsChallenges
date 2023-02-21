using System.Text;
using System;
using System.Collections.Generic;

namespace C_Challenges.Challenges;
class MorseCodeDecoder
{
	public static string Decode(string morseCode)
	{
        Dictionary<string, string> dict = new Dictionary<string, string>(){{".-", "A"}, {"-...", "B"}, {"-.-.", "C"}, {"-..", "D"},
                                                                           {".", "E"}, {"..-.", "F"}, {"--.", "G"}, {"....", "H"}, {"..", "I"},
                                                                           {".---", "J"}, {"-.-", "K"}, {".-..", "L"}, {"--", "M"}, 
                                                                           {"-.", "N"}, {"---", "O"}, {".--.", "P"}, {"--.-", "Q"}, {".-.", "R"},
                                                                           {"...", "S"}, {"-", "T"}, {"..-", "U"}, {"...-", "V"}, {".--", "W"},
                                                                           {"-..-", "X"}, {"-.--", "Y"}, {"--..", "Z"}, {".----", "1"},
                                                                           {"..---", "2"}, {"...--", "3"}, {"....-", "4"}, {".....", "5"},
                                                                           {"-....", "6"}, {"--...", "7"}, {"---..", "8"}, {"----.", "9"},
                                                                           {"-----", "0"}, {"...---...", "SOS"}, {"", " "}, {"-.-.--", "!"}, {".-.-.-", "."}};
        StringBuilder builder = new StringBuilder();
        foreach(var letter in morseCode.Replace("   ", "  ").Split(' ')){
            builder.Append(dict[letter]);
        }
        
        return builder.ToString().Trim();
	}
}

