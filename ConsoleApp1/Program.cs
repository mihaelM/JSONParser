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
    }
}
