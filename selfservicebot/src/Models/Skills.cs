using System.Collections.Generic;

namespace SelfService.Models
{
    public class Skills
    {
        public string Name = "Skills";
        public List<Skill> SkillsList;

        public Skills()
        {
            SkillsList = new List<Skill>();
        }

        public void SetSkills(IList<Skill> skills)
        {
            foreach (Skill skill in skills)
            {
                SkillsList.Add(skill);
            }
        }
    }
}