### 1. Headless without any log message

Install SeleniumWebdriver, Chromedriver, SeleniumExtras from nuget and download Chromedriver.exe

> using OpenQA.Selenium.Chrome;
> using OpenQA.Selenium.Support.UI;
> using SeleniumExtras.WaitHelpers;

> ChromeOptions options = new ChromeOptions();

> options.AddArguments("--headless");

> options.SetLoggingPreference(LogType.Server, LogLevel.Off);

> ChromeDriverService service = ChromeDriverService.CreateDefaultService(<chromedriver-directory>);

> service.HideCommandPromptWindow = true;

> IWebDriver chrome = new ChromeDriver(service:service, options:options);

> WebDriverWait wait = new WebDriverWait(driver:chrome, timeout:TimeSpan.FromSeconds(<wait-seconds>));

> wait.Until(ExpectedConditions.PresenceOfAllElementsLocateBy(By.Id(idToFind)));

> String html = driver.PageSource;

> driver.close();

> Console.WriteLine("html source:");

> Console.WriteLine(html);
