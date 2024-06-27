import pandas as pd

# Example of mock data for different companies


def get_mock_data(company_name):
    return data.get(company_name, pd.DataFrame(columns=['title','description','url']))

microsoft = [
    {
        "source": {
            "id": None,
            "name": "PCMag.com"
        },
        "author": "Brian Westover",
        "title": "Microsoft Surface Pro (2024)",
        "description": "Arm makes this stunning flagship 2-in-1 a bit of a stretch\nWatching history circle around again is fascinating, especially at the intersection of laptops and tablet PCs. The original device that would eventually be called the Surface Pro remains a vivid memor…",
        "url": "https://uk.pcmag.com/laptops/153008/microsoft-surface-pro-2024",
        "urlToImage": "https://sm.pcmag.com/t/pcmag_uk/review/m/microsoft-/microsoft-surface-pro-2024_pt8m.1200.jpg",
        "publishedAt": "2024-06-26T20:24:59Z",
        "content": "Watching history circle around again is fascinating, especially at the intersection of laptops and tablet PCs. The original device that would eventually be called the Surface Pro remains a vivid memo… [+36810 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "PCMag.com"
        },
        "author": "Brian Westover",
        "title": "Microsoft Surface Pro (2024)",
        "description": "Arm makes this stunning flagship 2-in-1 a bit of a stretch\nWatching history circle around again is fascinating, especially at the intersection of laptops and tablet PCs. The original device that would eventually be called the Surface Pro remains a vivid memor…",
        "url": "https://me.pcmag.com/en/laptops/24371/microsoft-surface-pro-2024",
        "urlToImage": "https://sm.pcmag.com/t/pcmag_me/review/m/microsoft-/microsoft-surface-pro-2024_9yq6.1200.jpg",
        "publishedAt": "2024-06-26T20:24:59Z",
        "content": "Watching history circle around again is fascinating, especially at the intersection of laptops and tablet PCs. The original device that would eventually be called the Surface Pro remains a vivid memo… [+36810 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ZDNet"
        },
        "author": "Lance Whitney",
        "title": "Microsoft clamps down on Windows 11 users who want local accounts - but this trick still works",
        "description": "The company has removed online steps for switching from a Microsoft account to a local one and has killed off a past trick for choosing a local account in Windows 11.",
        "url": "https://www.zdnet.com/article/microsoft-clamps-down-on-windows-11-users-who-want-local-accounts-but-this-trick-still-works/",
        "urlToImage": "https://www.zdnet.com/a/img/resize/3c09121904f2d953d1e0cabbf43986f661c5a4a4/2024/06/26/426c1134-2459-474c-8fed-131a8e711b27/figure-top-microsoft-continues-to-wage-war-against-windows-11-users-who-want-local-accounts.jpg?auto=webp&fit=crop&height=675&width=1200",
        "publishedAt": "2024-06-26T20:09:10Z",
        "content": "Screenshot by Lance Whitney/ZDNET\r\nMicrosoft has long been battling Windows 11 users who'd rather sign in with a local account than the company's preferred Microsoft account. And with a couple of its… [+5392 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Mjtsai.com"
        },
        "author": "Michael Tsai",
        "title": "EU Charges Microsoft for Bundling Teams and Office",
        "description": "Kelvin Chan (via Hacker News): The European Commission said Monday it informed Microsoft of its preliminary view that the U.S. tech giant has been “restricting competition” by bundling Teams with core office productivity applications such as Office 365 and Mi…",
        "url": "https://mjtsai.com/blog/2024/06/26/eu-charges-microsoft-for-bundling-teams-and-office/",
        "urlToImage": None,
        "publishedAt": "2024-06-26T20:08:28Z",
        "content": "Kelvin Chan (via Hacker News):\r\nThe European Commission said Monday it informed Microsoft of its preliminary view that the U.S. tech giant has been “restricting competition” by bundling Teams with co… [+1469 chars]"
    },
    {
        "source": {
            "id": "financial-post",
            "name": "Financial Post"
        },
        "author": "GlobeNewswire",
        "title": "Quisitive Recognized as the Winner of 2024 Microsoft Analytics Partner of the Year",
        "description": "TORONTO, June 26, 2024 (GLOBE NEWSWIRE) — Quisitive Technology Solutions, Inc. (“Quisitive” or the “Company”) (TSXV: QUIS, OTCQX: QUISF), today announced it has won the Analytics 2024 Microsoft Partner of the Year Award. The Company was honored among a global…",
        "url": "https://financialpost.com/globe-newswire/quisitive-recognized-as-the-winner-of-2024-microsoft-analytics-partner-of-the-year",
        "urlToImage": None,
        "publishedAt": "2024-06-26T20:04:54Z",
        "content": "Author of the article:\r\nArticle content\r\nTORONTO, June 26, 2024 (GLOBE NEWSWIRE) Quisitive Technology Solutions, Inc. (Quisitive or the Company) (TSXV: QUIS, OTCQX: QUISF), today announced it has won… [+5595 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "GlobeNewswire"
        },
        "author": "Quisitive Technology Solutions Inc.",
        "title": "Quisitive Recognized as the Winner of 2024 Microsoft Analytics Partner of the Year",
        "description": "TORONTO, June 26, 2024 (GLOBE NEWSWIRE) -- Quisitive Technology Solutions, Inc. (“Quisitive” or the “Company”) (TSXV: QUIS, OTCQX: QUISF), today announced it has won the Analytics 2024 Microsoft Partner of the Year Award. The Company was honored among a globa…",
        "url": "https://www.globenewswire.com/news-release/2024/06/26/2904802/0/en/Quisitive-Recognized-as-the-Winner-of-2024-Microsoft-Analytics-Partner-of-the-Year.html",
        "urlToImage": "https://ml.globenewswire.com/Resource/Download/bdd1755f-f58e-4bf8-b5b9-c6fd2d8b1450",
        "publishedAt": "2024-06-26T20:00:00Z",
        "content": "TORONTO, June 26, 2024 (GLOBE NEWSWIRE) -- Quisitive Technology Solutions, Inc. (Quisitive or the Company) (TSXV: QUIS, OTCQX: QUISF), today announced it has won the Analytics 2024 Microsoft Partner … [+3366 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Skift"
        },
        "author": "Skift",
        "title": "Microsoft Exec Shares Xbox Lessons for Hotel Owners",
        "description": "Microsoft sees a future where everyone has a personal AI assistant and a digital ID, and travel companies with permission can tap into that data to create personalized experiences. -Justin Dawes",
        "url": "http://skift.com/2024/06/26/microsoft-exec-shares-xbox-lessons-for-hotel-owners/",
        "urlToImage": "https://skift.com/wp-content/uploads/2024/06/nocturnal_vapor_hero-92c6dcfc00d40365dd94-e1719430502932.jpg",
        "publishedAt": "2024-06-26T19:43:17Z",
        "content": "Xbox could teach the travel industry a few things about the customer experience.\r\nThats why Microsoft, which owns Xbox, is applying strategies from the gaming industry into next-generation tech produ… [+2627 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Microsoft.com"
        },
        "author": "Mark Russinovich",
        "title": "Mitigating Skeleton Key, a new type of generative AI jailbreak technique | Microsoft Security Blog",
        "description": "Microsoft recently discovered a new type of generative AI jailbreak method called Skeleton Key that could impact the implementations of some large and small language models. This new method has the potential to subvert either the built-in model safety or plat…",
        "url": "https://www.microsoft.com/en-us/security/blog/2024/06/26/mitigating-skeleton-key-a-new-type-of-generative-ai-jailbreak-technique/",
        "urlToImage": "https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2024/06/Featued-image.png",
        "publishedAt": "2024-06-26T19:39:21Z",
        "content": "In generative AI, jailbreaks, also known as direct prompt injection attacks, are malicious user inputs that attempt to circumvent an AI models intended behavior. A successful jailbreak has potential … [+10034 chars]"
    },
    {
        "source": {
            "id": "techradar",
            "name": "TechRadar"
        },
        "author": "allisa.james@futurenet.com (Allisa James)",
        "title": "Microsoft Surface Laptop 7 review: makes me believe in the Surface series again",
        "description": "The Microsoft Surface Laptop 7 has completely changed my mind about the Surface Laptop series.",
        "url": "https://www.techradar.com/computing/windows-laptops/microsoft-surface-laptop-7-review-makes-me-believe-in-the-surface-series-again",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/4bb7ZjQigJ4XBq9r5bDepE-1200-80.jpg",
        "publishedAt": "2024-06-26T19:27:57Z",
        "content": "Microsoft Surface Laptop 7: Two-minute review\r\nIt's no secret that I'm not fond of the Microsoft Surface Laptop series, so even with the Qualcomm Snapdragon X Elite chip and all the new Copilot+ AI b… [+11835 chars]"
    },
    {
        "source": {
            "id": "financial-post",
            "name": "Financial Post"
        },
        "author": "Business Wire",
        "title": "Crayon Recognized as the Winner of 2024 Microsoft Scale Solutions (LSP) Partner of the Year",
        "description": "OSLO, Norway — Crayon today announced it won the Scale Solutions (LSP) 2024 Microsoft Partner of the Year Award. The company was honored among a global field of top Microsoft partners for demonstrating excellence in innovation and implementation of customer s…",
        "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/crayon-recognized-as-the-winner-of-2024-microsoft-scale-solutions-lsp-partner-of-the-year",
        "urlToImage": None,
        "publishedAt": "2024-06-26T19:25:13Z",
        "content": "OSLO, Norway Crayon today announced it won the Scale Solutions (LSP) 2024 Microsoft Partner of the Year Award. The company was honored among a global field of top Microsoft partners for demonstrating… [+2523 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "PCMag.com"
        },
        "author": "Michael Kan",
        "title": "Microsoft: 'Skeleton Key' Jailbreak Can Trick Major Chatbots Into Behaving Badly",
        "description": "The jailbreak can prompt a chatbot to engage in prohibited behaviors, including generating content related to explosives, bioweapons, and drugs.\nMicrosoft has uncovered a jailbreak that allows someone to trick chatbots like ChatGPT or Google Gemini into overr…",
        "url": "https://uk.pcmag.com/ai/153003/microsoft-skeleton-key-jailbreak-can-trick-major-chatbots-into-behaving-badly",
        "urlToImage": "https://sm.pcmag.com/t/pcmag_uk/news/m/microsoft-/microsoft-skeleton-key-jailbreak-can-trick-major-chatbots-in_ju5k.1200.jpg",
        "publishedAt": "2024-06-26T19:23:40Z",
        "content": "Microsoft has uncovered a jailbreak that allows someone to trick chatbots like ChatGPT or Google Gemini into overriding their restrictions and engaging in prohibited activities.\r\nMicrosoft has dubbed… [+2174 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "PCMag.com"
        },
        "author": "Michael Kan",
        "title": "Microsoft: 'Skeleton Key' Jailbreak Can Trick Major Chatbots Into Behaving Badly",
        "description": "The jailbreak can prompt a chatbot to engage in prohibited behaviors, including generating content related to explosives, bioweapons, and drugs.\nMicrosoft has uncovered a jailbreak that allows someone to trick chatbots like ChatGPT or Google Gemini into overr…",
        "url": "https://me.pcmag.com/en/ai/24364/microsoft-skeleton-key-jailbreak-can-trick-major-chatbots-into-behaving-badly",
        "urlToImage": "https://sm.pcmag.com/t/pcmag_me/news/m/microsoft-/microsoft-skeleton-key-jailbreak-can-trick-major-chatbots-in_y5sm.1200.jpg",
        "publishedAt": "2024-06-26T19:23:40Z",
        "content": "Microsoft has uncovered a jailbreak that allows someone to trick chatbots like ChatGPT or Google Gemini into overriding their restrictions and engaging in prohibited activities.\r\nMicrosoft has dubbed… [+2174 chars]"
    },
    {
        "source": {
            "id": "financial-post",
            "name": "Financial Post"
        },
        "author": "Business Wire",
        "title": "Adastra recognized as finalist of 2024 Analytics Microsoft Global Partner of the Year",
        "description": "TORONTO — Adastra today announced it has been named a finalist of the Analytics Microsoft Global Partner of the Year Award. The company received recognition among a group of top Microsoft partners for demonstrating innovation and successfully delivering custo…",
        "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/adastra-recognized-as-finalist-of-2024-analytics-microsoft-global-partner-of-the-year",
        "urlToImage": None,
        "publishedAt": "2024-06-26T19:15:03Z",
        "content": "TORONTO Adastra today announced it has been named a finalist of the Analytics Microsoft Global Partner of the Year Award. The company received recognition among a group of top Microsoft partners for … [+3146 chars]"
    },
    {
        "source": {
            "id": "financial-post",
            "name": "Financial Post"
        },
        "author": "Business Wire",
        "title": "Cognite Recognized as 2024 Microsoft Energy and Resources Partner of the Year",
        "description": "AUSTIN, Texas & OSLO, Norway — Cognite, the globally recognized authority in Data and AI for industry, today announced it has won the Energy and Resources 2024 Microsoft Partner of the Year Award. This is the third year in a row Microsoft has recognized Cogni…",
        "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/cognite-recognized-as-2024-microsoft-energy-and-resources-partner-of-the-year",
        "urlToImage": "https://smartcdn.gprod.postmedia.digital/financialpost/wp-content/uploads/2024/06/bw20240625998941_press-microsoft-award-2024-fullhd.jpeg",
        "publishedAt": "2024-06-26T19:04:55Z",
        "content": "AUSTIN, Texas &amp; OSLO, Norway Cognite, the globally recognized authority in Data and AI for industry, today announced it has won the Energy and Resources 2024 Microsoft Partner of the Year Award. … [+3951 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "GlobeNewswire"
        },
        "author": "AvePoint, Inc.",
        "title": "AvePoint Named a Winner in the 2024 Microsoft Partner of the Year Awards",
        "description": "As the winner in the Education category, AvePoint is now a six-time global Microsoft Partner of the Year Award winner As the winner in the Education category, AvePoint is now a six-time global Microsoft Partner of the Year Award winner",
        "url": "https://www.globenewswire.com/news-release/2024/06/26/2904790/0/en/AvePoint-Named-a-Winner-in-the-2024-Microsoft-Partner-of-the-Year-Awards.html",
        "urlToImage": "https://ml.globenewswire.com/Resource/Download/eac3b932-e8a0-46f0-b5b5-747a258b0661",
        "publishedAt": "2024-06-26T19:00:00Z",
        "content": "JERSEY CITY, N.J., June 26, 2024 (GLOBE NEWSWIRE) -- AvePoint (Nasdaq: AVPT), the global leader in robust data management and data governance, today announced it has won its sixth global Microsoft Pa… [+6600 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "GlobeNewswire"
        },
        "author": "Pax8",
        "title": "Pax8 Recognized as the Winner of 2024 Microsoft Global Partner of the Year",
        "description": "DENVER, June 26, 2024 (GLOBE NEWSWIRE) -- Pax8, the leading cloud commerce marketplace, today announced it has won the Global 2024 Microsoft Partner of the Year Award. The company was honored among a global field of top Microsoft partners for demonstrating ex…",
        "url": "https://www.globenewswire.com/news-release/2024/06/26/2904789/0/en/Pax8-Recognized-as-the-Winner-of-2024-Microsoft-Global-Partner-of-the-Year.html",
        "urlToImage": "https://ml.globenewswire.com/Resource/Download/c1556ec2-e63e-48f2-bd9c-8c6c717703bb",
        "publishedAt": "2024-06-26T19:00:00Z",
        "content": "DENVER, June 26, 2024 (GLOBE NEWSWIRE) -- Pax8, the leading cloud commerce marketplace, today announced it has won the Global 2024 Microsoft Partner of the Year Award. The company was honored among a… [+2779 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ZDNet"
        },
        "author": "Alison DeNisco Rayome",
        "title": "Buy a one-year subscription to Microsoft 365 for $45: Last chance",
        "description": "Access Office apps like Word, Excel, PowerPoint, and Outlook, along with 1TB of OneDrive cloud storage for 35% less with this deal -- the lowest price we've seen.",
        "url": "https://www.zdnet.com/article/buy-a-one-year-subscription-to-microsoft-365-for-45-last-chance/",
        "urlToImage": "https://www.zdnet.com/a/img/resize/acb2a576380ddaf1583ad9ef8192bcc385c46393/2024/01/30/0d94260e-ad03-4617-ac4d-12b2a2f64e65/microsoft-365-personal.jpg?auto=webp&fit=crop&height=675&width=1200",
        "publishedAt": "2024-06-26T18:30:19Z",
        "content": "ZDNET's recommendations are based on many hours of testing, research, and comparison shopping. We gather data from the best available sources, including vendor and retailer listings as well as other … [+1153 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "WebProNews"
        },
        "author": "Matt Milano",
        "title": "Microsoft Enables Windows 11 OneDrive Backup Without Asking",
        "description": "In yet another instance of strong-arming users, Microsoft has changed Windows 11 setup so OneDrive backup is enabled by default.",
        "url": "https://www.webpronews.com/microsoft-enables-windows-11-onedrive-backup-without-asking/",
        "urlToImage": "https://www.webpronews.com/wp-content/uploads/2023/11/Microsoft-OneDrive.jpg",
        "publishedAt": "2024-06-26T18:28:30Z",
        "content": "In yet another instance of strong-arming users, Microsoft has changed Windows 11 setup so OneDrive backup is enabled by default.\r\nSpotted by Neowin, Microsoft appears to have made the change without … [+1293 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "TechSpot"
        },
        "author": "Alfonso Maruccia",
        "title": "Microsoft subsidiary Nuance blamed for data-stealing incident caused by a former employee",
        "description": "Geisinger Health, one of the leading healthcare providers in the US, suffered a troublesome security breach after a former Nuance employee accessed patient data without authorization. Sensitive information on hundreds of thousands of people may have been stol…",
        "url": "https://www.techspot.com/news/103556-microsoft-subsidiary-nuance-blamed-data-stealing-incident-caused.html",
        "urlToImage": "https://www.techspot.com/images2/news/bigimage/2024/06/2024-06-26-image-23.jpg",
        "publishedAt": "2024-06-26T17:46:00Z",
        "content": "Facepalm: When it comes to digital data management and user privacy, disgruntled former employees can become a threat for a number of reasons. Such an incident occurred in November 2023, with Microso… [+2040 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Neowin"
        },
        "author": "John Callaham",
        "title": "A Microsoft patent may show what the canceled Xbox Keystone streaming console looked like",
        "description": "A Microsoft patent that was first filed back in 2022 allegedly shows the design of Xbox Keystone, a streaming-only game console that the company developed but later decided to cancel. Read more...",
        "url": "https://www.neowin.net/news/a-microsoft-patent-may-show-what-the-canceled-xbox-keystone-streaming-console-looked-like/",
        "urlToImage": "https://cdn.neowin.com/news/images/uploaded/2024/06/1719422102_xbox-keystone-patent_story.jpg",
        "publishedAt": "2024-06-26T17:34:01Z",
        "content": "In 2021, Microsoft made some vague statements about developing an Xbox console that would stream games exclusively from its cloud services. In 2022, Microsoft confirmed those efforts, which it said h… [+1679 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Amazon.com"
        },
        "author": "aws@amazon.com",
        "title": "Amazon Linux announces availability of AL2023.5 with new versions of PHP and Microsoft .NET",
        "description": "Today are announcing the availability of the latest quarterly update to AL2023 containing the latest version of PHP and .NET, along with IPA Client and mod-php. Customers can take advantage of newer versions of PHP and .NET to ensure their applications are se…",
        "url": "https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-linux-al2023-5-versions-php-microsoft-net/",
        "urlToImage": "https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png",
        "publishedAt": "2024-06-26T17:00:00Z",
        "content": "Today are announcing the availability of the latest quarterly update to AL2023 containing the latest version of PHP and .NET, along with IPA Client and mod-php.\r\nCustomers can take advantage of newer… [+608 chars]"
    },
    {
        "source": {
            "id": "techradar",
            "name": "TechRadar"
        },
        "author": "Sead Fadilpašić",
        "title": "Microsoft console files are being exploited to let hackers gain access to private systems",
        "description": "MSC files used to target a known Windows flaw, allowing hackers to drop Cobalt Strike beacons.",
        "url": "https://www.techradar.com/pro/security/microsoft-console-files-are-being-exploited-to-let-hackers-gain-access-to-private-systems",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/Gy9BJ8WnmKgyVMLE625BxV-1200-80.jpg",
        "publishedAt": "2024-06-26T16:25:45Z",
        "content": "Hackers are now using custom-made MSC files to abuse a known, but unpatched, Windows cross-site scripting (XSS) vulnerability which could allows them to remotely execute malware or malicious code on … [+2108 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Tom's Hardware UK"
        },
        "author": "Jowi Morales",
        "title": "DEC PDP-10 owned by Microsoft co-founder coming to auction — $30k reserve on mainframe model behind firm's first commercial software",
        "description": "Christie's is set to auction off a DEC PDP-10 mainframe, similar to what Gates and Allen used to build the Altair BASIC — the first product Microsoft ever built.",
        "url": "https://www.tomshardware.com/tech-industry/dec-pdp-10-owned-by-microsoft-co-founder-coming-to-auction-dollar30k-reserve-on-mainframe-model-behind-firms-first-commercial-software",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/Uu3T7MTaUxRdrzDtFQkZXZ-1200-80.jpg",
        "publishedAt": "2024-06-26T16:02:08Z",
        "content": "A DEC PDP-10 mainframe computer from the Paul Allen (co-founder of Microsoft) collection, will be auctioned at Christie's in September. This mainframe computer is the same model Bill Gates and Paul A… [+4257 chars]"
    },
    {
        "source": {
            "id": "techradar",
            "name": "TechRadar"
        },
        "author": "John.Loeffler@futurenet.com (John Loeffler)",
        "title": "Microsoft Surface Pro 11 review: the best Surface ever — and it'll only get better",
        "description": "The Microsoft Surface Pro 11 had a high bar to clear, and it has absolutely made me a believer in Microsoft's vision for Windows-on-Arm.",
        "url": "https://www.techradar.com/computing/microsoft-surface-pro-11",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/gcySxH6HPHgaQ5ihNmi6FN-1200-80.jpg",
        "publishedAt": "2024-06-26T15:59:55Z",
        "content": "Microsoft Surface Pro 11: Three-minute review\r\nOK, so it's time for me to eat some crow.\r\nLast year around this time, I scoffed at the idea of Microsoft making its own Arm chip to power its Surface l… [+24090 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "cnbc.com",
        "title": "Nvidia, Apple, Amazon, Alphabet, Microsoft, Meta: Buy levels as entry points",
        "description": "Is it too late to get in on the Super Six?\nWe addressed that question back in late January to help investors who didn't own shares find some key entry points. Apple and Alphabet pulled back to the support levels we highlighted and have since rallied strongly.…",
        "url": "https://biztoc.com/x/0303a2f6e5448a10",
        "urlToImage": "https://biztoc.com/cdn/0303a2f6e5448a10_s.webp",
        "publishedAt": "2024-06-26T15:46:10Z",
        "content": "Is it too late to get in on the Super Six?We addressed that question back in late January to help investors who didn't own shares find some key entry points. Apple and Alphabet pulled back to the sup… [+128 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Neowin"
        },
        "author": "John Callaham",
        "title": "Microsoft Teams launches a new optimization architecture for virtual desktops in preview",
        "description": "Microsoft has announced it is rolling out a public preview of a new optimization architecture that is supposed to add new features and improve Teams support for virtual desktop users. Read more...",
        "url": "https://www.neowin.net/news/microsoft-teams-launches-a-new-optimization-architecture-for-virtual-desktops-in-preview/",
        "urlToImage": "https://cdn.neowin.com/news/images/uploaded/2023/01/1674764070_fotor_2023-1-27_1_13_35_story.jpg",
        "publishedAt": "2024-06-26T15:16:01Z",
        "content": "The new and revamped version of Microsoft Teams officially launched for the Windows and Mac platforms in October 2023, after several months in public preview. This week, the company revealed it is la… [+1835 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "go.theregister.com",
        "title": "Microsoft makes it harder to avoid OneDrive during new Windows 11 installs",
        "description": "Hey, OneDrive! Leave my files alone\nUser data is being slurped into Microsoft's cloud via OneDrive folder backup without user permission.…",
        "url": "https://biztoc.com/x/3f47354b0e2120b6",
        "urlToImage": "https://biztoc.com/cdn/799/og.png",
        "publishedAt": "2024-06-26T15:12:04Z",
        "content": "Hey, OneDrive! Leave my files aloneUser data is being slurped into Microsoft's cloud via OneDrive folder backup without user permission.\r\nThis story appeared on go.theregister.com, 2024-06-26."
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "benzinga.com",
        "title": "Dan Ives Labels Nvidia Correction A 'Near-Term Pullback', Hails Palantir As 'Purest AI Name' Amid Growing Market Use Cases - Microsoft (NASDAQ:MSFT), Apple (NASDAQ:AAPL)",
        "description": "The stock of NVIDIA Corp NVDA has seen a significant rebound after a recent correction, with a prominent analyst suggesting that the company’s market cap could reach $4 trillion. Additionally, the analyst has identified Palantir Technologies Inc. PLTR as the …",
        "url": "https://biztoc.com/x/3284fd97ffa561c3",
        "urlToImage": "https://biztoc.com/cdn/3284fd97ffa561c3_s.webp",
        "publishedAt": "2024-06-26T15:02:15Z",
        "content": "The stock of NVIDIA Corp NVDA has seen a significant rebound after a recent correction, with a prominent analyst suggesting that the companys market cap could reach $4 trillion. Additionally, the ana… [+128 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Theregister.com"
        },
        "author": "Richard Speed",
        "title": "Microsoft makes it harder to avoid OneDrive during new Windows 11 installs",
        "description": "Hey, OneDrive! Leave my files alone\nUser data is being slurped into Microsoft's cloud via OneDrive folder backup without user permission.…",
        "url": "https://www.theregister.com/2024/06/26/microsoft_makes_onedrive_avoidance_trickier/",
        "urlToImage": "https://regmedia.co.uk/2015/12/09/shutterstock_bureaucrat_paper_pusher.jpg",
        "publishedAt": "2024-06-26T15:00:06Z",
        "content": "User data is being slurped into Microsoft's cloud via OneDrive folder backup without user permission.\r\nFirst reported by Neowin, a change in Windows 11's setup for new devices has resulted in OneDriv… [+2047 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Quartz India"
        },
        "author": "William Gavin",
        "title": "GM taps ex-Amazon and Microsoft exec to lead self-driving startup Cruise amid comeback",
        "description": "General Motors has added two more members to the executive team overseeing self-driving startup Cruise’s comeback, including a new chief executive officer. Read more...",
        "url": "https://qz.com/general-motors-cruise-avs-robotaxis-whitten-xbox-amazon-1851561226",
        "urlToImage": "https://i.kinja-img.com/image/upload/c_fill,h_675,pg_1,q_80,w_1200/f87c8de1ae5ca287f6e1724735fee8c7.jpg",
        "publishedAt": "2024-06-26T14:40:00Z",
        "content": "General Motors has added two more members to the executive team overseeing self-driving startup Cruises comeback, including a new chief executive officer. \r\nMarc Whitten, one of the key engineers beh… [+2180 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "marketbeat.com",
        "title": "Microsoft Was Just Named a $600 Stock with a 33% Upside",
        "description": "$450.95 +3.28 (+0.73%) (As of 06/25/2024 ET)\n- 52-Week Range\n- $309.45\n▼\n$452.75 - Dividend Yield\n- 0.67%\n- P/E Ratio\n- 39.04\n- Price Target\n- $467.12\nWith its stock closing at another record high last night, around $450, it’s safe to say that Microsoft Inc N…",
        "url": "https://biztoc.com/x/e2756db0694b2821",
        "urlToImage": "https://biztoc.com/cdn/e2756db0694b2821_s.webp",
        "publishedAt": "2024-06-26T13:33:03Z",
        "content": "$450.95 +3.28 (+0.73%) (As of 06/25/2024 ET)- 52-Week Range- $309.45\r\n$452.75 - Dividend Yield- 0.67%- P/E Ratio- 39.04- Price Target- $467.12With its stock closing at another record high last night,… [+130 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "TechSpot"
        },
        "author": "Zo Ahmed",
        "title": "Microsoft opens Start menu to third-party Companions: Here's how to enable the feature",
        "description": "It's all part of the new Companions feature that showed up for Windows Insiders in build 26212 back in early May. As Tom's Hardware reports, any packaged app can now declare itself as a Start menu companion by tweaking a few lines in the manifest and pointing…",
        "url": "https://www.techspot.com/news/103547-microsoft-opens-start-menu-third-party-companions-here.html",
        "urlToImage": "https://www.techspot.com/images2/news/bigimage/2024/06/2024-06-26-image.jpg",
        "publishedAt": "2024-06-26T12:39:00Z",
        "content": "In context: Microsoft recently gave us a taste of Start menu widgets with Phone Link the Windows-Android syncing utility scoring some handy real estate. That's far from the only widget you'll be able… [+3108 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Slashdot.org"
        },
        "author": "feedfeeder",
        "title": "Only Hours Remain on This 35% Microsoft 365 Subscription Discount",
        "description": "You can save money on both individual and family subscriptions to Microsoft 365 -- but only until the end of the day.",
        "url": "https://slashdot.org/firehose.pl?op=view&amp;id=174320593",
        "urlToImage": None,
        "publishedAt": "2024-06-26T12:34:09Z",
        "content": "Did you know that if you took all the economists in the world and lined\r\nthem up end to end, they'd still point in the wrong direction?"
    },
    {
        "source": {
            "id": None,
            "name": "PC Gamer"
        },
        "author": "Nick Evanson",
        "title": "Grab your popcorn as Microsoft lands in hot water again with the EU for its 'insufficient' changes to how it bundles Teams",
        "description": "There's a potential fine of up to $20 billion if the Commission finds Microsoft guilty of breaching antitrust laws.",
        "url": "https://www.pcgamer.com/software/grab-your-popcorn-as-microsoft-lands-in-hot-water-again-with-the-eu-for-its-insufficient-changes-to-how-it-bundles-teams/",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/Sv3GL5WkoS3VdhqTitd9sY-1200-80.jpg",
        "publishedAt": "2024-06-26T12:11:55Z",
        "content": "The everlong battle between Microsoft and the European Commission gained a fresh page in its annals, as not only does the Commission believe the software giant has breached EU antitrust laws, but it … [+3415 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "investorplace.com",
        "title": "Microsoft Stock Predictions: Is MSFT Headed to $5 Trillion?",
        "description": "Currently, Microsoft (NASDAQ:MSFT) is the world’s most valuable company, with a market cap of $3.33 trillion. With a valuation like that, you may think that it’ll be difficult for the company to produce the level of growth necessary to drive the next needle-m…",
        "url": "https://biztoc.com/x/c38dfc20ed798e9e",
        "urlToImage": "https://biztoc.com/cdn/c38dfc20ed798e9e_s.webp",
        "publishedAt": "2024-06-26T11:44:09Z",
        "content": "Currently, Microsoft (NASDAQ:MSFT) is the worlds most valuable company, with a market cap of $3.33 trillion. With a valuation like that, you may think that itll be difficult for the company to produc… [+137 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "CNET"
        },
        "author": "Oliver Haslam",
        "title": "Only Hours Remain on This 35% Microsoft 365 Subscription Discount",
        "description": "You can save money on both individual and family subscriptions to Microsoft 365 -- but only until the end of the day.",
        "url": "https://www.cnet.com/deals/only-hours-remain-on-this-35-microsoft-365-subscription-discount/",
        "urlToImage": "https://www.cnet.com/a/img/resize/066d425e8b2105e7986709f477ee226bc6041e64/hub/2024/04/16/4420b500-acb8-496c-832d-b52a6add21b2/microsoft-365-family.png?auto=webp&fit=crop&height=675&width=1200",
        "publishedAt": "2024-06-26T11:44:00Z",
        "content": "If you're someone with a PC at home, you'll probably want a Microsoft 365 subscription. After all, it gives you access to a wide range of really useful apps, which are essential whether you're workin… [+1303 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Slashdot.org"
        },
        "author": "feedfeeder",
        "title": "The Morning After: Microsoft might be the latest company to violate antitrust laws",
        "description": "Nearly a year after the European Commission opened its investigation into Microsoft, the European Union’s executive body’s preliminary findings say the company violated antitrust laws by tying Microsoft Teams to its Office 365 and Microsoft 365 business suite…",
        "url": "https://slashdot.org/firehose.pl?op=view&amp;id=174320305",
        "urlToImage": None,
        "publishedAt": "2024-06-26T11:33:47Z",
        "content": "Nearly a year after the European Commission opened its investigation into Microsoft, the European Union’s executive body’s preliminary findings say the company violated antitrust laws by tying Micros… [+3253 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Yahoo Entertainment"
        },
        "author": "Mat Smith",
        "title": "The Morning After: Microsoft might be the latest company to violate antitrust laws",
        "description": "Nearly a year after the European Commission opened its investigation into Microsoft, the European Union’s executive body’s preliminary findings say the company violated antitrust laws by tying Microsoft Teams to its Office 365 and Microsoft 365 business suite…",
        "url": "https://consent.yahoo.com/v2/collectConsent?sessionId=1_cc-session_42fcc1db-64d1-46a1-95ea-bba1c7cc6159",
        "urlToImage": None,
        "publishedAt": "2024-06-26T11:15:16Z",
        "content": "If you click 'Accept all', we and our partners, including 237 who are part of the IAB Transparency &amp; Consent Framework, will also store and/or access information on a device (in other words, use … [+678 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Windows Central"
        },
        "author": "richard.devine@futurenet.com (Richard Devine)",
        "title": "My biggest issue with Copilot+ isn't Windows Recall, it's that Microsoft is ignoring millions of Windows users",
        "description": "Copilot+ is here, but hardly anyone can use it. In a world of bad headlines and millions of Windows users, why has Microsoft decided to freeze out those with capable hardware from the likes of NVIDIA?",
        "url": "https://www.windowscentral.com/software-apps/my-biggest-copilot-issue-isnt-windows-recall-its-microsoft-ignoring-users",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/2RzTjuXgGKFfH4d4UQMr4f-1200-80.jpg",
        "publishedAt": "2024-06-26T11:05:47Z",
        "content": "Copilot+ PCs are a big deal for Microsoft, Windows and the manufacturers that are making them. By all accounts, the Snapdragon X Elite chip powering most of the new breed is astonishingly good, and o… [+5167 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "XDA Developers"
        },
        "author": "Ayush Pande",
        "title": "Where did Microsoft go wrong with Windows 8?",
        "description": "Windows 8 brought a lot of design changes and new additions to the table. So, why did it end up as one of the most despised Windows operating systems?",
        "url": "https://www.xda-developers.com/where-did-microsoft-go-wrong-with-windows-8/",
        "urlToImage": "https://static1.xdaimages.com/wordpress/wp-content/uploads/wm/2024/06/windows-8-2-1.jpg",
        "publishedAt": "2024-06-26T11:00:13Z",
        "content": "Key Takeaways\r\n<ul><li>\r\n Windows 8 was too different from previous versions, leading users to revolt against its design changes and new features.\r\n </li><li>\r\n The attempt to cater to both tablet an… [+6177 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Grey Fox Wealth Advisors LLC Boosts Stock Holdings in Microsoft Co. (NASDAQ:MSFT)",
        "description": "Grey Fox Wealth Advisors LLC grew its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 11.4% during the first quarter, HoldingsChannel reports. The institutional investor owned 1,514 shares of the software giant’s stock after purchasing an a…",
        "url": "https://www.etfdailynews.com/2024/06/26/grey-fox-wealth-advisors-llc-boosts-stock-holdings-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:58:41Z",
        "content": "Grey Fox Wealth Advisors LLC grew its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 11.4% during the first quarter, HoldingsChannel reports. The institutional investor owned 1,51… [+6480 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Hospitalmanagement.net"
        },
        "author": "GlobalData",
        "title": "Community Health Network deploys Microsoft Azure, Nuance’s medical system",
        "description": "The move comes as part of the health system’s effort to transition its IT infrastructure to Azure to improve healthcare delivery.",
        "url": "https://www.hospitalmanagement.net/news/community-health-microsoft-azure-nuance/",
        "urlToImage": "https://s.yimg.com/ny/api/res/1.2/mp4cCaYdd8JUkp1VIHt.0g--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD02NzU-/https://media.zenfs.com/en/hospital_management_177/e1726f53c1308eb5e6bb59d0b9627327",
        "publishedAt": "2024-06-26T10:55:28Z",
        "content": "Community Health Network, a central Indiana, US-based health system, is set to transform its healthcare delivery and patient experiences through the comprehensive deployment of Microsoft Azure and th… [+2847 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Techreport.com"
        },
        "author": "Krishi Chowdhary",
        "title": "Microsoft Gets Charged by the EU for Violating Antitrust Regulations",
        "description": "On Tuesday (June 25), Microsoft was charged with violating antitrust regulations by the EU over its “abusive” bundling of Microsoft Teams and Microsoft Office products. What Exactly Is the Issue?...\nThe post Microsoft Gets Charged by the EU for Violating Anti…",
        "url": "https://techreport.com/news/microsoft-charged-eu-violating-antitrust-regulations/",
        "urlToImage": "https://techreport.com/wp-content/uploads/2024/06/ed-hardie-xG02JzIBf7o-unsplash-1-scaled.jpg?_t=1719398212",
        "publishedAt": "2024-06-26T10:33:47Z",
        "content": "<ul><li> The EU has sent a Statement of Objections to Microsoft, accusing it of violating antitrust regulations by bundling Microsoft Teams and other productivity tools.</li><li> If found guilty, Mic… [+2462 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Microsoft.com"
        },
        "author": "Microsoft Store",
        "title": "Buy Body Cam, Season 8 - Microsoft Store",
        "description": "Body Cam captures the up-close and dangerous world of police officers.",
        "url": "https://www.microsoft.com/en-us/p/season-8/8d6kgwxxww15",
        "urlToImage": "https://musicimage.xboxlive.com/catalog/video.tvseason.8D6KGWXXWW15/image?locale=en-us&mode=scale&purposes=BoxArt&w=120&h=120&q=60",
        "publishedAt": "2024-06-26T10:21:25Z",
        "content": "Season 8, Episode 1 TV-14CCHDCCSD\r\nA carjacking becomes a hostage situation, and a man sets a house on fire.\r\nSeason 8, Episode 2 TV-14CCHDCCSD\r\nA bar fight leads to a shoot-out with hostages, and a … [+885 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Microsoft Co. (NASDAQ:MSFT) Shares Sold by Shilanski & Associates Inc.",
        "description": "Shilanski & Associates Inc. decreased its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 0.7% during the first quarter, according to its most recent 13F filing with the Securities and Exchange Commission. The institutional investor owned 15,1…",
        "url": "https://www.etfdailynews.com/2024/06/26/microsoft-co-nasdaqmsft-shares-sold-by-shilanski-associates-inc/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:43Z",
        "content": "Shilanski &amp; Associates Inc. decreased its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 0.7% during the first quarter, according to its most recent 13F filing with the Securitie… [+6582 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Lakehouse Capital Pty Ltd Has $6.09 Million Stock Position in Microsoft Co. (NASDAQ:MSFT)",
        "description": "Lakehouse Capital Pty Ltd lowered its holdings in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 26.0% during the 1st quarter, according to its most recent Form 13F filing with the Securities and Exchange Commission (SEC). The institutional investor o…",
        "url": "https://www.etfdailynews.com/2024/06/26/lakehouse-capital-pty-ltd-has-6-09-million-stock-position-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:43Z",
        "content": "Lakehouse Capital Pty Ltd lowered its holdings in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 26.0% during the 1st quarter, according to its most recent Form 13F filing with the Securities… [+6633 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "MCIA Inc Acquires 294 Shares of Microsoft Co. (NASDAQ:MSFT)",
        "description": "MCIA Inc raised its holdings in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 9.5% in the first quarter, HoldingsChannel reports. The firm owned 3,398 shares of the software giant’s stock after buying an additional 294 shares during the quarter. Micr…",
        "url": "https://www.etfdailynews.com/2024/06/26/mcia-inc-acquires-294-shares-of-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:43Z",
        "content": "MCIA Inc raised its holdings in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 9.5% in the first quarter, HoldingsChannel reports. The firm owned 3,398 shares of the software giant’s stock af… [+6406 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Boston Standard Wealth Management LLC Has $724,000 Position in Microsoft Co. (NASDAQ:MSFT)",
        "description": "Boston Standard Wealth Management LLC trimmed its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 9.3% in the first quarter, according to the company in its most recent filing with the Securities and Exchange Commission (SEC). The institutiona…",
        "url": "https://www.etfdailynews.com/2024/06/26/boston-standard-wealth-management-llc-has-724000-position-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:42Z",
        "content": "Boston Standard Wealth Management LLC trimmed its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 9.3% in the first quarter, according to the company in its most recent filing with th… [+6973 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "RFG Advisory LLC Has $20.04 Million Stock Holdings in Microsoft Co. (NASDAQ:MSFT)",
        "description": "RFG Advisory LLC decreased its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 8.4% during the 1st quarter, according to its most recent 13F filing with the Securities & Exchange Commission. The fund owned 47,641 shares of the software giant’s…",
        "url": "https://www.etfdailynews.com/2024/06/26/rfg-advisory-llc-has-20-04-million-stock-holdings-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:41Z",
        "content": "RFG Advisory LLC decreased its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 8.4% during the 1st quarter, according to its most recent 13F filing with the Securities &amp; Exchange … [+6359 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Cornerstone Wealth Advisors Inc. Cuts Position in Microsoft Co. (NASDAQ:MSFT)",
        "description": "Cornerstone Wealth Advisors Inc. trimmed its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 17.2% during the 1st quarter, according to its most recent 13F filing with the Securities and Exchange Commission (SEC). The institutional investor…",
        "url": "https://www.etfdailynews.com/2024/06/26/cornerstone-wealth-advisors-inc-cuts-position-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:41Z",
        "content": "Cornerstone Wealth Advisors Inc. trimmed its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 17.2% during the 1st quarter, according to its most recent 13F filing with the Securiti… [+6886 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Allied Investment Advisors LLC Lowers Stake in Microsoft Co. (NASDAQ:MSFT)",
        "description": "Allied Investment Advisors LLC decreased its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 0.3% in the 1st quarter, according to its most recent 13F filing with the SEC. The firm owned 61,528 shares of the software giant’s stock after sel…",
        "url": "https://www.etfdailynews.com/2024/06/26/allied-investment-advisors-llc-lowers-stake-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:41Z",
        "content": "Allied Investment Advisors LLC decreased its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 0.3% in the 1st quarter, according to its most recent 13F filing with the SEC. The firm… [+6677 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Cadent Capital Advisors LLC Buys 480 Shares of Microsoft Co. (NASDAQ:MSFT)",
        "description": "Cadent Capital Advisors LLC grew its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 50.1% in the 1st quarter, according to the company in its most recent 13F filing with the SEC. The fund owned 1,438 shares of the software giant’s stock af…",
        "url": "https://www.etfdailynews.com/2024/06/26/cadent-capital-advisors-llc-buys-480-shares-of-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T10:20:41Z",
        "content": "Cadent Capital Advisors LLC grew its position in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 50.1% in the 1st quarter, according to the company in its most recent 13F filing with the SEC. … [+6508 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Yanko Design"
        },
        "author": "JC Torres",
        "title": "Microsoft Surface Pro 11, Surface Laptop 7 repairability gets thumbs up from iFixit",
        "description": "Microsoft Surface Pro 11, Surface Laptop 7 repairability gets thumbs up from iFixitIt has only been a month since Microsoft unveiled its latest Surface-branded computers, and while the tech industry was awash with discussions on the company’s...",
        "url": "https://www.yankodesign.com/2024/06/26/microsoft-surface-pro-11-surface-laptop-7-repairability-gets-thumbs-up-from-ifixit/",
        "urlToImage": "https://www.yankodesign.com/images/design_news/2024/06/microsoft-surface-pro-11-surface-laptop-7-repairability-gets-thumbs-up-from-ifixit/ms-surface-pro-laptop.jpg",
        "publishedAt": "2024-06-26T10:07:04Z",
        "content": "It has only been a month since Microsoft unveiled its latest Surface-branded computers, and while the tech industry was awash with discussions on the company’s aggressive Copilot AI push and ARM-base… [+2290 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Computerworld"
        },
        "author": "Preston Gralla",
        "title": "Congress warns Microsoft about foreign hackers again — will it matter this time?",
        "description": "To get things done using the power of the US government, President Theodore Roosevelt used to advise, “Speak softly and carry a big stick.” No need to rage and roar to accomplish what you want — instead, rely on the considerable power of the federal governmen…",
        "url": "https://www.computerworld.com/article/2501191/congress-warns-microsoft-about-foreign-hackers-again-will-it-matter-this-time.html",
        "urlToImage": "https://www.computerworld.com/wp-content/uploads/2024/06/usa_united_states_capitol_building_congress_by_uschools_gettyimages-607463592_abstract_digital_infrastructure_by_metamorworks_gettyimages-1129515465_2400x1600-100828809-orig.jpg?quality=50&strip=all&w=1024",
        "publishedAt": "2024-06-26T10:00:00Z",
        "content": "A year ago, the Chinese-government sponsored espionage group Storm-0558 conducted an audacious feat of hacking — it broke into the email accounts of high-level government officials, including Commerc… [+863 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ReadWrite"
        },
        "author": "Graeme Hanna",
        "title": "Microsoft accused of EU antitrust violation by bundling Teams",
        "description": "The European Commission has accused Microsoft of breaking EU antitrust rules by bundling its Teams communication app with its subscription… Continue reading Microsoft accused of EU antitrust violation by bundling Teams\nThe post Microsoft accused of EU antitru…",
        "url": "https://readwrite.com/microsoft-accused-of-eu-antitrust-violation-by-bundling-teams/",
        "urlToImage": "https://readwrite.com/wp-content/uploads/2024/06/mt.webp",
        "publishedAt": "2024-06-26T09:52:21Z",
        "content": "The European Commission has accused Microsoft of breaking EU antitrust rules by bundling its Teams communication app with its subscription services.\r\nThe regulator, which is the executive body of the… [+2249 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Meyer Handelman Co. Increases Position in Microsoft Co. (NASDAQ:MSFT)",
        "description": "Meyer Handelman Co. increased its position in Microsoft Co. (NASDAQ:MSFT – Free Report) by 3.0% during the 1st quarter, according to the company in its most recent disclosure with the Securities & Exchange Commission. The institutional investor owned 496,655 …",
        "url": "https://www.etfdailynews.com/2024/06/26/meyer-handelman-co-increases-position-in-microsoft-co-nasdaqmsft/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T09:44:42Z",
        "content": "Meyer Handelman Co. increased its position in Microsoft Co. (NASDAQ:MSFT – Free Report) by 3.0% during the 1st quarter, according to the company in its most recent disclosure with the Securities &amp… [+6341 chars]"
    },
    {
        "source": {
            "id": "techradar",
            "name": "TechRadar"
        },
        "author": "Craig Hale",
        "title": "The EU thinks Microsoft Teams is giving the company an unfair advantage",
        "description": "Tech giant remains under EU pressure following 2020 complaint about its bundling of Teams in Microsoft 365.",
        "url": "https://www.techradar.com/pro/the-eu-thinks-microsoft-teams-is-giving-the-company-an-unfair-advantage",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/nqNUTPym2nGuSizXkQNPR7-1200-80.jpg",
        "publishedAt": "2024-06-26T09:36:28Z",
        "content": "The European Union (EU) has formally accused Microsoft of breaching competition rules by bundling its Teams video conferencing app with its popular Microsoft 365 subscription.\r\nThe EU issued a statem… [+2273 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "ETF Daily News"
        },
        "author": "MarketBeat News",
        "title": "Microsoft Co. (NASDAQ:MSFT) Stock Position Raised by First Community Trust NA",
        "description": "First Community Trust NA raised its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 5.8% in the first quarter, according to the company in its most recent filing with the Securities and Exchange Commission. The fund owned 20,517 shares of the …",
        "url": "https://www.etfdailynews.com/2024/06/26/microsoft-co-nasdaqmsft-stock-position-raised-by-first-community-trust-na/",
        "urlToImage": "https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/microsoft-corporation-logo-1200x675.png&w=240&h=240&zc=2",
        "publishedAt": "2024-06-26T09:12:46Z",
        "content": "First Community Trust NA raised its stake in shares of Microsoft Co. (NASDAQ:MSFT – Free Report) by 5.8% in the first quarter, according to the company in its most recent filing with the Securities a… [+7024 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Neowin"
        },
        "author": "Taras Buria",
        "title": "Microsoft releases Edge 128 for testing in the Dev Channel",
        "description": "Microsoft Edge 128 is now available for testing in the Dev Channel. The first weekly update for version 128 adds a Copilot button for the built-in screenshot tool and fixes a bunch of various bugs. Read more...",
        "url": "https://www.neowin.net/news/microsoft-releases-edge-128-for-testing-in-the-dev-channel/",
        "urlToImage": "https://cdn.neowin.com/news/images/uploaded/2024/06/1719392646_edge_dev_128_story.jpg",
        "publishedAt": "2024-06-26T09:08:01Z",
        "content": "Microsoft Edge 128 has arrived in the Dev Channel for testing and weekly feature updates. Version 128.0.2661.0 is now available for insiders with a new Copilot button in the built-in screenshot tool … [+2122 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "wsj.com",
        "title": "Microsoft Wrestles With Rising Emissions From AI Ahead of Its 2030 Net-Zero Goal",
        "description": "Chief Sustainability Officer Melanie Nakagawa says she is open to the right kind of carbon offsets, small nuclear reactors and even more composting in her battle to improve the climate.",
        "url": "https://biztoc.com/x/82a7f2b189649755",
        "urlToImage": "https://biztoc.com/cdn/799/og.png",
        "publishedAt": "2024-06-26T08:37:09Z",
        "content": "Chief Sustainability Officer Melanie Nakagawa says she is open to the right kind of carbon offsets, small nuclear reactors and even more composting in her battle to improve the climate.\r\nThis story a… [+30 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Geeky Gadgets"
        },
        "author": "Julian Horsey",
        "title": "10+ Microsoft Copilot tips and tricks to improve your productivity",
        "description": "Microsoft Copilot is an innovative tool that can transform the way you work across various Microsoft applications. By using an understanding its advanced features and capabilities, you can significantly improve your productivity and achieve more in less time.…",
        "url": "https://www.geeky-gadgets.com/?p=431075",
        "urlToImage": "https://www.geeky-gadgets.com/wp-content/uploads/2024/06/MS-copilot-tips-and-tricks-2024.jpg",
        "publishedAt": "2024-06-26T08:28:11Z",
        "content": "Microsoft Copilot is an innovative tool that can transform the way you work across various Microsoft applications. By using an understanding its advanced features and capabilities, you can significan… [+8752 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "MediaNama.com"
        },
        "author": "Simone Lobo",
        "title": "European Commission accuses Microsoft of breaching EU anti-trust laws",
        "description": "Microsoft could face major penalties from the EU for allegedly limiting competition by tying Teams to its productivity suites. \nThe post European Commission accuses Microsoft of breaching EU anti-trust laws appeared first on MEDIANAMA.",
        "url": "https://www.medianama.com/2024/06/223-european-commission-accuses-microsoft-breaching-eu-anti-trust-laws/",
        "urlToImage": "https://www.medianama.com/wp-content/uploads/2023/09/ed-hardie-xG02JzIBf7o-unsplash-scaled-1.jpg",
        "publishedAt": "2024-06-26T08:23:41Z",
        "content": "The European Commission, based on its preliminary findings, has informed Microsoft that the company has violated EU antitrust rules by tying its communication and collaboration service, ‘Teams’, to i… [+2335 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Neowin"
        },
        "author": "Taras Buria",
        "title": "Microsoft fixed 'Open with' Windows 10 taskbar bug in KB5039299",
        "description": "If your Windows 10 PC is giving you a hard time when right-clicking apps on the taskbar, the latest non-security update is here to save the day. Microsoft fixed the \"Open with\" issue in KB5039299. Read more...",
        "url": "https://www.neowin.net/news/microsoft-fixed-open-with-windows-10-taskbar-bug-in-kb5039299/",
        "urlToImage": "https://cdn.neowin.com/news/images/uploaded/2023/06/1686472481_img19_story.jpg",
        "publishedAt": "2024-06-26T08:00:01Z",
        "content": "While most users probably ignore optional non-security updates for Windows 10 and 11 as they are not mandatory, sometimes, it is worth installing the latest preview release, especially when it fixes … [+1823 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "MSPoweruser"
        },
        "author": "Rafly Gilang",
        "title": "ChatGPT desktop app arrives on macOS, despite billions that Microsoft spent on OpenAI. Why?",
        "description": "ChatGPT desktop app on macOS is now available for everyone, but why did OpenAI release it for Windows' competitor first?\nThe post ChatGPT desktop app arrives on macOS, despite billions that Microsoft spent on OpenAI. Why? appeared first on MSPoweruser.",
        "url": "https://mspoweruser.com/chatgpt-desktop-app-arrives-on-macos-despite-billions-that-microsoft-spent-on-openai-why/",
        "urlToImage": "https://mspoweruser.com/wp-content/uploads/2024/06/chatgpt-desktop-app-macos.png",
        "publishedAt": "2024-06-26T07:01:41Z",
        "content": "A ChatGPT desktop app for macOS desktops has officially arrived, and it is now available to all users. The Microsoft-backed company said that all ChatGPT capabilities on the website are also rolling … [+1434 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Techmeme.com"
        },
        "author": None,
        "title": "Some CIOs say getting full value out of AI tools like Copilot for Microsoft 365 requires heavy lifting, as enterprise data isn't always accurate and up-to-date (Isabelle Bousquette/Wall Street Journal)",
        "description": "Isabelle Bousquette / Wall Street Journal:\nSome CIOs say getting full value out of AI tools like Copilot for Microsoft 365 requires heavy lifting, as enterprise data isn't always accurate and up-to-date  —  Getting full value out of AI workplace assistants is…",
        "url": "https://www.techmeme.com/240626/p6",
        "urlToImage": "https://images.wsj.net/im-973374/social",
        "publishedAt": "2024-06-26T06:30:04Z",
        "content": "About This Page\r\nThis is a Techmeme archive page.\r\nIt shows how the site appeared at 2:30 AM ET, June 26, 2024.\r\nThe most current version of the site as always is available at our home page.\r\nTo view… [+67 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "TweakTown"
        },
        "author": "Jak Connor",
        "title": "Microsoft faulted for massive hospital record data heist by former employee",
        "description": "Microsoft has been blamed for the theft of more than a million hospital patient records that were stolen by a former employee after their termination. Continue reading at TweakTown >",
        "url": "https://www.tweaktown.com/news/99017/microsoft-faulted-for-massive-hospital-record-data-heist-by-former-employee/index.html",
        "urlToImage": "https://static.tweaktown.com/news/9/9/99017_798798_microsoft-fired-an-employee-who-then-stole-hospital-records-of-1-million-patients_full.png",
        "publishedAt": "2024-06-26T05:34:02Z",
        "content": "An American healthcare provider that serves more than 1.2 million people is concerned a former employee from the Microsoft-owned Nuance Communications stole sensitive data on more than a million pati… [+1427 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "TweakTown"
        },
        "author": "Jak Connor",
        "title": "Microsoft moves to remove local Windows accounts and force Microsoft accounts",
        "description": "Microsoft has removed the instructions on its support page for Windows 11 users to switch from a Microsoft account to a local account. Continue reading at TweakTown >",
        "url": "https://www.tweaktown.com/news/99015/microsoft-moves-to-remove-local-windows-accounts-and-force/index.html",
        "urlToImage": "https://static.tweaktown.com/news/9/9/99015_615516_microsoft-moves-to-remove-local-accounts-from-windows-11-forcing_full.png",
        "publishedAt": "2024-06-26T05:02:01Z",
        "content": "Microsoft is moving to a world where a Windows user will be required to have a Microsoft account, and now the company has taken another step in that direction.\r\nBacked up version of the Microsoft sup… [+1494 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Nvidia.com"
        },
        "author": "Nate Bradford",
        "title": "Transforming Microsoft XLS and PPT Files into a Factory Digital Twin with OpenUSD",
        "description": "SyncTwin GmbH, a company that builds software to optimize production, intralogistics, and assembly, is on a mission to unlock industrial digital twins for small and medium-sized businesses (SMBs).",
        "url": "https://developer.nvidia.com/blog/transforming-microsoft-xls-and-ppt-files-into-a-factory-digital-twin-with-openusd/",
        "urlToImage": "https://developer-blogs.nvidia.com/wp-content/uploads/2024/06/synctwin-digital-twin-openusd-featured.png",
        "publishedAt": "2024-06-26T03:48:00Z",
        "content": "SyncTwin GmbH, a company that builds software to optimize production, intralogistics, and assembly, is on a mission to unlock industrial digital twins for small and medium-sized businesses (SMBs). \r\n… [+7649 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "scmp.com",
        "title": "EU hits Microsoft with antitrust charge for bundling Teams with Office, risking hefty fine",
        "description": "The EU competition watchdog’s latest action was triggered by a complaint from workspace messaging app Slack, owned by Salesforce.",
        "url": "https://biztoc.com/x/8b89cf76b11069b5",
        "urlToImage": "https://biztoc.com/cdn/8b89cf76b11069b5_s.webp",
        "publishedAt": "2024-06-26T03:09:35Z",
        "content": "The EU competition watchdogs latest action was triggered by a complaint from workspace messaging app Slack, owned by Salesforce.\r\nThis story appeared on scmp.com, 2024-06-26."
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "wsj.com",
        "title": "The EU charged Microsoft with antitrust violations over the bundling of its Teams collaboration tool with Office 365 and Microsoft 365",
        "description": "The EU charged Microsoft with antitrust violations over the bundling of its Teams collaboration tool with Office 365 and Microsoft 365.",
        "url": "https://biztoc.com/x/c828f37628a915b4",
        "urlToImage": "https://biztoc.com/cdn/799/og.png",
        "publishedAt": "2024-06-26T02:58:35Z",
        "content": "The EU charged Microsoft with antitrust violations over the bundling of its Teams collaboration tool with Office 365 and Microsoft 365.\r\nThis story appeared on wsj.com, 2024-06-26."
    },
    {
        "source": {
            "id": None,
            "name": "Commonsensewithmoney.com"
        },
        "author": "F2D",
        "title": "Microsoft Office – One Time Purchase – No Monthly Fees!",
        "description": "Get Microsoft Office Home & Business (One Time Purchase – No Monthly Fee) as low as $19.88! Save Up To 91%! This is a one time purchase – No Monthly Fees! This bundle is for families, students, and small businesses who want classic MS ...",
        "url": "https://www.commonsensewithmoney.com/microsoft-office-one-time-purchase-no-monthly-fees-92/",
        "urlToImage": "https://www.commonsensewithmoney.com/wp-content/uploads/2024/06/cmoffice-14.png",
        "publishedAt": "2024-06-26T02:31:49Z",
        "content": "Get Microsoft Office Home &amp; Business (One Time Purchase – No Monthly Fee) as low as $19.88! Save Up To 91%! This is a one time purchase – No Monthly Fees! This bundle is for families, students, a… [+453 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Ozbargain.com.au"
        },
        "author": "MetroCom",
        "title": "[Refurb] Microsoft Surface Book 3 13.5″ Touch i5-1035G7 8GB RAM 256GB SSD Iris WIN10 Pro $539 Delivered @ MetroCom",
        "description": "Hi all, got a batch of Surface Book 3 with Iris graphics card for sale today and also a Surface laptop 5.\nMinimum battery health is 80%.\n\nSpecs of the Surface Book 3\nProcessor\nIntel i5-1035G7\nMemory\n8GB\nOperating System\nWindows 10 Pro 64(EN:English)\nHard Driv…",
        "url": "https://www.ozbargain.com.au/node/853302",
        "urlToImage": "https://files.ozbargain.com.au/n/02/853302l.jpg?h=cf59e67e",
        "publishedAt": "2024-06-26T01:31:37Z",
        "content": "Hi all, got a batch of Surface Book 3 with Iris graphics card for sale today and also a Surface laptop 5.Minimum battery health is 80%.\r\nSpecs of the Surface Book 3ProcessorIntel i5-1035G7Memory8GBOp… [+737 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "go.theregister.com",
        "title": "Microsoft blamed for million-plus patient record theft at US hospital giant",
        "description": "Microsoft blamed for million-plus patient record theft at US hospital giant\nProbe: Worker at speech-recog outfit Nuance wasn't locked out after firing\nAmerican healthcare provider Geisinger fears highly personal data on more than a million of its patients has…",
        "url": "https://biztoc.com/x/651b83fb7b4b4f26",
        "urlToImage": "https://biztoc.com/cdn/651b83fb7b4b4f26_s.webp",
        "publishedAt": "2024-06-26T00:58:23Z",
        "content": "Microsoft blamed for million-plus patient record theft at US hospital giantProbe: Worker at speech-recog outfit Nuance wasn't locked out after firingAmerican healthcare provider Geisinger fears highl… [+139 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Theregister.com"
        },
        "author": "Brandon Vigliarolo",
        "title": "Microsoft blamed for million-plus patient record theft at US hospital giant",
        "description": "Probe: Worker at speech-recog outfit Nuance wasn't locked out after firing\nAmerican healthcare provider Geisinger fears highly personal data on more than a million of its patients has been stolen – and claimed a former employee at a Microsoft subsidiary is th…",
        "url": "https://www.theregister.com/2024/06/26/geisinger_nuance_microsoft/",
        "urlToImage": "https://regmedia.co.uk/2016/03/10/monitor_648x429.jpg",
        "publishedAt": "2024-06-26T00:44:06Z",
        "content": "American healthcare provider Geisinger fears highly personal data on more than a million of its patients has been stolen and claimed a former employee at a Microsoft subsidiary is the likely culprit.… [+2894 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Theregister.com"
        },
        "author": "Brandon Vigliarolo",
        "title": "Microsoft blamed for million-plus patient record theft at US hospital giant",
        "description": "Probe: Worker at speech-recog outfit Nuance wasn't locked out after firing American healthcare provider Geisinger fears highly personal data on more than a million of its patients has been stolen – and claimed a former employee at a Microsoft subsidiary is th…",
        "url": "https://www.theregister.com/2024/06/26/geisinger_nuance_microsoft_worker/",
        "urlToImage": "https://regmedia.co.uk/2024/06/26/shutterstock_nurse.jpg",
        "publishedAt": "2024-06-26T00:44:06Z",
        "content": "American healthcare provider Geisinger fears highly personal data on more than a million of its patients has been stolen and claimed a former employee at a Microsoft subsidiary is the likely culprit.… [+2901 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "C-sharpcorner.com"
        },
        "author": "Sigar Dave",
        "title": "Channel Types in Microsoft Teams: Public, Private, and Shared",
        "description": "Microsoft Teams offers Standard, Private, and Shared Channels to meet various communication needs. Standard Channels are open to all team members for general discussions. Private Channels are for specific members, ideal for confidential projects. Shared Chann…",
        "url": "https://www.c-sharpcorner.com/article/channel-types-in-microsoft-teams-public-private-and-shared/",
        "urlToImage": "https://www.c-sharpcorner.com/images/csharp-corner.png",
        "publishedAt": "2024-06-26T00:00:00Z",
        "content": "Microsoft Teams offers Standard, Private, and Shared Channels to meet various communication needs. Standard Channels are open to all team members for general discussions. Shared Channels enable cross… [+48 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Elastic.co"
        },
        "author": "Dusty Jackson,Hemant Malik,Lisa Troshian,Greg Crist,Jeff Maddocks,Brian Bergholm",
        "title": "Elastic wins 2024 Microsoft US Partner of the Year",
        "description": "Elastic was awarded 2024 Microsoft US Partner of the Year and ISV Innovation Finalist honors, affirming its premier standing as a dynamic Global ISV partner with Microsoft, driving forward industry in...",
        "url": "https://www.elastic.co/blog/elastic-wins-2024-microsoft-us-partner-of-the-year",
        "urlToImage": "https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt9156c06548feaab2/66631715a05fae19d7c2e572/MSFT-POTY-blog-720x420.png",
        "publishedAt": "2024-06-26T00:00:00Z",
        "content": "Microsoft's recognition of Elastic as the 2024 US Partner of the Year and a finalist in the ISV Innovation category is a significant achievement. This honor acknowledges our strong partnership, innov… [+1499 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "C-sharpcorner.com"
        },
        "author": "Sigar Dave",
        "title": "Microsoft Forms: New Features in 2024",
        "description": "Microsoft Forms has introduced powerful updates in 2024, including real-time data sync with Excel, a Practice Mode for learning reinforcement, a new Forms app for easy survey creation, and the ability to disable question numbers.",
        "url": "https://www.c-sharpcorner.com/article/microsoft-forms-new-features-in-2024/",
        "urlToImage": "https://www.c-sharpcorner.com/images/csharp-corner.png",
        "publishedAt": "2024-06-26T00:00:00Z",
        "content": "Microsoft Forms has introduced a range of powerful updates in 2024, enhancing its utility for creating, collecting, and analyzing data. Here’s a detailed overview of the new features.\r\nKey Features\r\n… [+1981 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "TechSpot"
        },
        "author": "Daniel Sims",
        "title": "Microsoft Flight Simulator 2024 feature showcase outlines ray tracing, on-foot gameplay, and more",
        "description": "Asobo Studio used this year's FlightSim Expo to explore the visual, gameplay, and physics improvements it plans to introduce in Microsoft Flight Simulator 2024. Launching on November 19, the update aims to add numerous activities that enable players to see th…",
        "url": "https://www.techspot.com/news/103545-microsoft-flight-simulator-2024-presentation-outlines-ray-tracing.html",
        "urlToImage": "https://www.techspot.com/images2/news/bigimage/2024/06/2024-06-25-image-22.jpg",
        "publishedAt": "2024-06-25T23:11:00Z",
        "content": "Something to look forward to: When Asobo unveiled Microsoft Flight Simulator 2024 last year, some might have seen it as a moderate upgrade over the already technically ambitious 2020 edition. Since t… [+2511 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Techrights.org"
        },
        "author": "Roy Schestowitz",
        "title": "Microsoft: By Default, Destroy Linux",
        "description": "For a lot of software on GNU/Linux, it is nowadays not possible to install/use without systemd",
        "url": "http://techrights.org/n/2024/06/24/Microsoft_By_Default_Destroy_Linux.shtml",
        "urlToImage": None,
        "publishedAt": "2024-06-25T23:09:24Z",
        "content": "posted by Roy Schestowitz on Jun 24, 2024,updated Jun 24, 2024\r\nEARLIER TODAY my wife updated her Debian laptop and she needed to enter \"Secure Boot\" password, a disturbing and now-common ritual even… [+1517 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Digital Trends"
        },
        "author": "Luke Larsen",
        "title": "The Microsoft AI CEO just dropped a huge hint about GPT-5",
        "description": "A towering figure in the world of AI just did a new interview where he talks about the future of GPT-5 and even GPT-6.",
        "url": "https://www.digitaltrends.com/computing/microsoft-ai-ceo-just-dropped-huge-hint-gpt-5/",
        "urlToImage": "https://www.digitaltrends.com/wp-content/uploads/2024/06/Mustafa-Suleyman-Featured-Image-1.jpg?resize=1200%2C630&p=1",
        "publishedAt": "2024-06-25T22:46:01Z",
        "content": "The timeline on GPT-5 continues to be a moving target, but a recent interview with Microsoft AI CEO Mustafa Suleyman sheds some light on what GPT-5 and even what its successor will be like.\r\nMustafa … [+4039 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Dealcatcher.com"
        },
        "author": None,
        "title": "Amazon - Racing Wheel Overdrive Designed for Xbox Series X|S By HORI - Officially Licensed by Microsoft $89.99",
        "description": "Amazon has this Racing Wheel Overdrive Designed for Xbox Series X|S By HORI - Officially Licensed by Microsoft on sale for $89.99 after clippable coupon. Plus, shipping is free.<br /><br /><strong>More Ways to Save at Amazon:</strong><ul><li>Don't already hav…",
        "url": "https://www.dealcatcher.com/video-games?offer=998253705",
        "urlToImage": "https://app.dealcatcher.com/bigly/998253705-607.jpg",
        "publishedAt": "2024-06-25T22:26:41Z",
        "content": "$89.99$119.99 (25% off) at Amazon\r\nAmazon has this Racing Wheel Overdrive Designed for Xbox Series X|S By HORI - Officially Licensed by Microsoft on sale for $89.99 after clippable coupon. Plus, ship… [+151 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "The Boston Globe"
        },
        "author": "Adam Satariano",
        "title": "EU charges Microsoft with antitrust violations over Teams bundling",
        "description": "European Union regulators said Microsoft bundling Teams gave it an unfair advantage over rivals.",
        "url": "https://www.bostonglobe.com/2024/06/25/business/eu-microsoft-antitrust-teams-bundling/",
        "urlToImage": "https://bostonglobe-prod.cdn.arcpublishing.com/resizer/SiYLgj0cx4mG5ccGwHHkwGuPauI=/506x0/cloudfront-us-east-1.images.arcpublishing.com/bostonglobe/ODT2KYFKUVTJQKHCKWVBWFVTDI.jpg",
        "publishedAt": "2024-06-25T22:12:17Z",
        "content": "LONDON European Union regulators on Tuesday charged Microsoft with breaking antitrust rules by bundling its Teams video conferencing and collaboration software with a suite of other productivity tool… [+2853 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Japan Today"
        },
        "author": None,
        "title": "EU accuses Microsoft of abusing dominant position with Teams",
        "description": "Microsoft violated EU antitrust rules by bundling its Teams communications app with its popular Office suite, Brussels said on Tuesday, as the U.S. tech giant vowed to do what it takes to address competition concerns. The charge sheet comes after the European…",
        "url": "https://japantoday.com/category/tech/eu-accuses-microsoft-of-abusing-dominant-position-with-teams",
        "urlToImage": None,
        "publishedAt": "2024-06-25T22:05:24Z",
        "content": "Microsoft violated EU antitrust rules by bundling its Teams communications app with its popular Office suite, Brussels said on Tuesday, as the U.S. tech giant vowed to do what it takes to address com… [+2304 chars]"
    },
    {
        "source": {
            "id": "the-verge",
            "name": "The Verge"
        },
        "author": "Antonio G. Di Benedetto",
        "title": "Forza Horizon 4 will be delisted from Microsoft stores and Steam in December",
        "description": "Digital sales of Playground Games’ Forza Horizon 4 will end on December 15th, when it will be pulled from Microsoft storefronts, Game Pass, and Steam.",
        "url": "https://www.theverge.com/2024/6/25/24185972/forza-horizon-4-xbox-pc-microsoft-steam-delisted",
        "urlToImage": "https://cdn.vox-cdn.com/thumbor/iUIGgBXl3g8R-aWcorEior2lEqI=/0x0:3840x2160/1200x628/filters:focal(1920x1080:1921x1081)/cdn.vox-cdn.com/uploads/chorus_asset/file/13200189/edecbd5e_4a92_4811_8a84_0fdc6e4baae3.jpg",
        "publishedAt": "2024-06-25T22:04:01Z",
        "content": "Forza Horizon 4 will be delisted from Microsoft stores and Steam in December\r\nForza Horizon 4 will be delisted from Microsoft stores and Steam in December\r\n / The racing game will be removed from Mic… [+2268 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "XDA Developers"
        },
        "author": "Rich Edmonds",
        "title": "How to install Microsoft Edge on Ubuntu",
        "description": "Stay inside Microsoft's ecosystem while using Linux",
        "url": "https://www.xda-developers.com/how-to-install-microsoft-edge-on-ubuntu/",
        "urlToImage": "https://static1.xdaimages.com/wordpress/wp-content/uploads/wm/2024/06/install-microsoft-edge-ubuntu-hero.jpg",
        "publishedAt": "2024-06-25T22:00:13Z",
        "content": "Firefox is the default web browser on a fresh Ubuntu installation, but there's good news if you prefer to use Microsoft's Chromium-based Edge as it's effortless to install. Microsoft Edge is supporte… [+2468 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Slashdot.org"
        },
        "author": "BeauHD",
        "title": "GM's Cruise Names Former Amazon, Microsoft Xbox Executive As New CEO",
        "description": "Cruise, the autonomous vehicle unit from General Motors, named Amazon and Microsoft executive Marc Whitten as its new CEO, replacing former CEO and co-founder Kyle Vogt. CNBC reports: Whitten was a founding engineer at Microsoft's Xbox before leaving the comp…",
        "url": "https://tech.slashdot.org/story/24/06/25/2125208/gms-cruise-names-former-amazon-microsoft-xbox-executive-as-new-ceo",
        "urlToImage": "https://a.fsdn.com/sd/topics/business_64.png",
        "publishedAt": "2024-06-25T21:40:00Z",
        "content": "Whitten was a founding engineer at Microsoft's Xbox before leaving the company after more than 17 years to become chief product officer of audio company Sonos in 2014, according to his LinkedIn profi… [+1307 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "barrons.com",
        "title": "Stock Market Today: Dow Falls Nearly 300 Points; Nasdaq Up; Nvidia, Microsoft, Super Micro, SolarEdge, FedEx, and More Movers; Treasury Yields",
        "description": "LIVE UPDATES\nStock Market News: Dow Dips\nThe S&P 500 and Nasdaq rose on the back of strong performance in technology.\nLast Updated:\nJune 25, 2024 at 4:19 PM EDT\nWhat to Watch Today\nMarkets were mixed Tuesday, with mostly technology stocks keeping things afloa…",
        "url": "https://biztoc.com/x/d35b116ac3ec6739",
        "urlToImage": "https://biztoc.com/cdn/799/og.png",
        "publishedAt": "2024-06-25T21:09:03Z",
        "content": "LIVE UPDATESStock Market News: Dow DipsThe S&amp;P 500 and Nasdaq rose on the back of strong performance in technology.Last Updated:June 25, 2024 at 4:19 PM EDTWhat to Watch TodayMarkets were mixed T… [+135 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "SiliconANGLE News"
        },
        "author": "Maria Deutscher",
        "title": "EU files antitrust charges against Microsoft for bundling Teams with Microsoft 365",
        "description": "European Union officials have tentatively determined that Microsoft Corp. breached the bloc’s antitrust rules with its Microsoft Teams collaboration service. The European Commission, the EU’s executive branch, published its findings today. The development is …",
        "url": "https://siliconangle.com/2024/06/25/eu-files-antitrust-charges-microsoft-bundling-teams-microsoft-365/",
        "urlToImage": "https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2024/06/microsoft-1.png",
        "publishedAt": "2024-06-25T21:01:04Z",
        "content": "European Union officials have tentatively determined that Microsoft Corp. breached the blocs antitrust rules with its Microsoft Teams collaboration service.\r\nThe European Commission, the EUs executiv… [+3714 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "cnbc.com",
        "title": "GM's Cruise names former Amazon, Microsoft Xbox executive as new CEO",
        "description": "General Motors' Cruise autonomous vehicle unit on Tuesday announced Marc Whitten, a former Amazon and Microsoft executive, as its new CEO.\n- His appointment comes at a crucial time for Cruise, as the GM subsidiary attempts to relaunch its autonomous vehicles …",
        "url": "https://biztoc.com/x/7366c82c5aa7f6be",
        "urlToImage": "https://biztoc.com/cdn/7366c82c5aa7f6be_s.webp",
        "publishedAt": "2024-06-25T20:47:26Z",
        "content": "General Motors' Cruise autonomous vehicle unit on Tuesday announced Marc Whitten, a former Amazon and Microsoft executive, as its new CEO.- His appointment comes at a crucial time for Cruise, as the … [+132 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "CNBC"
        },
        "author": None,
        "title": "GM's Cruise names former Amazon, Microsoft Xbox executive as new CEO",
        "description": "General Motors' Cruise autonomous vehicle unit on Tuesday announced Marc Whitten, a former Amazon and Microsoft executive, as its new CEO.",
        "url": "https://www.cnbc.com/2024/06/25/gms-cruise-names-former-amazon-microsoft-xbox-executive-as-new-ceo.html",
        "urlToImage": "https://image.cnbcfm.com/api/v1/image/107117284-1663017727791-gettyimages-1238159326-GM_CRUISE_VEHICLES.jpeg?v=1719341744&w=1920&h=1080",
        "publishedAt": "2024-06-25T20:29:13Z",
        "content": "DETROIT General Motors' Cruise autonomous vehicle unit on Tuesday announced former Amazon and Microsoft executive Marc Whitten as its new CEO.\r\nWhitten was a founding engineer at Microsoft's Xbox bef… [+3049 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "entrepreneur.com",
        "title": "A Microsoft-Partnered AI Startup Is Being Sued By the Biggest Record Labels in the World",
        "description": "The company is allegedly profiting from AI without compensating the human work that fed the technology, the lawsuit says.",
        "url": "https://biztoc.com/x/a149948394a49202",
        "urlToImage": "https://biztoc.com/cdn/a149948394a49202_s.webp",
        "publishedAt": "2024-06-25T20:24:05Z",
        "content": "The company is allegedly profiting from AI without compensating the human work that fed the technology, the lawsuit says.\r\nThis story appeared on entrepreneur.com, 2024-06-25."
    },
    {
        "source": {
            "id": None,
            "name": "Softpedia.com"
        },
        "author": "Softpedia Drivers",
        "title": "Microsoft Surface Laptop Go 2 Firmware/Driver 24.061.7285.0 for Windows 11",
        "description": "Driver Versions:- dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.107.139.0- WbfUsbDriver: 3.15.12011.10144- ibtusb: 23.30.0.3- MiniCtaDriver: 27.20.100.9624- iigd_dch_d: 27.20.100.9624- iigd_dch: 27.20.100.9624- dax3_ext_rtk: 8.605.313.22- DevicesTelemetry…",
        "url": "https://drivers.softpedia.com/get/Tablets/Microsoft/Microsoft-Surface-Laptop-Go-2-Firmware-Driver-24-061-7285-0-for-Windows-11.shtml",
        "urlToImage": "https://cdnssl.softpedia.com/_img/softpedia_logo_rss.png",
        "publishedAt": "2024-06-25T19:27:22Z",
        "content": "Driver Versions:\r\n- dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.107.139.0- WbfUsbDriver: 3.15.12011.10144- ibtusb: 23.30.0.3- MiniCtaDriver: 27.20.100.9624- iigd_dch_d: 27.20.100.9624- iigd_dch… [+4683 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Softpedia.com"
        },
        "author": "Softpedia Drivers",
        "title": "Microsoft Surface Laptop Go 2 Firmware/Driver 24.061.10038.0 for Windows 10",
        "description": "Driver Versions:- dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.107.139.0- WbfUsbDriver: 3.15.12011.10144- ibtusb: 23.30.0.3- MiniCtaDriver: 27.20.100.9624- iigd_dch_d: 27.20.100.9624- iigd_dch: 27.20.100.9624- dax3_ext_rtk: 8.605.313.22- DevicesTelemetry…",
        "url": "https://drivers.softpedia.com/get/Tablets/Microsoft/Microsoft-Surface-Laptop-Go-2-Firmware-Driver-24-061-10038-0-for-Windows-10.shtml",
        "urlToImage": "https://cdnssl.softpedia.com/_img/softpedia_logo_rss.png",
        "publishedAt": "2024-06-25T19:27:22Z",
        "content": "Driver Versions:\r\n- dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.107.139.0- WbfUsbDriver: 3.15.12011.10144- ibtusb: 23.30.0.3- MiniCtaDriver: 27.20.100.9624- iigd_dch_d: 27.20.100.9624- iigd_dch… [+4648 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Softpedia.com"
        },
        "author": "Softpedia Drivers",
        "title": "Microsoft Surface Laptop Studio Firmware/Driver June 2024 for Windows 11",
        "description": "Improvements and fixes:- Addresses an issue that prevented DFCI removal via network.- Resolves a problem that caused taskbar flickering and occasional device freezing when using Surface Slim Pen.- Provides a seamless experience when connecting two devices via…",
        "url": "https://drivers.softpedia.com/get/Tablets/Microsoft/Microsoft-Surface-Laptop-Studio-Firmware-Driver-June-2024-for-Windows-11.shtml",
        "urlToImage": "https://cdnssl.softpedia.com/_img/softpedia_logo_rss.png",
        "publishedAt": "2024-06-25T19:20:08Z",
        "content": "Improvements and fixes:\r\n- Addresses an issue that prevented DFCI removal via network.- Resolves a problem that caused taskbar flickering and occasional device freezing when using Surface Slim Pen.- … [+6523 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Softpedia.com"
        },
        "author": "Softpedia Drivers",
        "title": "Microsoft Surface Laptop Studio Firmware/Driver June 2024 for Windows 10",
        "description": "Improvements and fixes:- Addresses an issue that prevented DFCI removal via network.- Resolves a problem that caused taskbar flickering and occasional device freezing when using Surface Slim Pen.- Provides a seamless experience when connecting two devices via…",
        "url": "https://drivers.softpedia.com/get/Tablets/Microsoft/Microsoft-Surface-Laptop-Studio-Firmware-Driver-June-2024-for-Windows-10.shtml",
        "urlToImage": "https://cdnssl.softpedia.com/_img/softpedia_logo_rss.png",
        "publishedAt": "2024-06-25T19:20:07Z",
        "content": "Improvements and fixes:\r\n- Addresses an issue that prevented DFCI removal via network.- Resolves a problem that caused taskbar flickering and occasional device freezing when using Surface Slim Pen.- … [+6486 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Softpedia.com"
        },
        "author": "Softpedia Drivers",
        "title": "Microsoft Surface Book 3 Tablet Firmware/Driver 24.061.6112.0 for Windows 10",
        "description": "Versions: - dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.26.139.0- ibtusb: 23.30.0.3- iacamera64: 42.18362.3.12043- MiniCtaDriver: 30.0.101.3118- iigd_dch_d: 30.0.101.3118- iigd_dch: 30.0.101.3118- nvmsoegpu: 31.0.15.3758- dax3_ext_dolbyatmos: 5.224.130.…",
        "url": "https://drivers.softpedia.com/get/Tablets/Microsoft/Microsoft-Surface-Book-3-Tablet-Firmware-Driver-24-061-6112-0-for-Windows-10.shtml",
        "urlToImage": "https://cdnssl.softpedia.com/_img/softpedia_logo_rss.png",
        "publishedAt": "2024-06-25T19:13:57Z",
        "content": "Versions:\r\n- dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.26.139.0- ibtusb: 23.30.0.3- iacamera64: 42.18362.3.12043- MiniCtaDriver: 30.0.101.3118- iigd_dch_d: 30.0.101.3118- iigd_dch: 30.0.101.3… [+5833 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Softpedia.com"
        },
        "author": "Softpedia Drivers",
        "title": "Microsoft Surface Book 3 Tablet Firmware/Driver 24.061.6108.0 for Windows 11",
        "description": "Versions: - dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.26.139.0- ibtusb: 23.30.0.3- iacamera64: 42.18362.3.12043- MiniCtaDriver: 30.0.101.3118- iigd_dch_d: 30.0.101.3118- iigd_dch: 30.0.101.3118- nvmsoegpu: 31.0.15.3758- dax3_ext_dolbyatmos: 5.224.130.…",
        "url": "https://drivers.softpedia.com/get/Tablets/Microsoft/Microsoft-Surface-Book-3-Tablet-Firmware-Driver-24-061-6108-0-for-Windows-11.shtml",
        "urlToImage": "https://cdnssl.softpedia.com/_img/softpedia_logo_rss.png",
        "publishedAt": "2024-06-25T19:13:41Z",
        "content": "Versions:\r\n- dax3_swc_aposvc: 3.30508.581.0- SurfaceBattery: 2.26.139.0- ibtusb: 23.30.0.3- iacamera64: 42.18362.3.12043- MiniCtaDriver: 30.0.101.3118- iigd_dch_d: 30.0.101.3118- iigd_dch: 30.0.101.3… [+5832 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Biztoc.com"
        },
        "author": "theguardian.com",
        "title": "Microsoft faces huge antitrust fine over Teams app",
        "description": "Microsoft faces a hefty antitrust fine after the European Commission on Tuesday accused it of illegally linking its chat and video app Teams with its Office 365 suite of products including Word.\nThe allegations, which the US tech company can challenge, are th…",
        "url": "https://biztoc.com/x/af06dfc9fbc14869",
        "urlToImage": "https://biztoc.com/cdn/af06dfc9fbc14869_s.webp",
        "publishedAt": "2024-06-25T18:46:10Z",
        "content": "Microsoft faces a hefty antitrust fine after the European Commission on Tuesday accused it of illegally linking its chat and video app Teams with its Office 365 suite of products including Word.The a… [+138 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "PC Gamer"
        },
        "author": "Rich Stanton",
        "title": "Late Microsoft co-founder's treasure hoard of artefacts to be auctioned, includes a letter Einstein sent to Roosevelt that ultimately led to the Manhattan Project",
        "description": "As per Allen's wishes, all proceeds will go to philanthropy.",
        "url": "https://www.pcgamer.com/gaming-industry/late-microsoft-co-founders-treasure-hoard-of-artefacts-to-be-auctioned-includes-a-letter-einstein-sent-to-roosevelt-that-ultimately-led-to-the-manhattan-project/",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/gWdeVKjCcR6fYxjjtnKFLj-1200-80.jpg",
        "publishedAt": "2024-06-25T18:44:24Z",
        "content": "Paul Allen was the co-founder of Microsoft, a computing pioneer, and one of the world's great philanthropists. Allen died in 2018\r\n, at the age of 65, and at the time his co-founder Bill Gates paid t… [+3283 chars]"
    }
]

