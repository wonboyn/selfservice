using System.Collections.Generic;

namespace SelfService.Models
{
    // Model for a skill
    public class Skill
    {
        public string name { get; set; }
        public string description { get; set; }
        public string category { get; set; }
        public string boturl { get; set; }
        public string docurl { get; set; }
        public string role { get; set; }
        public List<SkillParam> inputs { get; set; }
    }
}
