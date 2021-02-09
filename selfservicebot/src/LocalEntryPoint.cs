using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;

namespace SelfService
{
    // This class is only used for local testing.
    public class LocalEntryPoint
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                })

                // Add AWS Secrets Manager Configuration provider to
                // load secrets into the configuration object.
                // See https://github.com/Kralizek/AWSSecretsManagerConfigurationExtensions
                .ConfigureAppConfiguration((context, builder) =>
                {
                    builder.AddSecretsManager();
                });
    }
}
