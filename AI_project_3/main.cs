using System;

class PlantExpertSystem
{
    static void Main()
    {
        string color, hasThorns, hasSmell, hasFruits, hasSpikes, hasClimbingAbility, hasMedicinalProperties, hasEdibleParts, hasPoisonousParts, hasLargeLeaves, hasSmallFlowers;
        
        Console.WriteLine("欢迎使用植物专家系统！");
        
        Console.Write("植物的颜色是什么？（绿色、红色、黄色、紫色、白色、橙色、蓝色、粉色）：");
        color = Console.ReadLine();
        
        Console.Write("植物是否有刺？（是、否）：");
        hasThorns = Console.ReadLine();
        
        Console.Write("植物是否有香味？（是、否）：");
        hasSmell = Console.ReadLine();
        
        Console.Write("植物是否结实？（是、否）：");
        hasFruits = Console.ReadLine();
        
        Console.Write("植物是否有刺状突起？（是、否）：");
        hasSpikes = Console.ReadLine();
        
        Console.Write("植物是否具有攀爬能力？（是、否）：");
        hasClimbingAbility = Console.ReadLine();
        
        Console.Write("植物是否具有药用性质？（是、否）：");
        hasMedicinalProperties = Console.ReadLine();
        
        Console.Write("植物是否有可食用部分？（是、否）：");
        hasEdibleParts = Console.ReadLine();
        
        Console.Write("植物是否有毒部分？（是、否）：");
        hasPoisonousParts = Console.ReadLine();
        
        Console.Write("植物是否有大叶子？（是、否）：");
        hasLargeLeaves = Console.ReadLine();
        
        Console.Write("植物是否有小花？（是、否）：");
        hasSmallFlowers = Console.ReadLine();

        string species = IdentifyPlant(color, hasThorns, hasSmell, hasFruits, hasSpikes, hasClimbingAbility, hasMedicinalProperties, hasEdibleParts, hasPoisonousParts, hasLargeLeaves, hasSmallFlowers);
        
        Console.WriteLine("植物的种类是：" + species);
    }

    static string IdentifyPlant(string color, string hasThorns, string hasSmell, string hasFruits, string hasSpikes, string hasClimbingAbility, string hasMedicinalProperties, string hasEdibleParts, string hasPoisonousParts, string hasLargeLeaves, string hasSmallFlowers)
    {
        if (color == "绿色")
        {
            return "蕨类植物";
        }
        else if (color == "红色" && hasThorns == "是")
        {
            return "玫瑰";
        }
        else if (color == "红色" && hasThorns == "否")
        {
            return "郁金香";
        }
        else if (color == "黄色" && hasSmell == "是")
        {
            return "茉莉花";
        }
        else if (color == "黄色" && hasSmell == "否")
        {
            return "向日葵";
        }
        else if (color == "紫色")
        {
            return "薰衣草";
        }
        else if (color == "白色")
        {
            return "百合花";
        }
        else if (color == "橙色")
        {
            return "金盏花";
        }
        else if (color == "蓝色")
        {
            return "风铃草";
        }
        else if (color == "粉色")
        {
            return "樱花";
        }
        else
        {
            return "未知";
        }
    }
}
