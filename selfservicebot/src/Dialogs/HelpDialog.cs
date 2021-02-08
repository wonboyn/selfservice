using AdaptiveCards.Templating;

using Amazon;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

using Microsoft.Bot.Schema;
using Microsoft.Extensions.Logging;

using Newtonsoft.Json;

using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Threading.Tasks;

using SelfService.Models;

namespace SelfService.Dialogs
{
    public class HelpDialog
    {

        // Dynamo DB table name
        private static readonly string _tableName = "skills";

        // Skills List Adaptive Card template
        private static readonly string _skillsListTemplate = @"
        {
            ""$schema"": ""http://adaptivecards.io/schemas/adaptive-card.json"",
            ""type"": ""AdaptiveCard"",
            ""version"": ""1.2"",
            ""body"": [
                {
                    ""type"": ""TextBlock"",
                    ""text"": ""Skills List"",
                    ""weight"": ""bolder"",
                    ""size"": ""large""
                },
                {
                    ""type"": ""TextBlock"",
                    ""text"": ""The following skills are available"",
                    ""wrap"": true
                },
                {
                    ""type"": ""Container"",
                    ""spacing"": ""Large"",
                    ""items"": [
                        {
                            ""type"": ""ColumnSet"",
                            ""columns"": [
                                {
                                    ""type"": ""Column"",
                                    ""width"": ""stretch"",
                                    ""items"": [
                                        {
                                            ""type"": ""TextBlock"",
                                            ""weight"": ""Bolder"",
                                            ""text"": ""Skill""
                                        }
                                    ]
                                },
                                {
                                    ""type"": ""Column"",
                                    ""width"": ""stretch"",
                                    ""items"": [
                                        {
                                            ""type"": ""TextBlock"",
                                            ""weight"": ""Bolder"",
                                            ""text"": ""Description""
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    ""bleed"": true
                },
                {
                    ""type"": ""ColumnSet"",
                    ""columns"": [
                        {
                            ""type"": ""Column"",
                            ""width"": ""stretch"",
                            ""items"": [
                                {
                                    ""$data"": ""${SkillsList}"",
                                    ""type"": ""TextBlock"",
                                    ""text"": ""${name}"",
                                    ""wrap"": true
                                }
                            ]
                        },
                        {
                            ""type"": ""Column"",
                            ""width"": ""stretch"",
                            ""items"": [
                                {
                                    ""$data"": ""${SkillsList}"",
                                    ""type"": ""TextBlock"",
                                    ""text"": ""${description}"",
                                    ""wrap"": true
                                }
                            ]
                        }
                    ]
                }
            ]
        }";


        public static Attachment CreateCard(ILogger logger)
        {

            // Debug
            logger.LogInformation("Started processing CreateCard()");

            // Get list of skills from Dynamo DB
            IList<Skill> results = GetSkills().Result;

            // Convert the skills list to JSON
            Skills skills = new Skills();
            skills.SetSkills(results);
            var skillsJson = JsonConvert.SerializeObject(skills);

            // Create the Adaptive card
            var template = new AdaptiveCardTemplate(_skillsListTemplate);
            var cardJson = template.Expand(skillsJson);
            Attachment attach = new Attachment()
            {
                ContentType = "application/vnd.microsoft.card.adaptive",
                Content = JsonConvert.DeserializeObject(cardJson),
            };

            // Debug
            logger.LogInformation("Finished processing CreateCard()");

            // Finally, return the card
            return attach;
        }


        private static async Task<IList<Skill>> GetSkills()
        {
            // Setup DynamoDB context
            AWSConfigsDynamoDB.Context.TypeMappings[typeof(Skill)] = new Amazon.Util.TypeMapping(typeof(Skill), HelpDialog._tableName);
            var config = new DynamoDBContextConfig { Conversion = DynamoDBEntryConversion.V2 };
            IDynamoDBContext ddbContext = new DynamoDBContext(new AmazonDynamoDBClient(), config);

            // Retrieve skills from DynamoDB
            var search = ddbContext.ScanAsync<Skill>(null);
            IList<Skill> skillsList = await search.GetRemainingAsync();

            // Finally, return the list of skill objects
            return skillsList;
        }
    }
}