figma = [
    {
        "source": {
            "id": None,
            "name": "Small Business Trends"
        },
        "author": "Michael Guta",
        "title": "Wix Studio Introduces Figma Plugin for Seamless Design-to-Web Transition",
        "description": "Wix Studio launches a Figma plugin to seamlessly convert designs into interactive websites for better design efficiency and web functionality.",
        "url": "https://smallbiztrends.com/?p=1490761",
        "urlToImage": "https://smallbiztrends.com/wp-content/themes/sahifa/images/logo-full.jpg",
        "publishedAt": "2024-06-26T21:00:37Z",
        "content": "Wix.com Ltd. has announced the launch of a new plugin that allows professionals to export their Figma designs directly into the Wix Studio platform. This new tool, named the Figma to Wix Studio plugi… [+1947 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Slashdot.org"
        },
        "author": "feedfeeder",
        "title": "Figma announces big redesign with AI - The Verge",
        "description": "Figma announces big redesign with AIThe Verge Figma's new Slides app focuses on design, fun, and (oh, yeah!) AIFast Company A new Figma update make the design tool more powerful than everFast Company Figma Unveils New Redesign and AI Integration Features At C…",
        "url": "https://slashdot.org/firehose.pl?op=view&amp;id=174322851",
        "urlToImage": None,
        "publishedAt": "2024-06-26T18:53:22Z",
        "content": "Sign up for the Slashdot newsletter! OR check out the new Slashdot job board to browse remote jobs or jobs in your areaDo you develop on GitHub? You can keep using GitHub but automatically sync your … [+268 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Figma.com"
        },
        "author": "FelipeCortez",
        "title": "Figma Slides",
        "description": "Create custom presentations for any event with Figma Slides. Effortlessly design, customize, and share visually appealing slides to captivate your audience.",
        "url": "https://www.figma.com/slides/",
        "urlToImage": "https://cdn.sanity.io/images/599r6htc/regionalized/b07a7378e4af476668b732a6e70deec32851c5dc-2400x1260.png?w=1200&q=70&fit=max&auto=format",
        "publishedAt": "2024-06-26T18:04:34Z",
        "content": "Backed by our design platform, Figma Slides makes it easier than ever for teams to co-create narratives, engage their audience, and craft impressive slide decks."
    },
    {
        "source": {
            "id": None,
            "name": "Figma.com"
        },
        "author": None,
        "title": "Figma AI: Empowering designers with intelligent tools",
        "description": "We’re introducing a suite of AI-powered features to help you push past creative blocks and bring your best ideas to life.",
        "url": "https://www.figma.com/blog/introducing-figma-ai/",
        "urlToImage": "https://cdn.sanity.io/images/599r6htc/regionalized/d1ef1bc0c4df3219a0ee3d61e3b2160ffbd0f754-3840x2160.png?w=1200&q=70&fit=max&auto=format",
        "publishedAt": "2024-06-26T17:39:50Z",
        "content": "Since we first brought AI features into FigJam, weve been thinking about how to harness the power of AI in Figma. As with everything we do at Figma, our main goal is to give you the tools you need to… [+12174 chars]"
    },
    {
        "source": {
            "id": "the-verge",
            "name": "The Verge"
        },
        "author": "Jay Peters",
        "title": "Figma announces big redesign with AI",
        "description": "Figma is adding new generative AI tools to help people more easily make projects in the popular design app. It’s also adding a slides feature and introducing a redesign.",
        "url": "https://www.theverge.com/2024/6/26/24183730/figma-ai-tools-app-redesign-slides",
        "urlToImage": "https://cdn.vox-cdn.com/thumbor/-AMjR821g7hTj4QiNrpgB4PF5BY=/0x0:3840x2160/1200x628/filters:focal(1920x1080:1921x1081)/cdn.vox-cdn.com/uploads/chorus_asset/file/25501876/_External__Figma_AI.png",
        "publishedAt": "2024-06-26T16:15:00Z",
        "content": "Figma announces big redesign with AI\r\nFigma announces big redesign with AI\r\n / Figma is launching a presentation feature, too.\r\nByJay Peters, a news editor who writes about technology, video games, a… [+5635 chars]"
    },
    {
        "source": {
            "id": "techradar",
            "name": "TechRadar"
        },
        "author": "Sead Fadilpašić",
        "title": "Wix Studio brings Figma designs into the fold with a new tool",
        "description": "Wix Studio Figma is a plugin that allows designers to create dynamic web experiences more easily.",
        "url": "https://www.techradar.com/computing/software/wix-studio-brings-figma-designs-into-the-fold-with-a-new-tool",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/FcqyMkKE9A8BFo889K3ja6-1200-80.png",
        "publishedAt": "2024-06-26T13:14:17Z",
        "content": "Wix, one of the best website builders, just introduced a new tool, allowing Figma designers to import their work into Wix Studio more easily.\r\nThe tool, called Wix Studio Figma, is a plugin that allo… [+2203 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Toynewsi.com"
        },
        "author": "toynewsi.com",
        "title": "Good Smile Company Figma Delicous in Dungeon Laios Touden Figure",
        "description": "Good Smile Company Figma Delicous in Dungeon Laios Touden Figure",
        "url": "https://toynewsi.com/news.php?itemid=53344",
        "urlToImage": None,
        "publishedAt": "2024-06-26T12:39:48Z",
        "content": "Forums Communities: \r\nToy Fans -\r\nMarvel Fans - \r\nTransformers Fans\r\n@ToyNewsI Socials: \r\nFacebook -\r\nTwitter -\r\nInstagram\r\n@MarvelousNews Socials:\r\nFacebook - \r\nTwitter -\r\nInstagram\r\n@Tformers Socia… [+1010 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Creative Bloq"
        },
        "author": "joe.foley@futurenet.com (Joe Foley)",
        "title": "New Figma plugin aims to makes it easier to turn designs into websites",
        "description": "Here's how it works.",
        "url": "https://www.creativebloq.com/web-design/new-figma-plugin-aims-to-makes-it-easier-to-turn-designs-into-websites",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/2yC4DGUHnntCGzbQrSA6cA-1200-80.jpg",
        "publishedAt": "2024-06-25T06:00:26Z",
        "content": "Wix Studio has announced the introduction of a new Figma Plugin to help turn designs into functional, interactive websites using the Wix Studio’s no-code animations, CMS and other tools. It's somethi… [+1061 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Search Engine Journal"
        },
        "author": "Roger Montti",
        "title": "Wix Announces A Figma Plugin That Turns Designs Into Websites via @sejournal, @martinibuster",
        "description": "Wix's new Figma Plugin enables designers to export their Figma designs into Wix Studio to transform it into a functional website\nThe post Wix Announces A Figma Plugin That Turns Designs Into Websites appeared first on Search Engine Journal.",
        "url": "https://www.searchenginejournal.com/wix-figma-plugin/520510/",
        "urlToImage": "https://www.searchenginejournal.com/wp-content/uploads/2024/06/wix-figma-plugin-688.jpg",
        "publishedAt": "2024-06-24T13:00:47Z",
        "content": "Wix announced a new Figma Plugin that enables designers to import Figma designs directly into Wix Studio and dramatically speed up site creation from the design stage to a functioning website.\r\nFigma… [+1761 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Freebiesbug.com"
        },
        "author": "Pasquale Vitiello",
        "title": "10,000 Free Icons for Figma",
        "description": "A huge set of over 10,000 UI icons for Figma. Each icon fits in a tiny 24x24px space, and you can change the size and line thickness.\nThe post 10,000 Free Icons for Figma appeared first on Freebiesbug.",
        "url": "https://freebiesbug.com/figma-freebies/10000-free-figma-icons/",
        "urlToImage": "https://freebiesbug.com/wp-content/uploads/2024/06/unlimited-icons.jpg",
        "publishedAt": "2024-06-24T07:18:08Z",
        "content": "A huge set of over 10,000 UI icons designed by Mihai Burzo in Figma. Each icon fits in a tiny 24x24px space, and you can change the size and line thickness. With tons of icons and categories, this fr… [+106 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Framer.app"
        },
        "author": "quillzhou",
        "title": "Show HN: AI Magic for Figma",
        "description": "Article URL: https://textwise.qutesoft.com/\nComments URL: https://news.ycombinator.com/item?id=40772862\nPoints: 1\n# Comments: 0",
        "url": "https://eternal-follow-218401.framer.app/",
        "urlToImage": "https://framerusercontent.com/images/JaFkPfsyhWJRImj8vXDdP4V8Z58.png",
        "publishedAt": "2024-06-24T05:34:16Z",
        "content": "Need creative copy or polished text for your design projects? TextWise is your AI text generator. Input a prompt and get engaging copy, outlines, lists, bios, content ideas, and more, instantly tailo… [+455 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Siliconera"
        },
        "author": "Jenni Lada",
        "title": "Legend of Zelda: Tears of the Kingdom Ganondorf and Zelda Figma Show Up",
        "description": "Back in February 2024 at WonHobby 38, Good Smile Company revealed The Legend of Zelda: Tears of the Kingdom Ganondorf and Zelda figma. At Smile Fest 2024, we got to see the latest progress on both of those figure prototypes.\n\n\nWhen The Legend of Zelda: Tears …",
        "url": "https://www.siliconera.com/legend-of-zelda-tears-of-the-kingdom-ganondorf-and-zelda-figma-show-up/",
        "urlToImage": "https://www.siliconera.com/wp-content/uploads/2024/06/legend-of-zelda-tears-of-the-kingdom-ganondorf-and-zelda-figma-show-up.jpg",
        "publishedAt": "2024-06-22T03:05:00Z",
        "content": "Back in February 2024 at WonHobby 38, Good Smile Company revealed The Legend of Zelda: Tears of the Kingdom Ganondorf and Zelda figma. At Smile Fest 2024, we got to see the latest progress on both of… [+1235 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Nintendo Life"
        },
        "author": "Liam Doolan",
        "title": "Zelda 'Tears Of The Kingdom' Figma Prototype Unveiled, Here's A First Look",
        "description": "Joining Link and Ganondorf.It's been an incredibly exciting week for Princess Zelda, with Nintendo announcing she'll be starring in her own game 'The Legend of Zelda: Echoes of Wisdom' this September. Now, to top it off, we've got our very first look at her f…",
        "url": "https://www.nintendolife.com/news/2024/06/zelda-tears-of-the-kingdom-figma-prototype-unveiled-heres-a-first-look",
        "urlToImage": "https://images.nintendolife.com/bfa28bdd69dd8/1280x720.jpg",
        "publishedAt": "2024-06-22T02:05:00Z",
        "content": "Image: Nintendo Life / Nintendo\r\nIt's been an incredibly exciting week for Princess Zelda, with Nintendo announcing she'll be starring in her own game 'The Legend of Zelda: Echoes of Wisdom' this Sep… [+891 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "GoNintendo"
        },
        "author": "jmaldonado",
        "title": "First look at Tears of the Kingdom Princess Zelda Figma Prototype shared",
        "description": "Laying in wait",
        "url": "https://gonintendo.com/contents/37073-first-look-at-tears-of-the-kingdom-princess-zelda-figma-prototype-shared",
        "urlToImage": "https://gonintendo.com/attachments/image/50070/file/medium-b1b8032dfbc702ba3a50487ba2a171d2.png",
        "publishedAt": "2024-06-21T23:12:00Z",
        "content": "Earlier this year we got the announcement that multiple Tears of the Kingdom characters would be receiving figures from Good Smile, particularly Link, Ganondorf, and Zelda. While Link and Ganondorf h… [+400 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Freebiesbug.com"
        },
        "author": "Pasquale Vitiello",
        "title": "Free Portfolio Template for Figma in 3 Styles",
        "description": "Free portfolio template built with Figma, which is basically a landing page that stands out with its super fresh and modern style.\nThe post Free Portfolio Template for Figma in 3 Styles appeared first on Freebiesbug.",
        "url": "https://freebiesbug.com/figma-freebies/portfolio-for-figma-3-styles/",
        "urlToImage": "https://freebiesbug.com/wp-content/uploads/2024/06/portfolio-template.jpg",
        "publishedAt": "2024-06-19T18:37:54Z",
        "content": "A free portfolio template built with Figma, which is basically a landing page that stands out with its super fresh and modern style, on-point typography, and smart use of negative space.\r\nIt comes in… [+166 chars]"
    },
    {
        "source": {
            "id": "techradar",
            "name": "TechRadar"
        },
        "author": "waynewilliams@onmail.com (Wayne Williams)",
        "title": "Startup backed by Dropbox and Figma debuts breakthrough tech that could solve one of the biggest AI problems — AMD's BFF Lamini promises to cut hallucinations by 90% using mindmap-like process",
        "description": "Lamini Memory Tuning embeds exact facts into LLMs, cutting the problem of hallucinations by 90%.",
        "url": "https://www.techradar.com/pro/startup-backed-by-dropbox-and-figma-debuts-breakthrough-tech-that-could-solve-one-of-the-biggest-ai-problems-amds-bff-lamini-promises-to-cut-hallucinations-by-90-using-mindmap-like-process",
        "urlToImage": "https://cdn.mos.cms.futurecdn.net/AvZcjmUMtehpuha5oJLcTB-1200-80.jpg",
        "publishedAt": "2024-06-18T06:50:28Z",
        "content": "Anyone who has used generative AI for any length of time will be more than familiar with hallucinations. These are when AI systems generate false or misleading information, a flaw often rooted in lim… [+1956 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Uxdesign.cc"
        },
        "author": "Fabricio Teixeira",
        "title": "Human passion, undocking UX monoliths, type variables in Figma",
        "description": "“In an era where AI can paint like Picasso and write like Hemingway, the line between human genius and silicon savvy blurs. We were once advised to chase our dreams and turn our passions into…",
        "url": "https://uxdesign.cc/human-passion-undocking-ux-monoliths-type-variables-in-figma-877410add58e",
        "urlToImage": "https://miro.medium.com/v2/resize:fit:1200/0*pY4y0tWo-d_Pku9r.png",
        "publishedAt": "2024-06-17T09:35:38Z",
        "content": "In an era where AI can paint like Picasso and write like Hemingway, the line between human genius and silicon savvy blurs. We were once advised to chase our dreams and turn our passions into paycheck… [+263 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Designshack.net"
        },
        "author": "Roshan Perera",
        "title": "25+ Best Figma Mockups (Devices, Print, Products & More)",
        "description": "Figma has revolutionized the design world with its real-time collaboration and seamless design process. However, presenting your designs effectively often requires high-quality mockups that showcase your work in a realistic context. In this post, we dive into…",
        "url": "https://designshack.net/articles/inspiration/figma-mockup/",
        "urlToImage": "https://designshack.net/wp-content/uploads/figma-mockup.jpg",
        "publishedAt": "2024-06-17T08:00:46Z",
        "content": "Figma has revolutionized the design world with its real-time collaboration and seamless design process. However, presenting your designs effectively often requires high-quality mockups that showcase … [+8952 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Uxdesign.cc"
        },
        "author": "Allie Paschal",
        "title": "Setting up typography variables in Figma",
        "description": "Though I’m always excited by Figma’s new features, it can take me a minute to sit down and learn how to use them. This is especially true when I need to change my thinking about the structure of…",
        "url": "https://uxdesign.cc/set-up-typography-variables-in-figma-359cfea88b68",
        "urlToImage": "https://miro.medium.com/v2/resize:fit:1200/1*u6D-Xvk0-plK2YO2oEBgWA.png",
        "publishedAt": "2024-06-14T17:52:26Z",
        "content": "1. Set up text styles (if you dont already have them)\r\nI hate to break it to you, but you cant create typography variables without an existing text style. After creating all my color variables native… [+7342 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Applech2.com"
        },
        "author": "applech2",
        "title": "Apple、macOS 15 SequoiaやiOS/iPadOS 18、visionOS 2のSketch用デザインテンプレートを公開。今後Figmaでの提供も開始し、Adobe XDでの提供は終了。",
        "description": "AppleがmacOS 15 SequoiaとiOS/iPadOS 18のSketch用デザインテンプレートを公開。今後Figmaでの提供も開始するそうです。詳細は以下から。 　Appleは現地時間2024年06月11 […]\nThe post Apple、macOS 15 SequoiaやiOS/iPadOS 18、visionOS 2のSketch用デザインテンプレートを公開。今後Figmaでの提供も開始し、Adobe XDでの提供は終了。 first appeared on AAPL Ch..",
        "url": "https://applech2.com/archives/20240614-apple-design-resources-2024.html",
        "urlToImage": "https://applech2.com/wp-content/uploads/2024/06/macOS-Sequoia-and-iOS-18-Design-Templates-Hero.jpg",
        "publishedAt": "2024-06-14T02:09:11Z",
        "content": "ApplemacOS 15 SequoiaiOS/iPadOS 18SketchFigma\r\nApple20240611WWDC24iOS 18iPadOS 18iOS 1812macOS 15 SequoiavisionOS 2Sketch\r\n/macOS 15 SequoiavisionOS (2)TechnologiesApp Clips Design Template, Apple Pa… [+455 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Freebiesbug.com"
        },
        "author": "Pasquale Vitiello",
        "title": "Free Credit Cards Mockups – Figma",
        "description": "Free credit card mockups made with Figma, featuring color gradients in 4 versions with both Visa and Mastercard logos.\nThe post Free Credit Cards Mockups – Figma appeared first on Freebiesbug.",
        "url": "https://freebiesbug.com/figma-freebies/credit-cards-mockups/",
        "urlToImage": "https://freebiesbug.com/wp-content/uploads/2024/06/Credit-Cards-mockups.png",
        "publishedAt": "2024-06-12T07:32:25Z",
        "content": "Free credit card mockups made with Figma. These beautiful mockups feature color gradients in 4 versions, and both Visa and Mastercard styles are included, for a total of 8 variations.\r\n Download mock… [+1 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Uxdesign.cc"
        },
        "author": "Nicolás Del Real",
        "title": "Boolean logic in Figma — an introduction",
        "description": "Don’t be afraid my fellow designer. Let’s unmask the ‘truth’, the ‘false’, and the ‘not’. Or maybe not. Prototyping with logic is fun.\r\nContinue reading on UX Collective »",
        "url": "https://uxdesign.cc/boolean-logic-in-figma-an-introduction-f52394760c83",
        "urlToImage": "https://miro.medium.com/v2/resize:fit:1200/1*DqtTBCcjzpUFposJQaeZIQ.png",
        "publishedAt": "2024-06-10T20:53:36Z",
        "content": "Its 2024. Spaghetti Prototyping died last year. We already reviewed the new way of prototyping with variables here. Today, if we aim for state-of-the-art prototyping, we"
    },
    {
        "source": {
            "id": "financial-post",
            "name": "Financial Post"
        },
        "author": "GlobeNewswire",
        "title": "LambdaTest Introduces Smart UI Figma CLI to Streamline Visual Regression Testing for Design Teams",
        "description": "LambdaTest’s Smart UI Figma CLI simplifies visual regression testing of Figma designs directly from the command line, saving time and improving design quality. San Francisco, June 10, 2024 (GLOBE NEWSWIRE) — June 10, 2024, Noida/San Francisco: LambdaTest, a l…",
        "url": "https://financialpost.com/globe-newswire/lambdatest-introduces-smart-ui-figma-cli-to-streamline-visual-regression-testing-for-design-teams",
        "urlToImage": None,
        "publishedAt": "2024-06-10T15:00:29Z",
        "content": "Author of the article:\r\nArticle content\r\nLambdaTests Smart UI Figma CLI simplifies visual regression testing of Figma designs directly from the command line, saving time and improving design quality.… [+7071 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "GlobeNewswire"
        },
        "author": "Lambdatest, Inc.",
        "title": "LambdaTest Introduces Smart UI Figma CLI to Streamline Visual Regression Testing for Design Teams",
        "description": "LambdaTest's Smart UI Figma CLI simplifies visual regression testing of Figma designs directly from the command line, saving time and improving design quality. LambdaTest's Smart UI Figma CLI simplifies visual regression testing of Figma designs directly from…",
        "url": "https://www.globenewswire.com/news-release/2024/06/10/2896171/0/en/LambdaTest-Introduces-Smart-UI-Figma-CLI-to-Streamline-Visual-Regression-Testing-for-Design-Teams.html",
        "urlToImage": "https://ml.globenewswire.com/Resource/Download/8949f1b2-c2ee-41d2-b1fc-f11285e859fe",
        "publishedAt": "2024-06-10T15:00:00Z",
        "content": "San Francisco, June 10, 2024 (GLOBE NEWSWIRE) -- June 10, 2024, Noida/San Francisco: LambdaTest, a leading cloud-based unified testing platform, announces the launch of its innovative  Smart UI Figma… [+4415 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Freebiesbug.com"
        },
        "author": "Pasquale Vitiello",
        "title": "Business Card Mockups for Figma",
        "description": "Minimalist and elegant business card mockups made with Figma, available in both light and dark modes.\nThe post Business Card Mockups for Figma appeared first on Freebiesbug.",
        "url": "https://freebiesbug.com/psd-freebies/business-card-mockups/",
        "urlToImage": "https://freebiesbug.com/wp-content/uploads/2024/06/figma-business-card-mockups.jpg",
        "publishedAt": "2024-06-10T06:45:19Z",
        "content": "Minimalist and elegant business card mockups, available in both light and dark modes. It’s a free Figma resource that also includes a 3D version, all yours to use however you want.\r\n Download mockup"
    },
    {
        "source": {
            "id": None,
            "name": "Wonderlist.design"
        },
        "author": "Armendi",
        "title": "Show HN: I created a collection of 127 premium website designs in 1 Figma file",
        "description": "I’m excited (and a bit jealous) to share Wonderlist.design, my personal curated collection of 127 website designs, encompassing over 1130 unique pages. Coming from a digital creative agency, I can say that this resource is perfect for anyone who wants to get …",
        "url": "https://www.wonderlist.design/",
        "urlToImage": "https://cdn.prod.website-files.com/662a547170447eb2045b895c/6658736404e34603b3ab042b_Access%20127%20websites.jpg",
        "publishedAt": "2024-06-06T14:13:05Z",
        "content": "Design websites in minutes, not weeks\r\nSimplify your website creation journey, transitioning from weeks of tasks to effortless design in just minutes, all thanks to our user-friendly toolkit."
    },
    {
        "source": {
            "id": None,
            "name": "Uxdesign.cc"
        },
        "author": "Rosie Hoggmascall",
        "title": "Is Figma pushing too hard to get free users to premium?",
        "description": "There I was creating a Figjam board with some paywall inspo when I noticed a little free-text module crop up: In the next 2000 words, we’ll have a look at how Figma uses various entry points, UI…",
        "url": "https://uxdesign.cc/is-figma-pushing-too-hard-to-get-free-users-to-premium-37415393d411",
        "urlToImage": "https://miro.medium.com/v2/resize:fit:1200/1*2OhbIImlfSqfF7JSdAiiXQ.png",
        "publishedAt": "2024-06-06T11:53:38Z",
        "content": "Is Figma pushing too hard to get free users to premium?\r\nAfter over five years on Figma, I saw my first monetisation prompt last week.\r\nThere I was creating a Figjam board with some paywall inspo whe… [+5935 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Freebiesbug.com"
        },
        "author": "Pasquale Vitiello",
        "title": "Resolve: SaaS Figma Template",
        "description": "Resolve is a free Figma template for creating SaaS websites providing all the sections you need to showcase your SaaS nicely.\nThe post Resolve: SaaS Figma Template appeared first on Freebiesbug.",
        "url": "https://freebiesbug.com/figma-freebies/resolve-saas-figma/",
        "urlToImage": "https://freebiesbug.com/wp-content/uploads/2024/05/resolve-landing.jpg",
        "publishedAt": "2024-06-04T07:20:28Z",
        "content": "Resolve is a free Figma template for creating SaaS websites. The style is clean and minimal, and it has all the sections you need to showcase your SaaS nicely. Plus, it comes with 9 ready-to-go pages… [+100 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "GoNintendo"
        },
        "author": "rawmeatcowboy",
        "title": "Persona 5 Joker figma re-release available to pre-order, complete with Morgana bonus",
        "description": "We're not joking!",
        "url": "https://gonintendo.com/contents/36176-persona-5-joker-figma-re-release-available-to-pre-order-complete-with-morgana-bonus",
        "urlToImage": "https://gonintendo.com/attachments/image/48795/file/medium-5ea9c44f598fe24a9ad3ac6abff9ce6d.png",
        "publishedAt": "2024-06-03T00:07:00Z",
        "content": "Persona 5 Royal fans, nows your second chance to get in on a figma that has been sold out for quite some time.\r\nGood Smile Company has officially opened pre-orders for their Persona 5 Joker figma re-… [+749 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Siliconera"
        },
        "author": "Stephanie Liu",
        "title": "Persona 5 Joker Figma Re-Release Includes Morgana Figure",
        "description": "Good Smile Company has opened up pre-orders for a re-release of the Joker figma from Persona 5. Good Smile Company also offers a miniature Morgana that you can place by his side.\n\n\nPre-orders for the Persona 5 Joker figma figure close on July 10, 2024. Those …",
        "url": "https://www.siliconera.com/persona-5-joker-figma-re-release-includes-morgana-figure/",
        "urlToImage": "https://www.siliconera.com/wp-content/uploads/2024/05/persona-5-joker-figma-header-05312024.png",
        "publishedAt": "2024-06-02T17:30:47Z",
        "content": "Good Smile Company has opened up pre-orders for a re-release of the Joker figma from Persona 5. Good Smile Company also offers a miniature Morgana that you can place by his side.\r\nPre-orders for the … [+1543 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Business-opportunities.biz"
        },
        "author": "Carrol Strain",
        "title": "10 Essential Figma Tips and Tricks for Beginners",
        "description": "Use this list of the top 10 most important tips to fully utilize Figma.\nThe post 10 Essential Figma Tips and Tricks for Beginners appeared first on BUSINESS OPPORTUNITIES.",
        "url": "https://www.business-opportunities.biz/2024/05/28/10-essential-figma-tips-tricks-beginners/",
        "urlToImage": "https://www.business-opportunities.biz/wp-content/uploads/2024/05/figma-2.jpg",
        "publishedAt": "2024-05-28T22:34:55Z",
        "content": "Figma is an online application for designing user interfaces and altering visuals. Here are ten important Figma tips and tricks for beginners. The platform has been working to redefine cooperation in… [+4900 chars]"
    },
    {
        "source": {
            "id": None,
            "name": "Uxdesign.cc"
        },
        "author": "Fabricio Teixeira",
        "title": "Defining process, life outside of Figma, giving better design presentations",
        "description": "“Design thinking, double diamond, agile, scrum, lean UX, design sprint. Humans seek formulas. Formulas sell books, classes, and courses, and feed multi-million contracts where consultancies come in…",
        "url": "https://uxdesign.cc/defining-process-life-outside-of-figma-giving-better-design-presentations-9c5630104026",
        "urlToImage": "https://miro.medium.com/v2/resize:fit:1200/0*QgbBlX2UA5iUfxw9.png",
        "publishedAt": "2024-05-27T10:34:34Z",
        "content": "Design thinking, double diamond, agile, scrum, lean UX, design sprint. Humans seek formulas. Formulas sell books, classes, and courses, and feed multi-million contracts where consultancies come in to… [+236 chars]"
    }
]

data = {
    'microsoft': pd.DataFrame(microsoft),
    'figma': pd.DataFrame(figma)
}