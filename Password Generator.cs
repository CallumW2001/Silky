using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string pass = "";
            char letter1 = 'a';
            char letter2 = 'b';
            char letter3 = 'c';
            Random Rand = new Random();
            int num = 0;
            int num2 = 0;
            int num3 = 0;
            int num4 = Rand.Next(8, 16);
            Random rnd = new Random();

            while (pass.Length < num4)
            {
                if (pass.Length >= num4)
                {
                    break;
                }

                num = rnd.Next(65, 90);
                num2 = rnd.Next(48, 57);
                num3 = rnd.Next(97, 122);

                letter1 = Convert.ToChar(num);
                letter2 = Convert.ToChar(num2);
                letter3 = Convert.ToChar(num3);

                pass += letter1 + "" + letter2 + "" + letter3;

            }


            Console.WriteLine(pass);
            Console.ReadLine();

        }
    }
}
