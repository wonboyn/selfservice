using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

using System;
using System.Linq;
using System.Threading.Tasks;

namespace SelfService
{
    // This class provides the Lambda entrypoint
    // SelfService::SelfService.LambdaEntryPoint::FunctionHandlerAsync
    public class LambdaEntryPoint :

        Amazon.Lambda.AspNetCoreServer.APIGatewayProxyFunction
    {
        protected override void Init(IWebHostBuilder builder)
        {
            builder
                .UseStartup<Startup>();
        }

        protected override void Init(IHostBuilder builder)
        {
        }
    }
}
