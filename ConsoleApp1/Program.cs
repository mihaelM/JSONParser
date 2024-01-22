namespace parsejsondotnet2;
using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World 2!");
        string json;
        JObject array;
        using (StreamReader r = new StreamReader("./ConsoleApp1/jsonfile/SabotageSAS.mup"))
        {
            json = r.ReadToEnd();
            array = (JObject)JsonConvert.DeserializeObject(json);
        }
        Console.WriteLine("{0}", array.Count);

        string str1 = "Directly send maniuplated meassurement values to IED with process bus rogue device";
        string str2 = "Directly send maniuplated meassurement values to IED from process bus switch";
        List <string> lst = new List <string>();
        lst.Add(str1);
        lst.Add(str2);

        JObject array2 = (JObject)array["Sabotage IEC 61850 SAS"];


        foreach (var item in lst)
        {
            //findAndRemoveNode(item, array);
        }

    }

    public static void findAndRemoveNode(String item, JObject array)
    {
        Console.WriteLine(item);
        JToken value;

        if (array.TryGetValue(item, out value))
        {
            Console.WriteLine(value);
        }

    }
}
