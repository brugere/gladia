from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "string",
        "name": "text",
        "example": "Input text to generate the headline from",
        "placeholder": "Insert text here to generate the headline from",
    },
    {
        "type": "integer",
        "name": "max_length",
        "example": "16",
        "placeholder": "Maximum length for the headline",
    },
]

output = {
    "name": "generated_headline",
    "type": "string",
    "example": """Very early yesterday morning, the United States President Donald Trump reported he and his wife First Lady Melania Trump tested positive for COVID-19. Officials said the Trumps' 14-year-old son Barron tested negative as did First Family and Senior Advisors Jared Kushner and Ivanka Trump.
    Trump took to social media, posting at 12:54 am local time (0454 UTC) on Twitter, "Tonight, [Melania] and I tested positive for COVID-19. We will begin our quarantine and recovery process immediately. We will get through this TOGETHER!" Yesterday afternoon Marine One landed on the White House's South Lawn flying Trump to Walter Reed National Military Medical Center (WRNMMC) in Bethesda, Maryland.
    Reports said both were showing "mild symptoms". Senior administration officials were tested as people were informed of the positive test. Senior advisor Hope Hicks had tested positive on Thursday.
    Presidential physician Sean Conley issued a statement saying Trump has been given zinc, vitamin D, Pepcid and a daily Aspirin. Conley also gave a single dose of the experimental polyclonal antibodies drug from Regeneron Pharmaceuticals.
    According to official statements, Trump, now operating from the WRNMMC, is to continue performing his duties as president during a 14-day quarantine. In the event of Trump becoming incapacitated, Vice President Mike Pence could take over the duties of president via the 25th Amendment of the US Constitution. The Pence family all tested negative as of yesterday and there were no changes regarding Pence's campaign events.""",
}

TaskRouter(
    router=router,
    input=inputs,
    output=output,
    default_model="michau-t5-base-en-generate-headline",
)