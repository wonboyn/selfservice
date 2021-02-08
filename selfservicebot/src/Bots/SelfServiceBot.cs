using Microsoft.Bot.Builder;
using Microsoft.Bot.Builder.Dialogs;
using Microsoft.Bot.Schema;
using Microsoft.Extensions.Logging;

using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

using SelfService.Dialogs;

namespace SelfService.Bots
{
    public class SelfServiceBot : ActivityHandler
    {
        // Logger member variable
        protected readonly ILogger Logger;

        public SelfServiceBot(ILogger<SelfServiceBot> logger)
        {
            Logger = logger;
        }

        protected override async Task OnMessageActivityAsync(ITurnContext<IMessageActivity> turnContext, CancellationToken cancellationToken)
        {
            // Create Skills List Card
            Attachment attach = HelpDialog.CreateCard(this.Logger);

            // Return the adaptive card
            await turnContext.SendActivityAsync(MessageFactory.Attachment(attach), cancellationToken);
        }

        protected override async Task OnMembersAddedAsync(IList<ChannelAccount> membersAdded, ITurnContext<IConversationUpdateActivity> turnContext, CancellationToken cancellationToken)
        {
            var welcomeText = "Hello and welcome!";
            foreach (var member in membersAdded)
            {
                if (member.Id != turnContext.Activity.Recipient.Id)
                {
                    await turnContext.SendActivityAsync(MessageFactory.Text(welcomeText, welcomeText), cancellationToken);
                }
            }
        }
    }
}